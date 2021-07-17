#remove all those items from the dictionary whos value is greater than 1

x= {"a":1,"b":2,'c':3}
x=dict((key, value) for key, value in x.items() if value <=1)
print(x)