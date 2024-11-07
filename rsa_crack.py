import rsa_classes as rsa


message = input() 
e, n = map(int, input().split())

alg = rsa.rsa_cracker(message, e, n)
alg.crack(print_message=True)