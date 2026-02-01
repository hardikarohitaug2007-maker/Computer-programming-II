s = input("Enter a string: ")
length = len(s)
if length == 0:
    print("Empty string")
elif length % 2 == 0:
    print("First character: ",s[0])
    print("Last character: ",s[length - 1])
    print("Middle character: Not applicable(length is even)")
else:
    mid = length // 2
    print("First character: ",s[0])
    print("Last character: ",s[length - 1])
    print("Middle character: ",s[mid])