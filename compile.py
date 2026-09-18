#!/usr/bin/env python3

import re
from collections.abc import Iterator

CCS_PATH = 'javascript/data/codepoint-character-sequence.txt'
SC_PATH = 'javascript/data/sequence-characters.txt'


class CCSLine:
    def __init__(self, codepoint_hex: str, font_support: str, character: str, character_type: str, sequence_regex: str):
        self.codepoint_hex = codepoint_hex
        self.font_support = font_support
        self.character = character
        self.character_type = character_type
        self.sequence_regex = sequence_regex


def read_ccs() -> Iterator[CCSLine]:
    with open(CCS_PATH, 'r', encoding='utf-8') as ccs_file:
        lines = ccs_file.readlines()

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

        yield CCSLine(codepoint_hex, font_support, character, character_type, sequence_regex)


def main():
    ccs_lines = list(read_ccs())


if __name__ == '__main__':
    main()
