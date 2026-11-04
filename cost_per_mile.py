"""Work out revenue per mile, cost per mile and what is left per mile.

Reads a CSV with columns line, kind, amount, where kind is miles, revenue or
cost (one miles row). Usage:
  python3 cost_per_mile.py cost-per-mile.csv
Python 3, standard library only.
"""
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

THREE = Decimal("0.001")


def per_mile(amount, miles):
    return (amount / miles).quantize(THREE, rounding=ROUND_HALF_UP)


def main(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    miles_rows = [r for r in rows if r["kind"] == "miles"]
    if len(miles_rows) != 1:
        print("Need exactly one row with kind = miles")
        return 2
    miles = Decimal(miles_rows[0]["amount"])
    revenue = sum(Decimal(r["amount"]) for r in rows if r["kind"] == "revenue")
    costs = [r for r in rows if r["kind"] == "cost"]
    total = sum(Decimal(r["amount"]) for r in costs)

    print(f"{'Line':<42}{'Amount':>12}{'Per mile':>10}")
    print(f"{'Revenue':<42}{revenue:>12,.2f}{per_mile(revenue, miles):>10}")
    for r in costs:
        amt = Decimal(r["amount"])
        print(f"{r['line']:<42}{amt:>12,.2f}{per_mile(amt, miles):>10}")
    print(f"{'Total cost':<42}{total:>12,.2f}{per_mile(total, miles):>10}")
    left = revenue - total
    print(f"{'Left before depreciation, owner pay and tax':<42}{left:>12,.2f}{per_mile(left, miles):>10}")
    print(f"\n{miles:,} miles. A rate below {per_mile(total, miles)} a mile loses money on these costs.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
