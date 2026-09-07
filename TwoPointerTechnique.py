#Two pointer Technique
#It is used when we want to scan from both ends of a list towards the middle
#Or when we want to start scanning from both ends simultaneously

def palindrome_check(s):
    left=0  #Index positions(left=start of list, right= last element of list)
    right=len(s)-1

    while(left<right):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s=input("Enter a string to check if its palindrome or not: ")
print(palindrome_check(s))
