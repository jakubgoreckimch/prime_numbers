# this program is able to find every prime number in your range

last_number = input("type search range for prime numbers: ")

all_numbers = list(range(1, int(last_number)))
# print(all_numbers)
prime_numbers = []

for i in all_numbers:
    if i == 2:
        prime_numbers.append(i)
    else:
        numbers = list(range(2, i))
        for j in numbers:
            if any([i % j == 0 for j in numbers]):
                break
            else:
                prime_numbers.append(i)
                break

print(prime_numbers)

