def even_odd():
    print("Welcome to the Coding Helper Agent!")
    print("This agent can divide your numbers into odd and even.")

    # User se input lena
    user_input = input("Write the numbers separated by commas (e.g. 1,2,3,4).")
    
    # String ko list mein convert karna
    try:
        numbers = [int(num.strip()) for num in user_input.split(',')]
    except ValueError:
        print("Enter only numbers. The program is crashing.")
        return

    even = []
    odd = []

    # Logic: even aur odd check karna
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    # Output dikhana
    print("Result:")
    print("Even numbers:", even)
    print("Odd numbers:", odd)

    # Explanation
    print("Explanation:")
    print("Each number was checked to see if it can be divided by 2 (num % 2 == 0).")
    print("If it was divisible, it went into the even list; otherwise, it went into the odd list.")

# Function ko call karna
even_odd()
