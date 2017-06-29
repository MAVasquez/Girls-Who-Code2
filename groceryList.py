groceryList = []
add = True

while add == True:
    print("Do you want to add an item to your list? Yes or no?")
    answer = input()

    if answer == "yes":
        print("what item would you like to add to your shopping cart?")
        answer2 = input()
        groceryList.append(answer2)
    elif answer == "no":
        print("here is your grocery list.")

        for x in groceryList:
            print(x)
        add = False
