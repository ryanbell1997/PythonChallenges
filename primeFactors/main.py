def get_prime_factors(input):
    input = int(input)
    primeFactors = []
    divisor = 2
    while(divisor <= input):
        if(input % divisor) == 0:
            primeFactors.append(divisor)
            input = input/divisor
        else:
            divisor += 1
    return primeFactors  



def main():
    print("Enter a number and I will provide you the prime factors of that number")
    userInput = input()
    primeFactors = get_prime_factors(userInput)
    print(primeFactors)
main()