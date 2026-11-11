# Listen Together · 同听一道

A mobile-friendly listening app for the Sunday Mandarin talks of St Helen's Bishopsgate (福音之家). I built it so that my family, a few friends from church and their parents in China can listen to the same talks each week, wherever they are.

**Live site:** https://bx-zhou315.github.io/listen-together/

## Features

- 200+ Mandarin talks from November 2022 onwards, browsable by date or by Bible book, with search
- In-page player with playback speed, previous/next talk, continuous play within a series, and resume from where you stopped
- Lock-screen controls, plus automatic reconnection when the network drops mid-talk (useful when listening on a walk)
- The Bible passage and sermon handout for each talk, re-typeset in a large Kaiti font for older readers
- Listening history, download to phone, and offline playback of downloaded recordings
- Adjustable text size and light/dark themes; works in any phone browser
- A built-in guide to keeping playback going on a locked screen, for iPhone and the main Android brands used in China (Xiaomi, Huawei/Honor, OPPO, vivo)
- Daily auto-update: a scheduled GitHub Actions job checks for new Sunday talks and adds them automatically

## How it works

| File | Purpose |
|---|---|
| `index.html` | The whole app in one self-contained page (talk list, handouts, passages, font subset, illustrations) |
| `latest.json` | Talks published since the page was built; loaded by the page at start-up |
| `update.py` | Fetches new talks from the church's public resource library and writes `latest.json` |
| `.github/workflows/update.yml` | Runs `update.py` every Sunday evening and every morning, so talks uploaded late in the week are still picked up |

## Sources and copyright

A personal, non-commercial project shared privately with a small group; it is not an official St Helen's Bishopsgate resource and is not indexed by search engines.

- Talk recordings and handouts belong to St Helen's Bishopsgate ([st-helens.org.uk](https://www.st-helens.org.uk)). Audio streams directly from the church's servers and is not re-hosted here.
- Scripture texts are from The Holy Bible, Chinese New Version (圣经新译本), Copyright ©1976, 1992, 1999, 2001, 2005, 2010 by The Worldwide Bible Society Limited. All rights reserved.
- Font: LXGW WenKai (SIL Open Font Licence).
