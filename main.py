import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Kiek norėtumete papildyti sąskaitą?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Pildoma suma turi buti didesnė, nei 0")
        else:
            print("Prašome įrašyti skaičių, jeigu norite papildyti sąskaitą")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Ant keliu linijų norėtumete atlikti statymą (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Irašykite validu linijų skaičių")
        else:
            print("Prašome įrašyti skaičių, jeigu norite atlikti statymą")

    return lines

def get_bets():
    while True:
        amount = input("Kokia suma norėtumete atlikti statymą ant vienos linijos?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Suma turėtų būti tarp {MIN_BET} - {MAX_BET}.")
        else:
            print("Prašome įrašyti skaičių, jeigu norite atlikti statymą")

    return amount

def spin(amount):
    lines = get_number_of_lines()
    while True:
        bet = get_bets()
        total_bet = bet * lines

        if total_bet > amount:
            print("Neturite pakankankamai lėšų. Bandykite vėliau.")
        else:
            break

    print(f"Išleidžiate po {bet} ant {lines} linjų(-os). Is viso jus statote {total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winning, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"Jus laimėjote {winning}")
    print(f"Jus laimėjote ant", *winning_lines, "pozicijos")
    return winning - total_bet

def main():
    amount = deposit()
    while True:
        print(f"Dabartinis balansas yra {amount} Eur.")
        answer = input("Paspauskite Enter, kad pradėti (q, kad baigti žaidimą)")
        if answer == "q":
            break
        amount += spin(amount)

    print(f"Dabartinis balansas: {amount}")

main()
