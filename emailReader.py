####################################
##### Reads .eml (email) files #####
####################################

from email import policy
from email.parser import BytesParser
import argparse

parser = argparse.ArgumentParser(description='Read Email Files')
parser.add_argument('-f', '--file', metavar='<filename.eml>', required=True)
args = parser.parse_args()

efile = args.file

with open(f'{efile}','r') as f:
    for line in f:
        if 'From' in line:
            print(line)
f.close()

with open(f'{efile}', 'r') as ft:
    for line in ft:
        if 'To' in line:
            print(line)

with open(f'{efile}', 'r') as fg:
    for line in fg:
        if 'Date' in line:
            print(line)
        if 'Subject' in line:
            print(line)

with open(f'{efile}', 'rb') as fp:
    msg = BytesParser(policy=policy.default).parse(fp)
    text = msg.get_body(preferencelist=('plain')).get_content()
    newText = ""
    flag = 0
    urlFlag = 0
    for i in range(len(text)):
        if(flag==1):
            flag = 0
            continue
        if(text[i]=="\\"):
            flag = 1
            continue
        if(text[i]=='<'):
            urlFlag = 1
            continue
        if(text[i]=='>'):
            urlFlag = 0
            continue
        if(urlFlag==0):
            newText = newText+text[i]
    print('Text: ' + newText)
fp.close()

