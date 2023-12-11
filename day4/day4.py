"""
1. Parses the data into a dictionary
2. Evaluates winning numbers against sample numbers. Appends dict with winners
3. Calculates the score for each card
4. Sums the scores from each card
"""


def parse_cards(data):
    cards = {}
    for card in data:
        card_num, numbers = card.split(":")
        card_num = int(card_num.split(" ")[-1])
        winning, sample = numbers.split("|")
        winning = [int(num) for num in winning.split()]
        sample = [int(num) for num in sample.split()]
        cards[card_num] = {"winning": winning, "sample": sample}
    return cards


def evaluate_cards(cards):
    for card_num, card in cards.items():
        winning = card["winning"]
        sample = card["sample"]
        wins = []
        for num in sample:
            if num in winning:
                wins.append(num)
        cards[card_num]["wins"] = wins
    return cards


def calculate_score(card):
    # x is how many winning numbers in a card
    # score = 2^(x-1)
    x = len(card["wins"])
    return 2 ** (x - 1)


def calculate_total_score(cards):
    total = 0
    for card in cards.values():
        total += calculate_score(card)
    return total


with open("input.txt", encoding="utf-8") as f:
    data = f.readlines()

cards = parse_cards(data)
cards = evaluate_cards(cards)
total = calculate_total_score(cards)
print(f"The total score is {total}")
