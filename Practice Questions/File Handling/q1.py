#1. WAP to input a line of text, store in a file and then read from the file to display its content.
text=input("Enter a Line of text= ")
with open ("a.txt","w") as fw:
    fw.write(text)
with open("a.txt","r") as fr:
    print(fr.readline())