# create menu 
menu = {
    'Pizza ' : 80,
    'Pasta ' : 50,
    'Burger' : 60,
    'Salad ' : 70,
    'Coffie' : 80
 }
# Greeting to costumer 
print('_____________________________________________________\n')
print('************ Welocme to Python Resturant ***********')
print('_____________________________________________________\n')
for k, v in menu.items():
    print(k,'     ',v)
print('_____________________________________________________\n')
total_amount = 0  #add to item amount to total amount 
item = input('Enter the name of item you want to order: ') # input items 
if item in menu:
    total_amount += menu[item]
    print(f'Your item{item} add to your order list:  ')
else:
    print(f'Your Ordered item {item} not available yet!') 
print('_____________________________________________________\n')

another_order = input('Do you want ordered any other item (Yes/No): ')     
if  another_order == 'Yes':
    item2 = input('Enter the name of item you want to order: ') 
    if item2 in menu:
     total_amount += menu[item2]
     print(f'Your item {item2} add to your order list:  ')
    else:
     print(f'Your Ordered item {item2} not available yet!')

print(f'Total amount have to pay:  {total_amount}')


