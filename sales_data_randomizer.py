import csv
import shutil
import random
import time

with open("sales_data.csv", 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)

# First backup and scan original file
shutil.copy2("sales_data.csv", "backup_sales_data.csv")

last_saved_day = None

while True:
    current_day = time.gmtime().tm_mday

    # We check if a backup has already been made for today
    if last_saved_day != current_day:
        print("Készítek biztonsági másolatot...")
        shutil.copy2("sales_data.csv", "backup_sales_data.csv")
        last_saved_day = current_day

    # Here you can mix the data and write it back to the original file
    header, rows = data[0], data[1:]
    random.shuffle(rows)

    with open("sales_data.csv", 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)

    print("Data shuffled.")

    time.sleep(10)