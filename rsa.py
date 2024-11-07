from numpy import lcm
import sys


class rsa:
    def __init__(self, message, e, n):
        self.m = message
        if(e == 0):
            self.e = 23
        else:
            self.e = e
        if(n == 0):
            self.n = 77
        else:
            self.n = n
        self.findpq()
        self.calculate_d()

    def encrypt(self, print_message=True):
        # Encrypt the message using the public key
        if print_message:
            print(f"Message in ASCII code: {[ord(char) for char in self.m]}", file=sys.stderr)
            print("", file=sys.stderr)
        encrypted_message = [pow(ord(char), self.e, self.n) for char in self.m]


        if(print_message):
            print(f"Message encoded {encrypted_message}", file=sys.stderr)
            print("".join(chr(num) for num in encrypted_message))
        
        self.encrypted_message = encrypted_message

        return encrypted_message

    def crack(self):
        # Add cracking logic here
        return self

    def findpq(self):
        # Prime factorization of n
        factors = self.prime_factors(self.n)
        if len(factors) == 2:
            self.q, self.p = factors
            print(f"Prime number P: {self.p}\nPrime number q: {self.q}", file=sys.stderr)
            print(f"Public Key (e): {self.e}", file=sys.stderr)
        else:
            raise ValueError("n is not a product of two primes")
        return self

    def prime_factors(self, n):
        i = 2 # Smallest prime number
        factors = [] # Store them vals
        while i * i <= n: # While i squared is less than n
            if n % i: # If n is not divisible by i aka not a prime factor
                i += 1
            else: # If n is divisible by i aka prime factor
                n //= i # Divide n by i and store the result in n
                factors.append(i)
        if n > 1: # If n is greater than 1 then we actually have a prime factor I care about
            factors.append(n)
        return factors

    def lamdaN(self):

        lmd = lcm(self.p-1, self.q-1)
        print(f"LMD: {lmd}")
        return lmd
    
    def calculate_d(self):
        # Calculate d such that (e * d) % lambda_n == 1
        lambda_n = self.lamdaN()
        for d in range(1, n):
            if (self.e * d) % lambda_n == 1:
                self.d = d
                break
        print(f"Private Key: {self.d}", file=sys.stderr)
        print(f"n: {self.n}", file=sys.stderr)
        print(f"Phi of n: {2 * lambda_n}", file=sys.stderr)
        return self


    m = 0
    e = 0
    n = 0 
    p = 0 # Prime number calculated from n
    q = 0 # Prime number calculated from n
    d = 0 # Calculated value
    encrypted_message = []


message = input() 
e, n = map(int, input().split())

alg = rsa(message, e, n)
alg.encrypt(print_message=True)
print("\n")