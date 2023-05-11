
### Q1

def mult_even_digits(n):
    product = 1
    has_even_digit = False
    for digit in str(n):
        if int(digit) % 2 == 0:
            product *= int(digit)
            has_even_digit = True
    return product if has_even_digit else 1

print(mult_even_digits(222))
print(mult_even_digits(1357))
print(mult_even_digits(246))

### Q2

def fix_grades(grades):
    passing_grades = 0
    for i in range(len(grades)):
        if grades[i] <= 50:
            grades[i] = 0
        elif 51 <= grades[i] <= 60:
            grades[i] = 60
            passing_grades += 1
        elif grades[i] > 60:
            passing_grades += 1
    return passing_grades

grades = [49, 58, 62, 85, 55]
print(fix_grades(grades))
print(grades)

### Q3

def most_popular_digit(num):
    digit_counts = {digit: 0 for digit in range(10)}
    
    for digit in str(num):
        digit_counts[int(digit)] += 1

    max_value = max(digit_counts.values())
    max_key = max([key for key, value in digit_counts.items() if value == max_value])

    return max_key

print(most_popular_digit(172772))
print(most_popular_digit(123456789))


### Q4

import csv

def extract(column):
    with open('AppleStore.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        return [row[column] for row in reader]

def freq_table(data_list):
    freq_dict = {}
    for item in data_list:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

def freq_table_gen(column):
    data_list = extract(column)
    freq_dict = freq_table(data_list)
    most_common = max(freq_dict, key=freq_dict.get)
    return freq_dict, most_common

genres_column = 11
genres = extract(genres_column)
print(genres)

genres_freq_table = freq_table(genres)
print(genres_freq_table)

user_rating_column = 7
user_rating_freq_table, most_common = freq_table_gen(user_rating_column)
print(user_rating_freq_table)
print(most_common)
