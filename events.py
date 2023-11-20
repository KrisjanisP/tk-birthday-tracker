import csv

def save_birthday(name: str, date: str):
    """
    Appends row to events.csv.

    Name: first name + surname

    Date: YYYY-MM-DD
    """
    with open('events.csv', 'a', encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,date,"birthday"])


def load_birthdays():
    res = []
    with open('events.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            res.append(row)
    return res

