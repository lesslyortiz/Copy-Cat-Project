# --------------------------------------------------------
#        Name: Les Ortiz
# Course Info: CSC111 - Fall 2020
# Description: Submission for Assignment 2
#        Date: 9/22/2020
# --------------------------------------------------------
#asks for user
sent = str(input("Enter a sentence: "))

print("0. ", sent)#prints original input
print("1a. ", sent.upper())#capitalizes the entire string
print("1b. ", sent.lower())#makes the string lowercase
vowel = (sent.replace("I","II").replace("A","AA").replace("E","EE").replace("O","OO").replace("U","UU").replace("a","aa").replace("e", "ee").replace("i","ii").replace("o","oo").replace("u", "uu"))
#mess of code here for the vowels to repeat
print("2. ", vowel)
print("3. ", sent[:5] + "..." + sent[-5:])#replaces the middle with ...
print("4. ", sent.title())#capitalizes the first letter of each word
print("5. ", "".join(reversed(sent)))#reverses the string w/o spaces
