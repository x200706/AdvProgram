while True:
    line = input()
    if line == '0 0':
        break
    line = list(map(int, line.split()))

    all_card = []

    card_for_a = line[0]
    a_card = []
    a_temp = list(map(int, input().split()))
    for e in a_temp:
        a_card.append(e)
        all_card.append(e)
    a_card = set(a_card)

    card_for_b = line[1]
    b_card = []
    b_temp = list(map(int, input().split()))
    for e in b_temp:
        b_card.append(e)
        all_card.append(e)
    b_card = set(b_card)

    all_card = set(all_card)

    print(min(len(all_card)-len(a_card), len(all_card)-len(b_card)))