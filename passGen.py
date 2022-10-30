###############################
##### Python Password Gen #####
###############################

import string, random, argparse

parser = argparse.ArgumentParser(description='Strong Password Generator')
parser.add_argument('-l', '--length', metavar='NUM', required=True, type=int, default=50, help='Password Length')
args = parser.parse_args()

howmany = args.length

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

random.shuffle(characters)

password = []
for i in range(howmany):
	password.append(random.choice(characters))

random.shuffle(password)

print("".join(password))
