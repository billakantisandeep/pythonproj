#Python program to demostrate 
#Addition of elements in a List 
#Creating the list 

List = []
print("Initial blank list")
print(List)

#Adding of th elements
#in the list
List.append(1)
List.append(2)
List.append(4)
print("\n List after addition of three elements")

#Adding the elements to the list 
#using the iterator

for i in range(1, 4):
    List.append(i)
print("\n List after adding the elements using the appender")

#Adding the tuples to the list 
List.append((5,6))
print("\n List after adding the tuples")
print(List)

#Adding the list to the list
List2 = ["Sandeep", "sandy"]
List.append(List2)
print("\n After adding the list to the list ")
print(List)

#Adding the element to 
#the specific location of the list
#(using the insert method)
List.insert(3,12)
List2.insert(0, "udvi")
print("\n List after performing the insert")

#Addition of multiple elements 
# to the end of the list 
#(Using the extend menthod)
List.extend([8, 'Greeks', 'Always'])
print("\n Lists after adding the elements using the extend method")
print(List)