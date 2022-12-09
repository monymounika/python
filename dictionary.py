#Dictionary
dic = {1:'Hema',2:'Satya', 3:'Mounika', 4:'Devi'}
print(dic[1])
print(dic.values()) # To print all the values
print(dic.keys()) # To print all the keys
dic[5] = 'From'
dic[6] = 'Computer Science and Engineering'
print(dic.values()) # To print all the values
print()

dic1 = {
    "College":'Aditya  College Of Engineering',
    "Location":'Surampalem, AP',
    "Roll No.":'19MH1A05B0',
    "Department":'Computer Science and Engineering'
}
for info in dic1: 
    print(info) # It will only shows the keys
print()
for val in dic1: 
    print(dic1[val]) # It will only shows the values

#taking inputs for using for loop
'''College = {}
for i in range(3):
    name = input("Enter name: ")
    rollnumber = input("Enter Roll Number: ")
    College[name] = rollnumber
print(College)'''

#Getting input from user and print it in a dictionary formate
name = input("Enter name: ")
rollnum = input("Enter Roll Number: ")
print({name:rollnum})