import csv

def process_csv_and_generate_report(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        total = 0
        count = 0
        for row in reader:
            try:
                value = float(row[1])
                total += value
                count += 1
            except ValueError:
                print(f"Skipping row with invalid data: {row}")
        if count == 0:
            print("No valid data found.")
            return
        sum_data = total
        average_data = total / count
        print("CSV Data Report")
        print(f"Total: {sum_data}")
        print(f"Average: {average_data}")

if __name__ == "__main__":
    try:
        with open("data.csv", 'w') as csvfile:
            fieldnames = ['name', 'value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': 'item1', 'value': '10'})
            writer.writerow({'name': 'item2', 'value': '20'})
            writer.writerow({'name': 'item3', 'value': '30'})
        print("data.csv file created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    process_csv_and_generate_report("data.csv")