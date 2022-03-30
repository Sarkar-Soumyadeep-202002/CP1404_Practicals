number_of_items=int(input('Number of items: '))
total=0.0
for item in range(0,number_of_items):
    price=float(input('Price of item: '))
    total+=price
if total>100:
    total-=10/100*total
print(f'Total price for {number_of_items} items is {total:.2f}$')