#!/usr/bin/env python3
"""Print the response states used by Tencent Cloud International Advisor."""

STATES = {
    "VERIFIED": "Supported by a current public official source",
    "CONDITIONAL": "Supported only within documented conditions",
    "NOT_VERIFIED": "Current public evidence is insufficient",
    "VERIFIED_UNAVAILABLE": "Official documentation excludes the requested scope",
}


def main() -> None:
    for state, meaning in STATES.items():
        print(f"{state}: {meaning}")


if __name__ == "__main__":
    main()
