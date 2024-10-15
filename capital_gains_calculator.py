import csv 

def calculate(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)

        startSave = False

        # Keeps track of Capital gains/losses
        total = 0

        # Determines which columns to read for the value of the transation and whether it was a disposal or an acqusition
        val_col = None
        sign_col = None

        # sign_col string to value mapping
        sign_dict = {
            'Increase' : -1,
            'Decrease' : 1
        }

        for row in reader:
            try:
                if startSave:
                    # Assigning values
                    val = row[val_col]
                    sign = row[sign_col]

                    # Printing the values for user
                    print(sign + ' ' + val)

                    # Summing total
                    total += float(sign_dict[sign]) * float(val)
            except:
                # Exit case
                if startSave and row == None:
                    break

            # Determines when to start reading values
            if (not startSave) and (row[0] == 'Security identifier'):
                startSave = True
                
                # Assigning column values
                for i in range(len(row)):
                    if row[i] == 'Value':
                        val_col = i
                    if row[i] == 'Quantity change':
                        sign_col = i


    return total

if __name__ == '__main__':
    fileName = input("CSV file name: ")
    print(calculate(fileName))