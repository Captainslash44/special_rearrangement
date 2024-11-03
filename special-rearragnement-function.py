"""
This code puts even numbers at the start and odd numbers at the end,
while preserving their original ordering.
"""


def Special_rearrangement(array):
    
    odd_numbers = []
    even_numbers = []

    # I made 2 arrays, one for odd numbers and the other for even ones,
    # then I added the 2 arrays in 1.
    for i in array:

        if i % 2 == 0:
            even_numbers.append(i)

        else:
            odd_numbers.append(i)

    answer = even_numbers + odd_numbers

    return answer


#I've used this tedious method to enter the array
#yet it ensures that all values are valid.
numbers = []

while True:
    n = input("Please enter a number to add to list, or press 'N' to continue: ")

    if n.upper() == "N": # Exit option for loop.
        break

    elif n.isdigit():
        numbers.append(int(n))

    else:
        print("Please enter a valid value.")

print(f"Original array: {numbers}")
print(Special_rearrangement(numbers))