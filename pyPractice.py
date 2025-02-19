lists=[1,2,3,4,5,6,7,8,9,10] #deault list
def sumlist(list):  #for question number 1
    sum=0
    for i in range(len(lists)):
        sum+=lists[i]
    return sum
print(sumlist(list))

numbers=[int(i) for i in range(1,21)]
def printEven(numbers):   #for question number 2
    result=[]
    for num in numbers:
        if num%2==0:
            result.append(num)
    return result
print(printEven(numbers))

nums=[10,22,325,586,30,0,-53,100,643,6979]
def printLargest(nums):
    result=0
    for num in nums:
        if num>result:
            result=num
    return result
print(printLargest(nums))