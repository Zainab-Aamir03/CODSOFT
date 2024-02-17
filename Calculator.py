def addition(*numbers):
    return sum(numbers)

def subtraction(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiplication(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def division(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            print("Error: Division by zero is not possible.")
            return None
    return result

print("Calculator Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicatio")
print("4. Division")

while True:
    choice = input("Enter operation to perform (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num_list = [float(input(f"Enter number {i + 1}: ")) for i in range(int(input("Enter the Total Numbers You Want To Perform " + choice +" Operation on: ")))]
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Result:", addition(*num_list))
        elif choice == '2':
            print("Result:", subtraction(*num_list))
        elif choice == '3':
            print("Result:", multiplication(*num_list))
        elif choice == '4':
            result = division(*num_list)
            if result is not None:
                print("Result:", result)

        another_calculation = input("Do you want to Continue? (y/n): ")
        if another_calculation.lower() != "y":
            break
    else:
        print("Invalid Input")
