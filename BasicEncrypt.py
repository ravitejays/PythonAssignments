# basic code to encrypt a sentence or password

def encrypt(sentence):
    encryption = " "
    for i in sentence:
        if i in "Aa":
            encryption = encryption + "9"
        elif i in "Bb":
            encryption = encryption + "8"
        elif i in "Cc":
            encryption = encryption + "7"
        elif i in "Dd":
            encryption = encryption + "6"
        elif i in "Ee":
            encryption = encryption + "5"
        elif i in "Ff":
            encryption = encryption + "4"
        elif i in "Gg":
            encryption = encryption + "3"
        elif i in "Hh":
            encryption = encryption + "2"
        elif i in "Ii":
            encryption = encryption + "1"
        elif i in "Jj":
            encryption = encryption + "0"
        elif i in "Kk":
            encryption = encryption + "/"
        elif i in "Ll":
            encryption = encryption + "*"
        elif i in "Mm":
            encryption = encryption + "-"
        elif i in "Nn":
            encryption = encryption + "+"
        elif i in "Oo":
            encryption = encryption + "!"
        elif i in "Pp":
            encryption = encryption + "%"
        elif i in "Qq":
            encryption = encryption + "@"
        elif i in "Rr":
            encryption = encryption + ")"
        elif i in "Ss":
            encryption = encryption + "#"
        elif i in "Tt":
            encryption = encryption + "|"
        elif i in "Uu":
            encryption = encryption + "?"
        elif i in "Ww":
            encryption = encryption + "("
        elif i in "Xx":
            encryption = encryption + "-"
        elif i in "Yy":
            encryption = encryption + "%"
        elif i in "Zz":
            encryption = encryption + "&"
        elif i in "0":
            encryption = encryption + "I"
        elif i in "1":
            encryption = encryption + "v"
        elif i in "2":
            encryption = encryption + "S"
        elif i in "3":
            encryption = encryption + "^"
        elif i in "4":
            encryption = encryption + "A"
        elif i in "5":
            encryption = encryption + "*"
        elif i in "6":
            encryption = encryption + "R"
        elif i in "7":
            encryption = encryption + "~"
        elif i in "8":
            encryption = encryption + "["
        elif i in "9":
            encryption = encryption + "}"
        else:
            encryption = encryption + i
    return encryption

print(encrypt(input('Type in the password or sentence which you want to encrypt: ')))