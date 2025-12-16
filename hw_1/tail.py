#!/usr/bin/env python3

import sys


def tail(lines, n=10):
    return lines[-n:] if len(lines) > n else lines


def process_file(filename, n=10):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"tail: {filename}: No such file or directory", file=sys.stderr)
        return
    except Exception as e:
        print(f"tail: {filename}: {e}", file=sys.stderr)
        return

    last_lines = tail(lines, n)
    for line in last_lines:
        print(line, end='')


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        multiple_files = len(files) > 1

        for filename in files:
            if multiple_files:
                print(f"==> {filename} <==")
            process_file(filename, n=10)
    else:
        lines = sys.stdin.readlines()
        last_lines = tail(lines, n=17)
        for line in last_lines:
            print(line, end='')


if __name__ == "__main__":
    main()

