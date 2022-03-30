# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name=input("Enter your name: ")
out_file=open("name",'w')
print(name,file=out_file)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
name=input("Enter your name: ")
in_file=open("name",'r')
print(f"Your name is {in_file.read()}")
in_file.close()

# 3.
out_file=open("numbers",'w')
print(17,file=out_file)
print(42,file=out_file)
print(400,file=out_file)
out_file.close()

in_file=open("numbers",'r')
count=0;sum=0
for line in in_file:
    if count==2:
        break
    sum+=int(line)
    count+=1
print(sum)
in_file.close()

# 4.
in_file=open("numbers",'r')
count=0;sum=0
for line in in_file:
    sum+=int(line)
print(sum)
in_file.close()







