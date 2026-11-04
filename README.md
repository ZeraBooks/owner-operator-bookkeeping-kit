# Owner-operator bookkeeping kit

An owner-operator should keep books every week: one business bank account,
every settlement booked at its gross amount with each deduction as its own
expense, fuel receipts kept for IFTA, and the bank account reconciled
to its statement each month. From those books you can work out cost per mile,
the number that tells you which loads to take.

This kit is the small set of files a one-truck owner-operator needs to do that
from the cab.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | Ten starter accounts, plus five to add when you need them (truck loan, owner draws, business card, truck asset, 2290 savings). Start with ten, not sixty. |
| `weekly-routine.md` | The five weekly steps and the monthly ones, as tick boxes. |
| `weekly-log.csv` | One row per week to mark each step done and note gross, deductions and net. The first row is a filled example. |
| `cost-per-mile.csv` | One month of miles, revenue and costs for a fictional one-truck owner-operator, Ridgeway Transport. |
| `cost_per_mile.py` | Reads that file and prints revenue, cost and what is left per mile. Python 3, standard library only. |
| `cost-per-mile-sheet.csv` | The same month with spreadsheet formulas, for people who would rather open it in Excel or Google Sheets. |
| `records-to-keep.md` | Which records to keep, how often and why, with a folder layout. |

## How to use it

1. Open a business checking account and use one card for the truck. Import
   `chart-of-accounts.csv` into your bookkeeping software or a spreadsheet.
2. Every week, work through `weekly-routine.md` and mark the row in
   `weekly-log.csv`.
3. At month end, put your ELD miles and the month's totals into
   `cost-per-mile.csv` and run:

   ```
   python3 cost_per_mile.py cost-per-mile.csv
   ```

   Or open `cost-per-mile-sheet.csv` and type over column B.

## Worked example: cost per mile

Ridgeway Transport is a fictional one-truck owner-operator. In September 2026
its ELD showed 9,800 miles and its settlements paid 22,050.00 gross, which is
2.25 a mile.

| Cost from the books | September | Per mile |
|---|---|---|
| Fuel | 6,370.00 | 0.650 |
| Insurance | 1,480.00 | 0.151 |
| Maintenance and tires | 1,150.00 | 0.117 |
| Truck loan interest | 610.00 | 0.062 |
| Permits, plates and Form 2290 set-aside | 420.00 | 0.043 |
| ELD and phone | 95.00 | 0.010 |
| Total cost | 10,125.00 | 1.033 |

At 2.25 a mile coming in and 1.03 going out, Ridgeway keeps about 1.22 a mile,
or 11,925.00 for the month, before depreciation, owner pay and income tax. Only
the interest part of the truck payment is a cost; the principal pays down the
loan. A rate below your cost per mile loses money however many miles you run.

All figures are fictional.

## FAQ

### Can an owner-operator keep books in a spreadsheet?

Yes, if you book settlements gross and reconcile to the bank each month. Most
spreadsheets fail on the second part: nothing checks that the rows add up to
the statement balance.

### Do I record per diem in my books?

No. Per diem is a tax calculation from your days away from home. The books
record what you actually spent; your accountant applies the rate.

### Is bookkeeping different if I run under my own authority?

Yes. Leased-on drivers get one settlement from the carrier with deductions
taken out. With your own authority you invoice brokers or shippers, chase
payments or factor invoices, and pay insurance and permits yourself, so you
also track receivables and factoring fees. A fuller chart for that is in
[chart-of-accounts-templates/trucking](https://github.com/ZeraBooks/chart-of-accounts-templates/tree/main/trucking).

## Learn more

[Owner-operator bookkeeping](https://www.zerabooks.com/owner-operator-bookkeeping)
on zerabooks.com, and the guide to
[bookkeeping for trucking](https://www.zerabooks.com/bookkeeping-for-trucking).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
