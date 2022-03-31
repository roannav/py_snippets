lst = [ 3, 5, 7, 1]
print(f"Original list: {lst}")

print("\n#######################  lst.reverse()  ##############################\n")

print("\nNOTE: lst.reverse() actually modifies lst.")
rev_list = lst.reverse()
print(f"lst.reverse() returns None... {rev_list}")
print(f"reverse of the list is {lst}")

lst.reverse()  # this actually modifies lst
print(f"reversing again, returns the list to its original state: {lst}")

print("\n#######################  slicing  ####################################\n")

print("\nNOTE: If you don't want modify the original list,")
print(f"then use slicing...  lst[::-1]")

print(f"reverse of the list  == lst[::-1] ==  {lst[::-1]}")
print(f"lst is unchanged: {lst}")

print("\nSlicing does make a copy, so any change to the original list,")
print("is NOT reflected in the reversed list.")
rev_list = lst[::-1]
print("\nSetting the first element of the original lst to 2.")
lst[0] = 2
print(f"reverse of the list  == lst[::-1] ==  {rev_list}")
print("lst[::-1] returns a COPY of the original list in reverse order,")
print("so it's not affected by setting lst[0] = 2")

print(f"\nlst is unchanged by the slice: {lst}")


print("\n#######################  reversed(lst)  ##############################\n")

print("\nAnother way that doesn't modify the original list is reversed()")
print("reversed() returns an iterator, which has the items in reverse order.")
itera = reversed(lst)
print(itera)
print(list(itera))
print("\nreversed() does not make a copy, so any change to the original list,")
print("will also be reflected in the reversed iterator.")
itera = reversed(lst)

print("\nSetting the first element of the original lst to 9.")
print("So in the reversed list, the last element is 9.")
lst[0] = 9
print(list(itera))

print("\nreversed() can be passed a list, string, or range, but not a plain iterator.")
print("Also you can NOT reverse a set, because how would you reverse something that")
print("is unordered.")
