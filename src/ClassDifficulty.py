import csv
import pandas as pd
import statistics

classes = []
difficulty = []
user_class_difficulties = []
    
def class_difficulty():
    with open("Database.csv","r") as database:
        reader = csv.reader(database)

        see_index = []
        equivalent_index = []
    
        for row in reader:
            if row[0] == '' or row[1] == '' or row[0] == 'Class':
                continue
            else:    
                classes.append(row[0])
                difficulty.append(row[1])
            
    database.close()
    
    counter = 0
    for entry in difficulty:
        if "See" in entry:
            see_index.append(counter)
        counter = counter + 1
    
    index = 0
    for diff in see_index:
        equivalent = difficulty[diff][4:]
        index = 0
        for name in classes:
            if equivalent == name:
                equivalent_index.append(index)
            index = index + 1
    
    eq_counter = 0
    for indexes in equivalent_index:
        difficulty[see_index[eq_counter]] = difficulty[indexes]
        eq_counter = eq_counter + 1
    
    data = pd.DataFrame({
        'Classes': classes,
        'Difficulty': difficulty,
    })
    data.index = data.index + 1
    data.to_csv('Difficulties.csv',encoding='utf-8') 
    
def check_class(class_name):
    found = False
    class_index = 0
    for name in classes:
        if class_name == name:
            user_class_difficulties.append(float(difficulty[class_index]))
            return True
        else:
            found = False
        class_index = class_index + 1

    if not found:
        return False

def user_inputs():
    user_classes = []
    count = 7
    user_input = input("Enter a class\n")
    user_input = user_input.upper()
    while(not check_class(user_input)):
        if user_input == "-":
            break
        user_input = input("Class not found, try again\n")
        user_input = user_input.upper()

    user_classes.append(user_input)

    while user_input != "-" and count != 0:
        user_input = input("Enter a class or \"-\" when finished\n")
        user_input = user_input.upper()
        
        while(not check_class(user_input)):
            if user_input == "-":
                break
            user_input = input("Class not found, try again\n")
            user_input = user_input.upper()

        if user_input == "-":
            break
        user_classes.append(user_input)
        count = count - 1
    
    mean = statistics.mean(user_class_difficulties)
    print("Class Average Difficulty Level for", end = ' ')
    for user_input_classes in user_classes:
        print(user_input_classes, end = ' ')
    print("is:",round(mean,3))
    
def main():
    class_difficulty()
    user_inputs()

if __name__ == "__main__":
    main()