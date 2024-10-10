import csv

def calculate(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    return None

if __name__ == '__main__':
    fileName = input("CSV file name: ")
    calculate(fileName)