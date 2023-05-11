### Q1

rows = int(input("Please enter number of rows: "))

if rows % 2 == 0:
    for i in range(rows // 2, 0, -1):
        print(' ' * (rows // 2 - i) + '*' * (2 * i - 1))
    for i in range(1, rows // 2 + 1):
        print(' ' * (rows // 2 - i) + '*' * (2 * i - 1))
else:
    for i in range(rows // 2, -1, -1):
        print(' ' * (rows // 2 - i) + '*' * (2 * i + 1))
    for i in range(1, rows // 2 + 1):
        print(' ' * (rows // 2 - i) + '*' * (2 * i + 1))


### Q2

numbers = []

while True:
    num = int(input("Please enter a number: "))
    if num == -1:
        break
    if num > 10:
        numbers.append(num)

print("The numbers are:")
for n in numbers:
    print(n)

### Q3

numbers = list(map(int, input("Please enter the numbers: ").split()))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) in numbers:
            print(f"{numbers[i] + numbers[j]}={numbers[i]}+{numbers[j]}")

### Q4

user_input = int(input("Please enter a number: "))

matrix = [[i * 10 + j + 1 for j in range(10)] for i in range(10)]
filtered_matrix = [[matrix[i][j] if matrix[i][j] % user_input == 0 else '' for j in range(10)] for i in range(10)]

for row in filtered_matrix:
    print(', '.join(map(str, row)))
