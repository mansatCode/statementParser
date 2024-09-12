import csv
from collections import defaultdict
from pprint import pprint

d = defaultdict(int)

with open("exampleCSV.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        description = row["Description"]
        amount = float(row["Amount"])
        if amount < 0:
            continue
        elif "JPMC" in description:
            d["JPMC"] += amount
        elif "TESCO" in description:
            d["TESCO"] += amount
        elif "LIDL" in description:
            d["LIDL"] += amount
        elif any(word in description for word in ["KOKO", "TICKETSWAP", "RESIDENT ADVISOR"]):
            d["EVENTS"] += amount
        elif "REEBOK SPORTS CLUB" in description:
            d["THIRD SPACE SHAKES"] += amount
        elif any(word in description for word in ["UBER", "LIME", "TFL TRAVEL", "TRAINLINE"]):
            d["TRANSPORT"] += amount
        else:
            d[description] += amount
pprint(d)

