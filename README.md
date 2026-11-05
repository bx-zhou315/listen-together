# Listen Together · 同听一道

A mobile-friendly listening app for the Sunday Mandarin talks of St Helen's Bishopsgate (福音之家), built so that my family in China and in London can listen to the same talks each week.

**Live site:** https://bx-zhou315.github.io/listen-together/

## Features

- 200+ Mandarin talks from November 2022 onwards, browsable by date or by Bible book, with search
- In-page player with playback speed, previous/next talk, continuous play within a series, and resume from where you stopped
- The Bible passage and sermon handout for each talk, re-typeset in a large Kaiti font for older readers
- Listening history, download to phone, and offline playback of downloaded recordings
- Adjustable text size and light/dark themes; works in any phone browser
- Weekly auto-update: a scheduled GitHub Actions job checks for new Sunday talks and adds them automatically

## How it works

| File | Purpose |
|---|---|
| `index.html` | The whole app in one self-contained page (talk list, handouts, passages, font subset, illustrations) |
| `latest.json` | Talks published since the page was built; loaded by the page at start-up |
| `update.py` | Fetches new talks from the church's public resource library and writes `latest.json` |
| `.github/workflows/update.yml` | Runs `update.py` every Sunday evening and Monday morning |

## Sources and copyright

A personal project; not an official St Helen's Bishopsgate resource. Talk recordings and handouts belong to St Helen's Bishopsgate ([st-helens.org.uk](https://www.st-helens.org.uk)); audio streams directly from the church's servers. Scripture: 圣经新译本 (Chinese New Version), © Worldwide Bible Society. Font: LXGW WenKai (SIL Open Font Licence).
