positive_sum=0
negative_sum=0
n = int(input("Enter the size of an array"))
list = [] #creates a empty list
# read elements of list
print(f"Enter {n} values")
for i in range(n):
  x=(int(input()))
  list.append(x)
 #check whether the list element is positive or negative
  if list[i] >= 0:
     positive_sum = positive_sum + x
  else:
      negative_sum = negative_sum + x
print("Sum of positive numbers = ",positive_sum)
print("Sum of negative numbers = ",negative_sum)