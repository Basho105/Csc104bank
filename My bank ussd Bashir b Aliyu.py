# def return_to_menu():
# 	print("welcome to uba bank ussd transaction")
# 	ussd_code = int(input("Enter ussd code here: "))
def back():
	if len(pin) == 4:
		print('your account balance is',balance,'Naira')
while True:
	list_of_accont_name = ['Bashir b aliyu']
	list_of_accont_number = []
	account_pin = 2117
	balance = 10000
	ussd_code = input("Enter ussd code here: ")
	if ussd_code == '*919#':
		print('UBA')
		print("1.Airtime self\n2.Airtime others\n3.Transfer UBA\n4.Transfer other banks\n5. Transfer UBA prepaid\n6.cheak balance\n7.Pay bills\n8.Nexr.")
		option = int(input('select option:'))
		if option == 1:
			pin = input('Enter your pin')
			if len(pin) == 4:
				amount = int (input('Please enter amount:'))
				print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option == 2:
			pin = input('Enter your pin')
			if len(pin) ==4:
			   	amount = int(input('Enter amount:'))
			   	int (input('please enter destination phone number:'))
			   	print('Transaction succeful')
			   	break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option==3:
			pin = input('Enter your pin')
			if len(pin) ==4:
				amount = int(input('Enter amount:'))
				int (input('please enter UBA account number:'))
				print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option==4:
			pin = input('Enter your pin')
			if len(pin) ==4:
				int (input('please enter account number of the beneficiary'))
				amount = int(input('Enter amount:'))
				print('select bank')
				print("1.Access bank\n2.City bank nig limited\n3.Eco bank Nigeria plc\n4.FidelityBank plc\n5.First bank Nigeria limited\n6.First city monument bankplc\n7.GTB plc\n8.Unity bank \n9. Wema bank \n10.Zenith.")
				option = int(input('select option:'))
				if option == 1:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 2:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 3:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 4:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 5:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 6:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 7:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 8:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 9:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 10:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
					break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option==5:
			pin = input('Enter your pin')
			if len(pin) ==4:
				int (input('please enter card client ID (full 10 digit) or name of the beneficiary'))
				print('Transaction succeful')
			break
		elif option == 6:
			pin = input('Enter your pin')
			if len(pin) ==4:
				print('your account bal: 50000')
			break
		elif option== 7:
			pin = input('Enter your pin')
			if len(pin) ==4:
				amount = int(input('Enter amount:'))
				print('please select')
				print("1.cable TV\n2.Betting l lottery\n3.Electricity - prepaid\n4. Electricity Post paid\n5.Tolls \n6.Next.")
				option = int(input('select option:'))
				if option == 1:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 2:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 3:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 4:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 5:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 6:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break