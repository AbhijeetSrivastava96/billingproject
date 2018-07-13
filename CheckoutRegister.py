#!/usr/bin/python3
from Product import product
class CheckoutRegister:
##
#   initialize product_cart using product class in Product.py 
##
    def __init__(self):
        self.product=product()
        self.a=self.product.a
        self.b=self.product.b
        self.c=self.product.c
        self.d=self.product.d
        self.e=self.product.e
        self.f=self.product.f
        self.g=self.product.g
        self.h=self.product.h
#
        self.bagged_product=[]
        self.total=0.0
        self.due=0.0
        self.amount=0.0
        self.product_cart=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]
#get float value only
#
    def	get_float(self,prompt):
#call function 
        value = float(0.0)
# initialize value for var 'value'
        while True:
            try:
		# convert input <str> to <float>
                value=float(input(prompt))
		# check iof value is greater than 0.0 (positive)
                if 0.0 > value:
                    print("We don't accept negative money!")
                    continue
# ths continue will skip the remaining loop and start over
                break
# break will stop loop execution when it get executed
            except ValueError:
                print('Please enter a valid floating point value.')
# exception handeled if value is not float  and retrn if no exeception occur and value is positive
        return value

##
#   scan item in product list using barcode
##
    def scan_item(self,barcode):

##

##
        for i in range(len(self.product_cart)):
            current_product=self.product_cart[i]
            barcode=str(barcode)
            #print(current_product)
            if barcode == current_product['barcode']:
                print("%s  $ %s \n"%(current_product['name'],current_product['price']))
                self.bagged_product.append(current_product)
                self.total += current_product['price']
                self.due=self.total
                break
                #return current_product
            else:
                if (i==len(self.product_cart)-1):
                    print("product doesn't exist in inventory...\n") 
                    
    def accept_payment(self,amount):
        self.amount += amount
        self.due -= amount
        if self.due <= 0.0:
            self.print_reciept()
            return self.due
        else:
            return self.due


    def print_reciept(self):
        print("\n**************FINAL PAYMENT RECEIPT******************")
        for _ in range(len(self.bagged_product)):
            temp=self.bagged_product[_]
            print("%s \t\t:\t\t$"%temp['name'],temp['price'])
        print("Total Due	:\t\t$",self.total)
        print("Total Amount 	:\t\t$ %2f"%self.amount)
        print("Remaining change:\t\t$ %2f"%(self.amount - self.total))
        print("\nThankyou for shopping... visit again\n\n")
        
