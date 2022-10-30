#############################################
##### Hash Generator (String or Random) #####
#############################################

import hashlib, colorama
from random_word import RandomWords
from colorama import Fore

rValue = RandomWords().get_random_word()

hashValue = input('Enter String to Hash (leave blank for random) > ')

if hashValue == '':
    hashmd5 = hashlib.md5()
    hashmd5.update(rValue.encode())
    print('\nMD5 Hash: ' + Fore.YELLOW + hashmd5.hexdigest() + Fore.RESET)

    hashsha1 = hashlib.sha1();
    hashsha1.update(rValue.encode())
    print('SHA1 Hash: ' + Fore.YELLOW + hashsha1.hexdigest() + Fore.RESET)

    hashsha224 = hashlib.sha224()
    hashsha224.update(rValue.encode())
    print('SHA224 Hash: ' + Fore.YELLOW + hashsha224.hexdigest() + Fore.RESET)

    hashsha256 = hashlib.sha256()
    hashsha256.update(rValue.encode())
    print('SHA256 Hash: ' + Fore.YELLOW + hashsha256.hexdigest() + Fore.RESET)

    hashsha384 = hashlib.sha384()
    hashsha384.update(rValue.encode())
    print('SHA384 Hash: ' + Fore.YELLOW + hashsha384.hexdigest() + Fore.RESET)

    hashsha512 = hashlib.sha512()
    hashsha512.update(rValue.encode())
    print('SHA512 Hash: ' + Fore.YELLOW + hashsha512.hexdigest() + Fore.RESET)
       
else:
    hashmd5 = hashlib.md5()
    hashmd5.update(hashValue.encode())
    print('\nMD5 Hash: ' + Fore.YELLOW + hashmd5.hexdigest() + Fore.RESET)

    hashsha1 = hashlib.sha1();
    hashsha1.update(hashValue.encode())
    print('SHA1 Hash: ' + Fore.YELLOW + hashsha1.hexdigest() + Fore.RESET)

    hashsha224 = hashlib.sha224()
    hashsha224.update(hashValue.encode())
    print('SHA224 Hash: ' + Fore.YELLOW + hashsha224.hexdigest() + Fore.RESET)

    hashsha256 = hashlib.sha256()
    hashsha256.update(hashValue.encode())
    print('SHA256 Hash: ' + Fore.YELLOW + hashsha256.hexdigest() + Fore.RESET)

    hashsha384 = hashlib.sha384()
    hashsha384.update(hashValue.encode())
    print('SHA384 Hash: ' + Fore.YELLOW + hashsha384.hexdigest() + Fore.RESET)

    hashsha512 = hashlib.sha512()
    hashsha512.update(hashValue.encode())
    print('SHA512 Hash: ' + Fore.YELLOW + hashsha512.hexdigest() + Fore.RESET)
