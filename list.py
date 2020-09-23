print("Press 1 to view list or Press 2 to add to the list?")
response=input("Enter 1 or 2; ")
if response == 1 then print(list)
if response == 2 then 
  with open('To_Do_List.txt', 'w') as f:
   f.write(input("What would you like to add to your list?"))
   
