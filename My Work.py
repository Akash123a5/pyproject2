# My Project 2 

favourite_fooods = []

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favourite all foods")
    
    
    option = input("Choose an option: ")

    if option =="0":
        print("Thanks for using Favourite Foods Manager")
        break

    elif option == "1":
         food = input("Enter you favourite food name: ")
         favourite_fooods.append(food)
         print(f"{food} add Successfully")

    elif option == "2":
        food = input("Enter a food name which you want to remove: ")
        if food in favourite_fooods:
            favourite_fooods.remove(food)
            print(f"{food} remove Successfully")
        else:
            print(f"{food} food does not exists in List")

    elif option =="3":
        if favourite_fooods:
            print("Your favourite foods: ")
            for index,food in enumerate(favourite_fooods,start=1):
                print(f"{index}.{food}")    
        else:
            print("Food List is empty or didn't added yet! ")
    else:
        print("Invalid Choice!")


