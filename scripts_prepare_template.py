import os
import glob
import csv
import pathlib
import re

text_dir = "projects/ai_tb_meta/data/text"
out_csv = "projects/ai_tb_meta/data/extracted/studies_template.csv"
os.makedirs(os.path.dirname(out_csv), exist_ok=True)

rows = []
for f in glob.glob(f"{text_dir}/*.txt"):
    base = pathlib.Path(f).stem
    # Guess study year/author patterns (very rough)
    text = open(f, encoding="utf-8", errors="ignore").read()
    m_year = re.search(r"(20\d{2}|19\d{2})", text)
    year = m_year.group(1) if m_year else ""
    rows.append([base, year, "", "", "", "", "", "", ""])

with open(out_csv, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["study_id", "year", "country", "setting", "n_total", "TP", "FP", "FN", "TN"])
    w.writerows(rows)

print(f"Template ready: {out_csv}")
print("Fill TP/FP/FN/TN (per index test vs reference). If counts unavailable, "
      "compute from sens/spec & denominators when possible.")
