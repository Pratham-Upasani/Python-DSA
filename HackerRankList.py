print("<----------------------------------------->")
print("List commands:")
print("1. Insert element e at index i, then type: insert i e")
print("2. Print the list, then type: print")
print("3. Remove an element e, then type: remove e")
print("4. Append an element e, then type: append e")
print("5. Sort the list in ascending, then type: sort")
print("6. Sort the list in descending, then type: reverse")
print("7. Pop the last element from the list, then type: pop")

N = int(input("\nEnter the number of commands you want to run: "))
print()
arr=[]

for x in range(N):
    prompt = input("Enter a command: ").split()

    if prompt[0]=="insert":
        index=int(prompt[1])
        element=int(prompt[2])
        arr.insert(index,element)

    elif prompt[0]=="print":
        print(arr)

    elif prompt[0]=="remove":
        element=int(prompt[1])
        arr.remove(element)

    elif prompt[0]=="append":
        element=int(prompt[1])
        arr.append(element)

    elif prompt[0]=="sort":
        arr.sort()

    elif prompt[0]=="reverse":
        arr.reverse()

    elif prompt[0]=="pop":
        arr.pop()
