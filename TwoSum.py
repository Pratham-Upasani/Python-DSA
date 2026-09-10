#Two sum using two pointer technique
arr=[1,3,5,6,9,18,19,21]
target=25

def TwoSum(arr,target):
    i=0
    j=len(arr)-1
    while i<j:
        if (arr[i]+arr[j])==target:
            return [arr[i], arr[j]]
        elif (arr[i]+arr[j])>target:
            j-=1
        else:
            i+=1
    return None

pairs=TwoSum(arr,target)
print(pairs)
