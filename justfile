md DAY:
  uv run utils/make_day.py {{DAY}}
  uv run aocd 2025 {{DAY}} > d{{DAY}}/r.in
  uv run aocd 2025 {{DAY}} --example | sed -n '/Example data/,/^---/p' | sed '1d;$d' > d{{DAY}}/t.in
