# Input list elements from the user
a = list(input("Nhập các phần tử: "))
print("Initial list:", a)

# Add an element to the list
add = input("Add: ")
a.append(add)
print("List after addition:", a)

# Delete an element from the list
delete = input("Delete: ")
if delete in a:
    a.remove(delete)
else:
    print(f"Element '{delete}' not found in the list.")
print("List after deletion:", a)

# Replace an element in the list
replace_what = input("Replace which element: ")
replace_with = input("Replace with: ")

if replace_what in a:
    index = a.index(replace_what)
    a[index] = replace_with
    print(f"List after replacing '{replace_what}' with '{replace_with}':", a)
else:
    print(f"Element '{replace_what}' not found in the list.")

