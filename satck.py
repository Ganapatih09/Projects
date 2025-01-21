list=[]
print("Enter your choice.")
print("1. Insert")
print("2. Remove")
print("3. Display")
print("4. Exit")

while True:
  x=int(input("Enter your choice"))

  if x==1:
    if len(list) == 5:
        print("Stack is full.")
    else:
        ele=input("Enter the element")
        list.append(ele)

  elif x==2:
    if not list:
        print("Stack is empty")
    else:
        print("Deleted element is : ",list.pop())

  elif x==3:
    if not list:
        print("Stack is empty")
    else:
        print("Content of stack is : ",list[::-1])
  else:
        break
print("End")
