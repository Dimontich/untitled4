import random

print("Правила")

card_a = ["1a", "2a", "3a", "4a", "5a", "6a"]
card_b = ["1b", "2b", "3b", "4b", "5b", "6b"]
card_c = ["1c", "2c", "3c", "4c", "5c", "6c"]
card_d = ["1d", "2d", "3d", "4d", "5d", "6d"]

player_card = []
Alica_card = []


# while len(Alica_card) == 0 or len(player_card) == 0:
def first_step():
    # карты игрока
    i = 0
    while i < 3:
        step = random.randint(0, 3)
        if step == 0:
            a_p = random.choice(card_a)
            player_card.append(a_p)
            card_a.remove(a_p)
        if step == 1:
            b_p = random.choice(card_b)
            player_card.append(b_p)
            card_b.remove(b_p)
        if step == 2:
            c_p = random.choice(card_c)
            player_card.append(c_p)
            card_c.remove(c_p)
        if step == 3:
            d_p = random.choice(card_d)
            player_card.append(d_p)
            card_d.remove(d_p)
        i += 1

    # Карты алисы
    j = 0
    while j < 3:
        step_a = random.randint(0, 3)
        if step_a == 0:
            a_a = random.choice(card_a)
            Alica_card.append(a_a)
            card_a.remove(a_a)
        if step_a == 1:
            b_a = random.choice(card_b)
            Alica_card.append(b_a)
            card_b.remove(b_a)
        if step_a == 2:
            c_a = random.choice(card_c)
            Alica_card.append(c_a)
            card_c.remove(c_a)
        if step_a == 3:
            d_a = random.choice(card_d)
            Alica_card.append(d_a)
            card_d.remove(d_a)
        j += 1


first_step()


def second_step():
    # карты игрока
    i = 0
    while i < 1:
        step = random.randint(0, 3)
        if step == 0:
            a_p = random.choice(card_a)
            player_card.append(a_p)
            card_a.remove(a_p)
        if step == 1:
            b_p = random.choice(card_b)
            player_card.append(b_p)
            card_b.remove(b_p)
        if step == 2:
            c_p = random.choice(card_c)
            player_card.append(c_p)
            card_c.remove(c_p)
        if step == 3:
            d_p = random.choice(card_d)
            player_card.append(d_p)
            card_d.remove(d_p)
        i += 1

    # Карты алисы
    j = 0
    while j < 1:
        step_a = random.randint(0, 3)
        if step_a == 0:
            a_a = random.choice(card_a)
            Alica_card.append(a_a)
            card_a.remove(a_a)
        if step_a == 1:
            b_a = random.choice(card_b)
            Alica_card.append(b_a)
            card_b.remove(b_a)
        if step_a == 2:
            c_a = random.choice(card_c)
            Alica_card.append(c_a)
            card_c.remove(c_a)
        if step_a == 3:
            d_a = random.choice(card_d)
            Alica_card.append(d_a)
            card_d.remove(d_a)
        j += 1


def second_step_Alica():
    j = 0
    while j < 1:
        step_a = random.randint(0, 3)
        if step_a == 0:
            a_a = random.choice(card_a)
            Alica_card.append(a_a)
            card_a.remove(a_a)
        if step_a == 1:
            b_a = random.choice(card_b)
            Alica_card.append(b_a)
            card_b.remove(b_a)
        if step_a == 2:
            c_a = random.choice(card_c)
            Alica_card.append(c_a)
            card_c.remove(c_a)
        if step_a == 3:
            d_a = random.choice(card_d)
            Alica_card.append(d_a)
            card_d.remove(d_a)
        j += 1


print(player_card)

print('')

print(Alica_card)
print('')


def randon_step():
    move_A = random.choice(Alica_card)
    Alica_card.remove(move_A)
    print(move_A)


# Отбиваеться игрок
def stepic_Alica(move_A):
    print("Мой ход - ", move_A)
    list_num = []
    for p in move_A:  # перевод в стоку
        try:
            num = str(p)
            list_num.append(num)
        except ValueError:
            continue
    # print(list_num)

    list_num1 = []
    for i in move_A:  # отделение числа
        try:
            num = int(i)
            list_num1.append(num)
        except ValueError:
            continue
    # print(list_num1)

    print("Ваш ход  ")
    print("Можете побить Да/Нет ")
    ans = input().lower()

    if ans == "да":
        print("Назовите карту")
        card = input()
        card = str(card)
        card1 = str(card)
        if card in player_card:
            print("Проверяю ваш ход")
            import re
            card1 = re.sub(r"\d+", "", card1, flags=re.UNICODE)
            print(card1)  # буква
            replaced = re.sub('[\D]', '', card)
            print(replaced)
            for t in replaced:  # отделение числа
                try:
                    n = int(t)
                except ValueError:
                    continue

            if card1 == list_num[1] and n > num:
                print("Отбой!")
                player_card.remove(card)
                second_step()
                print(Alica_card)
                print(player_card)
                # вызов функции отбивания Алисы


            else:
                print("Не обманывайте")
                player_card.append(move_A)
                print(player_card)
                second_step_Alica()
                print(Alica_card)
                return randon_step()
                return stepic_Alica()

        else:
            print("Не врите")
            player_card.append(move_A)
            print(player_card)
            second_step_Alica()
            print(Alica_card)
            return randon_step()
            return stepic_Alica()


    elif ans == 'нет':
        print("Берите!")
        player_card.append(move_A)
        print(player_card)
        second_step_Alica()
        print(Alica_card)
        return randon_step()
        return stepic_Alica()

    else:
        print("Я вас не поняла")
        return stepic_Alica()


stepic_Alica()
