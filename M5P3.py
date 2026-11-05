books = int(input("Enter number of books: "))
price = float(input("Enter price per book: "))

order_total = books * price

if order_total > 50:
    shipping = 0
else:
    shipping = 25

print("Order total:", order_total)
print("Shipping charge:", shipping)