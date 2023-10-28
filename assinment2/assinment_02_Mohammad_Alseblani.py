def count_digits_recursive(number):
    if number == 0:
        return 0
    else:
        return 1 + count_digits_recursive(number // 10)

def find_max_recursive(numbers):
    if not numbers:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        sub_max = find_max_recursive(numbers[1:])
        return numbers[0] if numbers[0] > sub_max else sub_max

def count_tags_recursive(input_string, tag):
    if tag in input_string:
        return 1 + count_tags_recursive(input_string.split(tag, 1)[1], tag)
    else:
        return 0

def count_normalized_columns_recursive(matrix):
    if not matrix:
        return 0
    if not matrix[0]:
        return count_normalized_columns_recursive(matrix[1:])
    else:
        column = [row[0] for row in matrix]
        if all(column[0] == element for element in column):
            return 1 + count_normalized_columns_recursive([row[1:] for row in matrix])
        else:
            return count_normalized_columns_recursive([row[1:] for row in matrix])

def display_menu():
    print("1. Count Digits")
    print("2. Find Max")
    print("3.1. Count Tags")
    print("3.2. Count Normalized Columns")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter a choice: ")

        if choice == '1':
            number = int(input("Enter an integer: "))
            digit_count = count_digits_recursive(abs(number))
            print("Number of digits:", digit_count)
        elif choice == '2':
            input_numbers = input("Enter a list of integers (comma-separated): ")
            numbers = [int(num) for num in input_numbers.split(",")]
            max_value = find_max_recursive(numbers)
            print("Maximum value:", max_value)
        elif choice == '3.1':
            input_string = input("Enter a string: ")
            tag = input("Enter the tag to count: ")
            tag_count = count_tags_recursive(input_string, tag)
            print("Tag count:", tag_count)
        elif choice == '3.2':
            input_matrix = input("Enter a list of lists (comma-separated rows, space-separated columns): ")
            rows = [row.split(",") for row in input_matrix.split()]
            matrix = [[int(element) for element in row] for row in rows]
            normalized_column_count = count_normalized_columns_recursive(matrix)
            print("Number of normalized columns:", normalized_column_count)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()