with open('To_Do_List.txt', 'w') as f:
  f.write("")
  
print("Press 1 to view list or Press 2 to add to the list?")
response=input("Enter 1 or 2; ")

if response == 1:
    with open('To_Do_List.txt', 'r') as f:
      print(f.read())
      f.close()
else:
  if response == 2:
    item = input("What would you like to add to your list?")
