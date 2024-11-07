import rsa_classes as rsa


message = input() 
e, n = map(int, input().split())

alg = rsa.rsa_encryptor(message, e, n)
alg.encrypt(print_message=True)
