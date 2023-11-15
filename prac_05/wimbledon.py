"""
CP1404/CP5632 Practical 5 - Do-from-scratch exercise 3
Wimbledon records

Estimate: forgot to do this!
Actual:
"""

FILENAME = "wimbledon.csv"
WINNER_INDEX = 2
COUNTRY_INDEX = 1


def main():
    """Process and display champion win-counts and winning countries from championship records."""
    records = load_records()
    winner_to_count, countries = process_records(records)
    display_results(winner_to_count, countries)


def load_records():
    """Load records from csv."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = []
        for line in in_file:
            records.append(line.strip().split(','))
    return records


def process_records(records):
    """Count wins per champion and list winning countries."""
    countries = set()
    winner_to_count = {}
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            winner_to_count[record[WINNER_INDEX]] += 1
        except KeyError:
            winner_to_count[record[WINNER_INDEX]] = 1
    return winner_to_count, countries


def display_results(winner_to_count, countries):
    """Display number of wins per champion and sorted set of winning countries."""
    print("Wimbledon Champions:")
    for winner, count in winner_to_count.items():
        print(winner, count)

    print(
        f"\nThese {len(countries)} countries have won Wimbledon:\n{', '.join(sorted(countries))}")


main()
