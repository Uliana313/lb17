import json

def read_data(filename):
    series = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                series.extend(int(num) for num in line.split() if num.isdigit())
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    return series

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Унікальні значення збережено у файл {filename}")

if __name__ == "__main__":
    series = read_data("data.txt")
    unique_values = list(set(series))
    print("Одновимірний масив:", series)
    print("Унікальні значення:", unique_values)
    save_to_json(unique_values, "unique_values.json")
    