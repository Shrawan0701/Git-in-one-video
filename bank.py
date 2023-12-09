data=[]
for i in range(0,5):
    a = input("Enter the transaction : ")
    data.append(a)
    net_amount=0
for i in data:
    transaction =i.split()

    trans_type = transaction[0] 
    amount = int(transaction [1])
    if trans_type =="D":
     net_amount += amount
    if trans_type =="W":
     net_amount -=amount
print("The bank balance is: ",net_amount)