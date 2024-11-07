#!/bin/bash
# This is a shell script that makes testing significantly easier. Proves that it works
python3 rsa_encrypt.py < tests/encryption_tests/test_encryption_1.input 2> log.txt > output.txt
echo 11 5183 >> output.txt
python3 rsa_crack.py < output.txt 2> crack_log.txt > crack_output.txt