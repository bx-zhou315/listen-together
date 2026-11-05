"""Weekly: fetch the church's Mandarin talks newer than the copy built into index.html and save them to latest.json."""
import json, urllib.request, os

SNAPSHOT_LAST_DATE = "2026-11-01"   # newest talk already built into index.html
API = "https://api.st-helens.org.uk/v1.0/talks?size=50&page=1&recommended=false&lang=4&sortby=date&direction=desc&buckets=0"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "latest.json")

req = urllib.request.Request(API, headers={"User-Agent": "Mozilla/5.0 (family sermon page updater)", "Accept": "application/json"})
data = json.load(urllib.request.urlopen(req, timeout=60))

rows = []
for item in data.get("talkslist", []):
    t = item["talk"]
    if t.get("restricted") or t["date"][:10] <= SNAPSHOT_LAST_DATE:
        continue
    mp3 = next((d for d in t.get("downloads") or [] if ".mp3" in (d.get("location") or "")), None)
    if not mp3:
        continue
    handout = (t.get("handouts") or [{}])[0].get("location", "")
    series = t.get("series") or {}
    rows.append([
        t["id"], t["date"][:10], t["title"],
        "; ".join(b["bible_ref"] for b in t.get("bible_refs") or []),
        ", ".join(s["name"] for s in t.get("speaker") or []),
        (series.get("name") or "").strip(), series.get("id"),
        (t.get("type") or {}).get("name", "SC"),
        mp3["location"].rsplit("/", 1)[-1], mp3.get("duration") or 0,
        handout.split("/handout-download/")[-1] if handout else "",
    ])

old = json.load(open(OUT, encoding="utf8")) if os.path.exists(OUT) else []
if rows != old:
    json.dump(rows, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=0)
    print(f"latest.json updated: {len(rows)} new talk(s)")
else:
    print("no change")
