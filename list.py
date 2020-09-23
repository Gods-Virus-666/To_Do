print("Press 1 to view list or Press 2 to add to the list?")
response=input("Enter 1 or 2; ")
with open('To_Do_List.txt', 'r') as f:
  if response == 1: print(f.read())
  f.close()

if response == 2 then 
  with open('To_Do_List.txt', 'a') as f:
   f.write(input("What would you like to add to your list?"))
   print(f.read())
   f.close
    
