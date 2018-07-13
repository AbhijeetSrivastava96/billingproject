#!/usr/bin/python3
from CheckoutRegister import CheckoutRegister
ck=CheckoutRegister()

def main():
	ck.total=0.0
	ck.amount=0.0
	ck.due=0.0
	try:
		ch='Y'
		print('[+]Starting Billing Application...\n\n')
		while(ch.upper()=='Y'):
			barcode=input('Enter barcode of product:')
			#
			ck.scan_item(barcode)# checkout.py file FUNC
			#
			ch=input('\nWould you like to scan another product (y/n):')
			while (ch.upper()!='Y') and (ch.upper()!='N'):
				print('options available. y/n ?:')
				ch=input('\nWould you like to scan another product (y/n):')
				if ch.upper()=='N':
					break
			continue
		total=ck.total
		while total > 0.0:
			amount=ck.get_float("Payment due: $%2f ,Please enter an amount to pay:"%ck.due)
			total=ck.accept_payment(amount)
		ch=input('\n(N)ext customer, or (Q)uit ? :')
		while ch.upper()!='N' and ch.upper()!='Q':
			print("valid options only : N/Q ?")
			ch=input('\n(N)ext customer, or (Q)uit: ')
		if ch.upper()=='N':
			print("\n\n******Billing Next customer*******\n\n")
			ck.total=0.0
			ck.amount=0.0
			ck.due=0.0
			main()
		if ch.upper()=='Q':
			exit(0)
	except KeyboardInterrupt:
		print("\n Ctrl^c or ctrl^z , exiting...\n")
if __name__ == '__main__':
    main()

