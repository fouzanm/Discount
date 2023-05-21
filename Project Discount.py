
#products=[{"A":20},{"B":40},{"C":50}]
product_price=[20,40,50]

#product names and prices
print(" Product   Prices\nProduct A:  $20\nProduct B:  $40\nProduct C:  $50 ")

wrap=0
#quantity of product
a = float(input("Quantity of A: "))
w1=input("is that product is wrapped as gift?(yes/no)")
if w1.upper()=="YES":
   wrap += a

b = float(input("Quantity of B: "))
w2=input("is that product is wrapped as gift?(yes/no)")
if w2.upper()=="YES":
   wrap += b

c = float(input("Quantity of C: "))
w3=input("is that product is wrapped as gift?(yes/no)")
if w3.upper()=="YES":
   wrap += c

price=[]
price.append(a*product_price[0])
price.append(b*product_price[1])
price.append(c*product_price[2])

#print(price)

#product details
print("Product Details:")
print("Product A: Quantity:",a,"; Total Amount: $"+str(price[0]))
print("Product B: Quantity:",b,"; Total Amount: $"+str(price[1]))
print("Product C: Quantity:",c,"; Total Amount: $"+str(price[2]))

#subtotal
subtotal= price[0] + price[1] + price[2]
print("Subtotal: $"+str(subtotal))

#total quantity
quantity= a+b+c
print("Total Quantity: ",quantity)

#list of quantities
amount=[]
amount.append(a)
amount.append(b)
amount.append(c)
#print(amount)


discount=[]

#flat 10$ discount:if subtotal exceeds 200$,a flat discount on subtotal
if subtotal > 200:
    temp = subtotal - 10
    discount.append(temp)
else :
    discount.append(subtotal)


#bulk 5% discount:If quantity of any single product exceeds 10 units, 5% discount on that item's total price
num = 0
for i in range(3):
    if amount[i] > 10:
        temp = price[i] - (price[i] * .05)
        num += temp
    else :
        num += price[i]
    #print(price[i])
#print(num)
discount.append(num)


#bulk 10% discount: If total quantity exceeds 20 units,10% discount on subtotal
if quantity > 20:
    temp = subtotal - (subtotal*.1)
    discount.append(temp)
else :
    discount.append(subtotal)


#tiered 50% discount:If total quantity exceeds 30 units & any single product quantity greater than 15.
#                    the first 15 quantity have the original price and unit above 15 will get 50% discount
val = 0
for i in range(3):
    if quantity > 30 and amount[i] > 15:
        x = amount[i] - 15
        temp = 15*product_price[i] + x*product_price[i]*.5
        val += temp
    else :
        val += price[i]
    #print(price[i])
discount.append(val)


print(discount)

#most beneficial discount for customer
min = discount[0]
for i in range(4):
    if min > discount[i]:
        min = discount[i]
if min == discount[0]:
    print("flat 10$ discount applied ; Discount amount: $"+str(subtotal - discount[0]))
elif min == discount[1] :
    print("bulk 5% discount applied ; Discount amount: $"+str(subtotal - discount[1]))
elif min == discount[2] :
    print("bulk 10% discount applied ; Discount amount: $"+str(subtotal - discount[2]))
elif min == discount[3] :
    print("tiered 50% discount applied ; Discount amount: $"+str(subtotal - discount[3]))


#gift wrap fee
print("Gift wrap price: $"+str(wrap))

#shipping fee
fee = quantity/10
shipping_fee= 5 * fee.__ceil__()
print("Shipping fee: $"+str(shipping_fee))

#Total price
total = min + shipping_fee + wrap
print("Total Price: $"+str(total))
