#!/usr/bin/env bash
# Rigenera l'inventario dal file Excel originale (che NON sta nel repo).
# Uso: bash script/run.sh /percorso/EKKECARS_Leads.xlsx /cartella/di/lavoro
# Richiede: python3, pandas, openpyxl, tabulate
set -euo pipefail
SRC="$1"; W="$2"; D="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$W"
python3 -I "$D/extract.py"  "$SRC" "$W/raw.pkl"
python3 -I "$D/classify.py" "$W/raw.pkl" "$W/cls.pkl"
python3 -I "$D/profile.py"  "$W/cls.pkl" "$W/final.pkl"
python3 -I "$D/inventory.py" "$W/final.pkl" > "$W/tabelle.md"
python3 -I "$D/export.py"   "$W/final.pkl" "$D/../dati/lead-anonimi.csv" "$W/Revisione-lead-per-Loris.xlsx"
echo "Fatto. Tabelle in $W/tabelle.md, file per Loris in $W (fuori dal repo)."
