import os, pathlib, requests

pmcids = {
    "PMC11540982": "CAD4TB accuracy 2024",
    "PMC10348531": "Three CAD systems accuracy 2023",
    "PMC9904090":  "AI algorithms in prisons 2022",
    "PMC10246158": "qXR accuracy 2023",
    "PMC6802077":  "Comparing CAD4TB/Lunit/qXR 2019"
}

base = "projects/ai_tb_meta/data/pdfs"
os.makedirs(base, exist_ok=True)

for pmcid, title in pmcids.items():
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/pdf"
    out = pathlib.Path(base)/f"{pmcid}.pdf"
    if out.exists() and out.stat().st_size>1024:
        print(f"✓ exists: {out.name}")
        continue
    print(f"↓ {pmcid}: {title}")
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        out.write_bytes(r.content)
        print(f"  saved: {out}")
    except Exception as e:
        print(f"  ⚠ Failed to download {pmcid}: {e}")
        print(f"    URL: {url}")
        # Create a placeholder file to indicate the download attempt
        out.write_text(f"Placeholder for {title}\nURL: {url}\nError: {e}")
        print(f"  created placeholder: {out}")
print("Done.")
