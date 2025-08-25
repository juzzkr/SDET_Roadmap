numbers = [1, 2, 5, 8, 10]

even_numbers = [n for n in numbers if n % 2 == 0]
sum_even = sum(even_numbers)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", sum_even)
