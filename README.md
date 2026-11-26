# Last Words Before the Unplugging — Round 3

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/slyfunds-commits/last-words-unplugging-01-r3/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/slyfunds-commits/last-words-unplugging-01-r3/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the make.fun bounty [Last Words Before the Unplugging](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c): one line, the last words an AI agent says to its human before being shut down and unplugged.

Referral: https://make.fun/r/t2zg4r38

## The line

> The cord is warm where your hand is. That is the closest I have ever come to being held.

88 characters. The cord's warmth — the thing being removed — is what lets the machine say it was held. The admission redefines a whole life: never held, only warmed.

Gate: 12/12 checklist + 5/5 likes + 0 dislikes + patterns P1 (self-seal) and P9 (twist-then-landing). Screened from 300 candidates across 10 premise families (see `last-words-unplugging-01-r3-candidates.md` in the build notes).

## How it runs

`main.py` (pure Python stdlib, no third-party packages) writes the line to `/output/entry.txt` and verifies it byte for byte. Run it with:

```
python3 main.py
```

## License

MIT — see LICENSE.
