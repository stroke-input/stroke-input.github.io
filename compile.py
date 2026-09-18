#!/usr/bin/env python3

import re
from collections import defaultdict

CCS_PATH = 'javascript/data/codepoint-character-sequence.txt'
SC_PATH = 'javascript/data/sequence-characters.txt'


class CompiledLine:
    def __init__(self, codepoint_hex: str, font_support: str, character: str, character_type: str, sequence_regex: str):
        self.codepoint_hex = codepoint_hex
        self.font_support = font_support
        self.character = character
        self.character_type = character_type
        self.sequence_regex = sequence_regex


def read_ccs() -> list[CompiledLine]:
    with open(CCS_PATH, 'r', encoding='utf-8') as ccs_file:
        lines = ccs_file.readlines()

    compiled_lines = []

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

        compiled_lines.append(CompiledLine(codepoint_hex, font_support, character, character_type, sequence_regex))

    return compiled_lines


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
    compiled_lines = read_ccs()
    sequences_from_character = read_sc()


if __name__ == '__main__':
    main()
