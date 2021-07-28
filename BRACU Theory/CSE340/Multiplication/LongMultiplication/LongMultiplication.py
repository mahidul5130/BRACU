from prettytable import PrettyTable 
 
myTable = PrettyTable(["Iteration", "Multiplicand", "Multiplier", "Product"]) 

  


Multiplicand = 28
Multiplier = 3
product = 0

Multiplicand_bit=8
Product_Bit=8
Multiplier_Bit =4

myTable.add_row(["0", f"{'0'*(Multiplicand_bit-len(str(bin(Multiplicand))[2:]))}{str(bin(Multiplicand))[2:]}", f"{'0'*(Multiplier_Bit-len(str(bin(Multiplier))[2:]))}{bin(Multiplier)[2:]}", f"{'0'*(Product_Bit-len(str(bin(product))[2:]))}{str(bin(product))[2:]}"])
myTable.add_row([f"{'-'*20}", f"{'-'*20}", f"{'-'*20}", f"{'-'*20}"])

i=1

while i<=4:

    temp = len(str(bin(Multiplier))) - 1
    # print(str(bin(Multiplier))[temp])

    if str(bin(Multiplier))[temp] == "1":
        product = int(product + Multiplicand)
        myTable.add_row(["", f"{'0'*(Multiplicand_bit-len(str(bin(Multiplicand))[2:]))}{str(bin(Multiplicand))[2:]}", f"{'0'*(Multiplier_Bit-len(str(bin(Multiplier))[2:]))}{bin(Multiplier)[2:]}", f"{'0'*(Product_Bit-len(str(bin(product))[2:]))}{str(bin(product))[2:]}"])


    Multiplier = int(Multiplier/2)
    myTable.add_row(["", f"{'0'*(Multiplicand_bit-len(str(bin(Multiplicand))[2:]))}{str(bin(Multiplicand))[2:]}", f"{'0'*(Multiplier_Bit-len(str(bin(Multiplier))[2:]))}{bin(Multiplier)[2:]}", f"{'0'*(Product_Bit-len(str(bin(product))[2:]))}{str(bin(product))[2:]}"])
    Multiplicand = Multiplicand * 2
    
    myTable.add_row([f"{i}", f"{'0'*(Multiplicand_bit-len(str(bin(Multiplicand))[2:]))}{str(bin(Multiplicand))[2:]}", f"{'0'*(Multiplier_Bit-len(str(bin(Multiplier))[2:]))}{bin(Multiplier)[2:]}", f"{'0'*(Product_Bit-len(str(bin(product))[2:]))}{str(bin(product))[2:]}"])
    
    myTable.add_row([f"{'-'*20}", f"{'-'*20}", f"{'-'*20}", f"{'-'*20}"])
    # print(str(bin(Multiplicand)), end=' ')
    # print(str(bin(Multiplier)), end=' ')
    # print(str(bin(product)))
    i=i+1
    
print(myTable)
