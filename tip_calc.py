bill = str(raw_input("What is the total bill amount?"))

service = int(raw_input("Level of the service?"))

if service == "good":
    print "'%.2f' % amount" + bill +(bill * (20/100))

elif service == "fair":
    print (bill * (15/100))

else:
    print (bill * (10/100))
