# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
for i in range(a):
    string1 = input()
    for j in range(len(string1)):
        if j % 2 == 0 :
            print(string1[j],end="")
    print(" ",end="")
    for j in range(len(string1)):
        if j % 2 != 0 :
            print(string1[j],end="")
    print()
