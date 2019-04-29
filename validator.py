def reverse(num: str):
    num = "4712839550684070"[::-1]
    print(num)


def checking_validation(card_num: str):
    card_num = len == 16
    summary = 0
    digits_in_num = len(card_num)
    change_num = card_num[1, 3, 5, 7, 9, 11, 13, 15]
    print(card_num)
    for count in range(0, digits_in_num):
        digit = int(card_num[count])

        if change_num:
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        summary = summary + digit
    return (summary % 10) == 0
    print(card_num)

