import csv


def validate(num: str):
    if len(num) == 16:
        list_form = list(num)
        list_form.pop(15)
        print(list_form)
        reversed_form = reverse(list_form)

        for index in range(len(reversed_form)):
            reversed_form[index] = int(reversed_form[index])

            if index in reversed_form:
                index = [0, 2, 4, 6, 8, 10, 12, 14]
        print(reversed_form)
    return False


def reverse(num: list):
    return num[::-1]


print(validate("4556737586899855"))

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         for row in reader:
#             old_number = row[0]  # string
#             if validate(old_number):
#                 writer.writerow(row)
#         print("OK")