#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and its number of steps."""


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
