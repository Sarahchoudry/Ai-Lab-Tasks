import random

def fizzbuzz(n: int):
    results = []
    
    # Generate n random numbers between 1 and n
    for _ in range(n):
        i = random.randint(1, n)
        if i % 3 == 0 and i % 5 == 0:
            results.append("fizzbuzz")
        elif i % 3 == 0:
            results.append("fizz")
        elif i % 5 == 0:
            results.append("buzz")
        else:
            results.append(str(i))

    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    fizzbuzz(15)
