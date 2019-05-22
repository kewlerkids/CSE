import csv


# index = ['region', 'country', 'item type', 'sales channel', 'order priority', 'order date', 'order id', 'ship date',
#          'unit sold', 'unit price', 'unit cost', 'total revenue', 'total cost', 'total profit']

item_type_list = {}
with open("SalesRecords.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            if row[0] == 'Region':
                continue
            thing = row[0]  # string
            item = row[2]
            profit = row[13]
            if item in item_type_list:
                item_type_list[item] += float(profit)
            else:
                item_type_list[item] = float(profit)
        highest_profit = max(item_type_list, key=item_type_list.get)
        print("The highest profit was: %s" % highest_profit, max(item_type_list.values()))
