for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0,101,10):
    print(j, end=" ")
print()

for number in range(20,0,-1):
    print(number, end=" ")
print()

num_of_stars=int(input('Enter the number of stars: '))
for star in range(0,num_of_stars):
    print('*',end='')
print()

for i in range(0,4):
    for j in range(0,i+1):
        print('*',end="")
    print()