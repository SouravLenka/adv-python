#1. Write a function to reverse a string.

def reverse_string(s):
    return s[::-1]
string_to_reverse = input("Enter a string to reverse: ")
reversed_string = reverse_string(string_to_reverse)
print(f"Reversed string: {reversed_string}")

#2. Write a function to check if a string is a palindrome.
def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]   
string_to_check = input("Enter a string to check for palindrome: ")
if is_palindrome(string_to_check):
    print(f"{string_to_check} is a palindrome.")
else:    
    print(f"{string_to_check} is not a palindrome.")


#3. Write a recursive function to find factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial(number)}.")


#4. Write a function to count vowels in a string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
string_to_count = input("Enter a string to count vowels: ")
vowel_count = count_vowels(string_to_count)
print(f"Number of vowels in '{string_to_count}': {vowel_count}")


#5. Write a function to find the largest number in a list.

def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers = input("Enter a list of numbers separated by spaces: ")
number_list = list(map(float, numbers.split()))
largest_number = find_largest(number_list)
if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")


#6. Write a function to check if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number_to_check = int(input("Enter a number to check if it's prime: "))
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")


#7. Write a function to find the sum of digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
number_for_sum = int(input("Enter a number to find the sum of its digits: "))   
digit_sum = sum_of_digits(number_for_sum)
print(f"The sum of the digits of {number_for_sum} is: {digit_sum}")


#8. Write a function to generate first n Fibonacci numbers.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n_fib = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(n_fib)
print(f"The first {n_fib} Fibonacci numbers are: {fib_numbers}")


#9. Write a function to remove duplicates from a list while keeping order.

def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
numbers_with_duplicates = input("Enter a list of numbers separated by spaces (with duplicates): ")
number_list_with_duplicates = numbers_with_duplicates.split()
unique_numbers = remove_duplicates(number_list_with_duplicates)
print(f"List after removing duplicates: {unique_numbers}")


#10. Write a function to find length of a string without using len().

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
string_to_measure = input("Enter a string to find its length: ")
length_of_string = string_length(string_to_measure)
print(f"The length of the string '{string_to_measure}' is: {length_of_string}")
