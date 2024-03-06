def count_numbers():
    positive_count = 0
    negative_count = 0
    zero_count = 0

    while True:
        try:
            num = float(input("Enter a number (enter 0 to stop): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if num == 0:
            break
        elif num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    print("\nCount of positive numbers:", positive_count)
    print("Count of negative numbers:", negative_count)
    print("Count of zeros:", zero_count)

if __name__ == "__main__":
    count_numbers()
