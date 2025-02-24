
#? the result of the task #

list1 = [100, 200, 300, 'A', 400, 500]

for item in list1:
    if not isinstance(item, int):
        print("Not all items are integers")
        break  
else:
    print("All items are integers") 
