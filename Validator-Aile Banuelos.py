import csv


def validate(num: str):
    # print("")
    if len(num) == 16:
        list_form = list(num)
        last_num = list_form.pop(15)
        reversed_form = reverse(list_form)

        for index in range(len(reversed_form)):
            reversed_form[index] = int(reversed_form[index])

            if index % 2 == 0:
                reversed_form[index] *= 2

                if reversed_form[index] >= 9:
                    reversed_form[index] -= 9

        # print(reversed_form)
        # print(sum(reversed_form))
        total = sum(reversed_form) % 10
        # print(total)

        if total == int(last_num):
            return True

        else:
            return False


def reverse(num: list):
    return num[::-1]


# print(validate("4556737586899855"))

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]  # string
            if validate(old_number):
                writer.writerow(row)
        print("OK")
