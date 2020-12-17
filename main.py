print('Welcome to the Tower ATM')
restart = ('Y')
chances = 3
balance = 999.99
while chances >= 0:
  pin = int(input('Please enter your 4 digit pin:\n'))
  if pin ==(1234):
    while restart not in ('n', 'NO', 'no', 'N', 'No', 'nO'):
      print('Please press 1 for your balance')
      print('Please press 2 to make a withdrawl')
      print('Please press 3 to pay' )
      print('PLease press 4 to return your card\n')
      option = int(input('What would you like to choose?: '))
      if option == 1:
        print('Your balance is £',balance)
        restart = input('Would you like to another option?\n')
        if restart in ('n', 'NO', 'no', 'N', 'No', 'nO'):
          print('Thank you, have a nice day.')
          break
      elif option == 2:
        option2 = ('y')
        withdrawl = float(input('How much would you like to withdraw?\n10, 20, 40, 60, 80, 100 for other enter 1:\n'))
        if withdrawl in [10, 20, 40, 60, 80, 100]:
          balance = balance - withdrawl
          print('\nYour new balance is £', balance)
          restart = input('Would you like to go back?\n')
          if restart in ('n', 'NO', 'no', 'N', 'No', 'nO'):
            print('Thank you and please have a nice day.')
            break
        elif withdrawl != [10, 20, 40, 60, 8, 100]:
          print('Invalid amount, please re-type\n')
          restart = ('y')
        elif withdrawl == 1:
          withdrawl = float(input('Please enter desired amount:\n'))
      elif option == 3:
        pay_in = float(input('How much would you like to pay into your account?\n'))
        balance = balance + pay_in
        print('Thank you, your balance is now £', balance)
        restart = input('Would you like to go back?\n')
        if restart in ('n', 'NO', 'no', 'N', 'No', 'nO'):
            print('Thank you and please have a nice day.')
            break
      elif option == 4:
        print('Please wait whilst you card is returned...\n')
        print('Thank you for using Tower ATMs')
        break
      else:
        print('Please enter a correct number. \n ')
        restart = ('y')
  elif pin != ('1234'):
    print('Sorry, incorrect pin')
    chances = chances - 1
    if chances == 0:
      print('\n Sorry no more tries')
      break

        

     
