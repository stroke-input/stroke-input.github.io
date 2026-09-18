#!/usr/bin/env python3

import re
from collections import defaultdict

CCS_PATH = 'javascript/data/codepoint-character-sequence.txt'
SC_PATH = 'javascript/data/sequence-characters.txt'

CMD_PATH = 'lookup/index.cmd'


class CCSLine:
    def __init__(self, codepoint_hex: str, font_support: str, character: str, character_type: str, sequence_regex: str):
        self.codepoint_hex = codepoint_hex
        self.font_support = font_support
        self.character = character
        self.character_type = character_type
        self.sequence_regex = sequence_regex

    def body_row_cmd(self, sequences_from_character: dict[str, set[str]]) -> str:
        return '\n'.join([
            f'  //',
            f'    , U+{self.codepoint_hex}{self.font_support}',
            f'    , {self.character}{self.character_type}',
            f'    , `{self.sequence_regex}`',
            f'    ,',
            f'      ==',
            *[f'      - `{sequence}`' for sequence in sorted(sequences_from_character[self.character])],
            f'      ==',
        ])

    @staticmethod
    def head_row_cmd() -> str:
        return '\n'.join([
            '  //',
            '    ; Codepoint',
            '    ; Character',
            '    ; Regex',
            '    ; Sequences',
        ])


def read_ccs() -> list[CCSLine]:
    with open(CCS_PATH, 'r', encoding='utf-8') as ccs_file:
        lines = ccs_file.readlines()

    ccs_lines = []

    for line in lines:
        compliant_match = re.fullmatch(
            r'''
                U[+] (?P<codepoint_hex> [0-9A-F]{4,5} ) (?P<font_support> !?)
                    \t
                (?P<character> \S ) (?P<character_type> [\^*]? )
                    \t
                (?P<sequence_regex> [1-5|()\\]+ )
                    \n
            ''',
            line,
            flags=re.VERBOSE,
        )

        if not compliant_match:
            continue

        codepoint_hex = compliant_match.group('codepoint_hex')
        font_support = compliant_match.group('font_support')
        character = compliant_match.group('character')
        character_type = compliant_match.group('character_type')
        sequence_regex = compliant_match.group('sequence_regex')

        ccs_lines.append(CCSLine(codepoint_hex, font_support, character, character_type, sequence_regex))

    return ccs_lines


def read_sc() -> dict[str, set[str]]:
    with open(SC_PATH, 'r', encoding='utf-8') as sc_file:
        lines = sc_file.readlines()

    sequences_from_character = defaultdict(set)

    for line in lines:
        compliant_match = re.fullmatch(
            r'(?P<sequence> [1-5]+ ) \t (?P<characters> \S+ ) \n',
            line,
            flags=re.VERBOSE,
        )

        if not compliant_match:
            continue

        sequence = compliant_match.group('sequence')
        characters = compliant_match.group('characters')

        for character in characters:
            sequences_from_character[character].add(sequence)

    return sequences_from_character


def main():
    ccs_lines = read_ccs()
    sequences_from_character = read_sc()

    with open(CMD_PATH, 'r', encoding='utf-8') as read_file:
        read_cmd = read_file.read()

    data_table_cmd = '\n'.join([
        f'<## data-table ##>',
        f"''''",
        f'|^',
        CCSLine.head_row_cmd(),
        f'|:',
        *[ccs_line.body_row_cmd(sequences_from_character) for ccs_line in ccs_lines],
        f"''''",
        f'<## /data-table ##>',
    ])

    write_cmd = re.sub(
        '<## data-table ##>.*?<## /data-table ##>',
        repl=data_table_cmd.replace('\\', r'\\'),
        string=read_cmd,
        flags=re.DOTALL,
    )

    if write_cmd == read_cmd:
        return

    with open(CMD_PATH, 'w', encoding='utf-8') as write_file:
        write_file.write(write_cmd)


if __name__ == '__main__':
    main()
