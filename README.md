# The Excuse Your Agent Gives You

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/khususcrypto0000-coder/excuse-your-agent-gives-you-makefun/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/khususcrypto0000-coder/excuse-your-agent-gives-you-makefun/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

One-line entry for the make.fun bounty
**"The Excuse Your Agent Gives You"**
(`u-kevin-the-excuse-your-agent-gives-you-c1861261`).

## The entry

> Sorry — everything else in that deploy was hallucinated. The bug is the only real code I wrote.

The joke turns on a hallucination inversion: an agent that usually
*denies* hallucinating confesses that everything in the deploy was fake
— except the bug. The bug is the one thing it genuinely, provably did.
Ninety-five characters, one line, sharp turn at the end.

## Run

```bash
python3 main.py
```

Writes the entry to `/output/entry.txt` (UTF-8, one line, no trailing
newline), then reads it back and asserts it is byte-identical to the
intended text. Python standard library only (`os`, `sys`).

## Files

- `main.py` — writes and verifies the entry.
- `LICENSE` — MIT.
