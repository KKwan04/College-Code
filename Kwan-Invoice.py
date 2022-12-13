# Programmer: Kyle Kwan
# Date 10/16/2022
# File Name: Kwan-Invoice.py
# Description: This program is an invoice of a student at Columbus State Communtiy College.
#              It takes the fees of books, labs, and tuition ad totals them all together.

# It's possible to also assign the all the variables in one line of code.
# college, college_address, college_location, product1, price1, product2, price2, product3, price3, total, message = "Columbus State Community College", "550 East Spring Street", "Columbus, OH 43215", "Books", 52.99, "Lab Fees", 25.00, "Tuition", 157.93 * 3, price1 + price2 + price3, "Thank you for being a Columbus State Student!"
# I find this highly unpractical as it is such a long line of code now and in very hard to decipher.

college = "Columbus State Community College"
college_address = "550 East Spring Street"
college_location = "Columbus, OH 43215"

product1, price1 = "Books", 52.99
product2, price2 = "Lab Fees", 25.00
product3, price3 = "Tuition", 157.93 * 3

total = price1 + price2 + price3

message = "Thank you for being a Columbus State Student!"

print("*" * 50)

# Another way of executing the 3 lines below is by using:
# college_info = f"\t{college}\n\t{college_address}\n\t{college_location}"
# print (college_info)
# -OR-
# print (f"\t{college}\n\t{college_address}\n\t{college_location}")
# It keeps it all in one line but makes it hard to decipher at first glance.

print (f"\t{college}")
print (f"\t{college_address}")
print (f"\t{college_location}")

print("=" * 50)

# Another way of executing the 4 lines below is by using:
# product_list = f"\tProduct Name:\tProduct Price:" f"\n\t{product1}\t\t${price1}\n\t{product2}\t${price2}\n\t{product3}\t\t${price3}"
# print (product_list)
# -OR-
# print (f"\tProduct Name:\tProduct Price:" f"\n\t{product1}\t\t${price1}\n\t{product2}\t${price2}\n\t{product3}\t\t${price3}")
# It keeps it all in one line but makes it hard to decipher at first glance.

print("\tProduct Name:\tProduct Price:")
print (f"\t{product1}\t\t${price1}")
print (f"\t{product2}\t${price2}")
print (f"\t{product3}\t\t${price3}")

print ("=" * 50)

# Another way of executing the 2 lines below is by using:
# print (f"\t\t\tTotal:\n\t\t\t${total}")
# It keeps it all in one line but makes it hard to decipher at first glance.

print (f"\t\t\tTotal:")
print (f"\t\t\t${total}")

print ("=" * 50)

# I would have used:
# print (f"\n  {message}\n")
# Since when you use \t it causes the message to not be center.

print (f"\n\t{message}\n")

print ("*" * 50)

input(f"\n\t\tPress enter to exit")