nums = [1, 2, 3, 4, 5]
for num in nums:
    print(f"Number: {num}")

#When range is used the loop will iterate from 0 to len(nums)-1
for i in range(len(nums)):
    print(f"Index: {i}")

#Using enumerate to get index and value
for index, value in enumerate(nums):
    print(f"Index: {index}, Value: {value}")

#for loop with condition
for num in nums:
    if num % 2 == 0:
        print(f"Even Number: {num}")
    else:
        print(f"Odd Number: {num}")

#Using list comprehension to get even numbers
evens = [x for x in nums if x % 2 == 0]
print("Even Numbers:", evens)

#Using generator expression to get even numbers
for x in (n for n in nums if n % 2 == 0):
    print(x)

#Using filter to get even numbers
for x in filter(lambda n: n % 2 == 0, nums):
    print(x)

#for-else construct - this is unique to Python
#Runs else only if the loop completes without break.
for x in nums:
    if x == 5:
        break
else:
    print("5 not found")



#Using while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1