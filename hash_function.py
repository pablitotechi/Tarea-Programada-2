def calculate_hash(date, qtr, teams):
    key = hash(f"{date}-{qtr}-{teams}") % 750
    return key
