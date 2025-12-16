#!/usr/bin/env python3

import sys


def count_stats(content):
    if isinstance(content, str):
        lines = content.count('\n')
        words = len(content.split())
        bytes_count = len(content.encode('utf-8'))
    else:
        lines = content.count(b'\n')
        words = len(content.split())
        bytes_count = len(content)

    return lines, words, bytes_count


def process_file(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        return count_stats(content)
    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory", file=sys.stderr)
        return None
    except Exception as e:
        print(f"wc: {filename}: {e}", file=sys.stderr)
        return None


def format_output(lines, words, bytes_count, filename=None):
    output = f"{lines:8d} {words:8d} {bytes_count:8d}"
    if filename:
        output += f" {filename}"
    print(output)


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for filename in files:
            stats = process_file(filename)
            if stats is not None:
                lines, words, bytes_count = stats
                total_lines += lines
                total_words += words
                total_bytes += bytes_count
                format_output(lines, words, bytes_count, filename)

        if len(files) > 1:
            format_output(total_lines, total_words, total_bytes, "total")
    else:
        content = sys.stdin.buffer.read()
        lines, words, bytes_count = count_stats(content)
        format_output(lines, words, bytes_count)


if __name__ == "__main__":
    main()

