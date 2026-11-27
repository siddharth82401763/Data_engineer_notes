print('Hello World')

print("Siddharth")

print("""  my name is 
siddhath pandey""")

s1 = "Love you india!"
print(len(s1))

"""
for s in s1:
    print(s)
    
print ("k,v")

for s11 in range(-1,(-len(s1)-1),-2 ):
    print(s1[s11])

print(s1[::-1])
 """

print(s1[0:len(s1):2])
print(s1[-1:-16: -1])

print('% ' * 2,)

#menu card  count  desh

item = ['hot dog','paneer','mixture','jilaibi']
price = ['20','40','60','80']

q1 = '-' * 20

dash_quantity = len(q1)
for tcount in range(len(item)):
    item_lenght = len(item[tcount])
    price_length = len(price[tcount])
    if (item_lenght + price_length) < dash_quantity:
        modified_dash  = dash_quantity-(item_lenght+price_length)
        print(item[tcount] + '-'*modified_dash + price[tcount])


#credid card display

user_input = input("Enter a number: ")
if len(user_input) == 16:
    x_quantity = 12
    print('X'*x_quantity + user_input[-4:16])
else:
    print('incorrect card number')







#for substance in item:



