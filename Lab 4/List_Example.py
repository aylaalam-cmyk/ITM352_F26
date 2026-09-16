#list example

shopping_list = []
shopping_list.append("apples")
shopping_list.append("bananas")
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append(42)
print("Shopping list:", shopping_list)


shopping_list.remove("milk")
print("Updated shopping list:", shopping_list)

shopping_list.pop()
print("Final shopping list:", shopping_list)