#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic text cleaning for https://github.com/wannaphongcom/thaigov-corpus
- Remove leading and trailing spaces (str.strip())
- Remove blank lines

== Output Format ==
Title
(one blank line)
Article body, running with no blank line
(one blank line)
Source : url
(one blank line)

"""

from __future__ import unicode_literals
import codecs
import argparse
import re

def main():
    parser = argparse.ArgumentParser(
        description='Basic text cleaning. Remove leading and trailing spaces. Remove blank lines.')
    parser.add_argument('filename', type=str, nargs='+',
                        help='name of a file to clean')

    args = vars(parser.parse_args())
    filenames = args['filename']

    for filename in filenames:
        text = ''
        page_view_line = 0
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            for n, line in enumerate(f):
                line = line.strip()
                if n == 0: # title line
                    text = line + '\n'
                else:
                    if line:
                        if re.match(r'^[\d,]+$', line): # skip page view count
                            page_view_line = n
                            continue
                        if line == 'พิมพ์' and page_view_line and page_view_line < n: # skip 'print'
                            continue

                        if re.match(r'^ที่มา : http', line):
                            text = text + '\n\n' + line + '\n'
                        else:
                            text = text + '\n' + line

        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

if __name__ == "__main__":
    main()
