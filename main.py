import random
from helpers import genera_stringa, logo

logo()

filename = input("Insert the filename here: ")
filename = f"{filename}.lst"
f = open(filename, "w", encoding="utf-8")
print("File opened successfully")

chars = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",

    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",

    "0","1","2","3","4","5","6","7","8","9",

    "!","@","#","$","%","^","&","*","(",")","-","_","=",
    "+","[","]","{","}",";",":",",",".","?","/","<",">",
    "|","\\"
]

leng = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

already = set()

n = input("Insert here the number of the passwords you want to generate: ")
n = int(n)

for i in range(n):
    stringa_random = genera_stringa(chars, length=random.choice(leng))

    if stringa_random in already:
        print("This password was already generated.")
    else:
        already.add(stringa_random)
        f.write(f"{stringa_random}\n")
        print(f"Password number {i} added to the wordlist.")

f.close()
