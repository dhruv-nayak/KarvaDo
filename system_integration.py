def transfer_data_to_system(data, system_file):
    with open(system_file, 'w') as f:
        for item in data:
            f.write(item + '\n')

if __name__ == "__main__":
    data_list = ["Data 1", "Data 2", "Data 3"]
    system_file_path = "system_data.txt"
    transfer_data_to_system(data_list, system_file_path)
    print("Data transferred to system_data.txt")