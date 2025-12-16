#!/usr/bin/env python3

import sys


def number_lines(input_file=None):
    if input_file:
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"nl: {input_file}: No such file or directory", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"nl: {input_file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()

    for line_num, line in enumerate(lines, start=1):
        print(f"{line_num:6d}\t{line}", end="")


def main():
    number_lines(sys.argv[1]) if len(sys.argv) > 1 else number_lines()


if __name__ == "__main__":
    main()
