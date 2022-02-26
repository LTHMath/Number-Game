import math
def megascaling(y):
  if y<100:
    return 1
  elif y==100:
    return 1.01
  else:
    return megascaling(y-1)*(((y-100)//5)*0.002+1.01)

def multi_formula(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  norm = (x%2)*40+81*(x//2)
  modednorm = norm*(1/(((ac1complete or inac1) and (not inac2))+1))
  scaling=(1.1**((x-20)//5))*(x>24)+(x<25)
  superscaling=(1.5**((x-40)//10))*(x>49)+(x<50)
  scalednorm=modednorm*scaling*superscaling*megascaling(x)
  if x==multi+1:
    return math.floor(scalednorm)
  else:
    start = multi_formula(multi+1)
    norm2 = math.floor(start+2*(scalednorm-start))
  return norm2

def base_conversion(number, base):
  result = 0
  digit = 0
  if base > 10:
    print('There is no support for this function yet until hexadecimal numbers are implemented, please give 3-5 business days.')
    #insert thingy thing here
  elif base < 2:
    print('An error has occurred in the code, check all features having to do with base if you are the developer.')
  elif isinstance(base, int):
    while int(number) > 0:
      result += (int(number) % (base)) * (10**digit)
      digit += 1
      number = (number - (int(number) % (base))) / base
    else:
      return result

def incremetybonus(incremetyinbase, multi, base):
  i=math.floor(math.log(incremetyinbase,10))+1
  j=math.floor(math.log(incremetyinbase,10))+1
  result=0
  while i>0:
    if incremetyinbase%(10^(j-i))<base:
      result+=incremetyinbase%(10^(j-i))*10^(j-i)
    else:
      result+=(base-1)*10^(j-i)
    i=i-1
  result=reverse_base_conversion(result, base)
  result=result*multi
  result=base_conversion(result, base)
  return result

def n():
  return numberinbase

def reverse_base_conversion(number, base):
  result = 0
  digit = 0
  midnumber = number
  while midnumber != 0:
    result += (midnumber % 10) * (base**digit)
    midnumber = (midnumber - midnumber % 10) / 10
    digit += 1
  return int(result)

def legalnumberinbase(number, base):
  midnumber = number
  result = True
  while midnumber != 0:
    result = result and (midnumber % 10 < base)
    midnumber = (midnumber - midnumber % 10) / 10
  return result

#toggleables
sp1 = False
sp2 = False
inac1 = False
ac1complete = False
inac2 = False
ac2complete = False
#not curently used
multiplier = 1
#reset on ac entrance
multi = 5
incremetybase = 10
#reset on multi reset
base = 9
increment = 1
ivmulti = int(multi / 5 + 1)
#reset on base reset
number = 100000
numberinbase = base_conversion(number, base)
nextnumberbase10 = int(number + multi * increment)
nextnumberinbase = base_conversion(nextnumberbase10, base)
incremety = 100
incremetyinbase = base_conversion(incremety, base)
nextincremetybase10 = int(incremety + ivmulti)
nextincremetyinbase = base_conversion(nextincremetybase10, base)

def ib(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global incremetybase
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if x == 1:
    if incremetybase == 10:
      if incremety >= 5000:
        multi = 1
        incremetybase = 9
        base = 10
        increment = 1
        ivmulti = int(multi / 5 + 1)
        number = 0
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        incremety = 0
        incremetyinbase = base_conversion(increment, base)
        nextincremetybase10 = int(number + ivmulti)
        nextincremetyinbase = base_conversion(nextincremetybase10, base)
        print('Congratulations! You have reset for incremety boost 1! Your base in incremty is now 9.')
      else:
        print('Sorry! You need 5000 incremety for incremety boost 1.')
    else:
      print('You must boost your incremety base to 10 before boosting it to 9!')
  elif x == 2:
    if incremetybase == 9:
      if incremety >= 10000:
        multi = 1
        incremetybase = 8
        base = 10
        increment = 1
        ivmulti = int(multi / 5 + 1)
        number = 0
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        incremety = 0
        incremetyinbase = base_conversion(increment, base)
        nextincremetybase10 = int(number + ivmulti)
        nextincremetyinbase = base_conversion(nextincremetybase10, base)
        print('Congratulations! You have reset for incremety boost 2! Your base in incremty is now 8.')
      else:
        print('Sorry! You need 10000 incremety for incremety boost 2.')
    else:
      print('You must boost your incremety base to 9 before boosting it to 8!')
  elif x == 3:
    if incremetybase == 8:
      if incremety >= 15000:
        multi = 1
        incremetybase = 7
        base = 10
        increment = 1
        ivmulti = int(multi / 5 + 1)
        number = 0
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        incremety = 0
        incremetyinbase = base_conversion(increment, base)
        nextincremetybase10 = int(number + ivmulti)
        nextincremetyinbase = base_conversion(nextincremetybase10, base)
        print('Congratulations! You have reset for incremty boost 3! Your base in incremty is now 7.')
      else:
        print('Sorry! You need 15000 incremety for incremety boost 3.')
    else:
      print('You must boost your incremety base to 8 before boosting it to 7!')
  elif x == 4:
    if incremetybase == 7:
      if incremety >= 20000:
        multi = 1
        incremetybase = 6
        base = 10
        increment = 1
        ivmulti = int(multi / 5 + 1)
        number = 0
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        incremety = 0
        incremetyinbase = base_conversion(increment, base)
        nextincremetybase10 = int(number + ivmulti)
        nextincremetyinbase = base_conversion(nextincremetybase10, base)
        print('Congratulations! You have reset for incremty boost 3! Your base in incremty is now 6.')
      else:
        print('Sorry! You need 20000 incremety for incremety boost 4.')
    else:
      print('You must boost your incremety base to 7 before boosting it to 6!')
  else:
    print('INVALID INCREMETY BASE AHHHHHHHHHHHHH')

def sp1unlock():
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if multi >= 5:
    sp1 = True
    print('You have unlocked subtraction perk 1! This allows you to reset for multiple multis, but with harsher scaling!')
  else:
    print('You need multi 5 to do this!')

def sp2unlock():
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if multi >= 10:
    sp2 = True
    print('You have unlocked subtraction perk 2! This allows you to undercount!')
  else:
    print('You need multi 10 to do this!')

def ic(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if sp2 == True:
    if x <= nextincremetyinbase and x > incremetyinbase:
      if legalnumberinbase(x, incremetybase):
        incremetyinbase = x
        incremety = reverse_base_conversion(incremetyinbase,incremetybase)
        incremetyinbase = base_conversion(incremety, incremetybase)
        nextincremetybase10 = int(incremety + ivmulti)
        nextincremetyinbase = base_conversion(nextincremetybase10,incremetybase)
        print(incremetyinbase)
      else:
        print("That is not a legal number in base " + str(incremetybase) + ".")
    else:
      print('Invalid number!!!!!!!!!!!!!!!!')
  elif x == nextincremetyinbase:
    incremety = nextincremetyinbase
    nextincremetybase10 = int(incremety + ivmulti)
    incremetyinbase = nextincremetyinbase
    nextincremetyinbase = base_conversion(nextincremetybase10, incremetybase)
    print(incremetyinbase)
  else:
    print("Sorry, your number is invalid, please try agian.")

def c(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if sp2 == True:
    if x <= nextnumberinbase and x > numberinbase:
      if legalnumberinbase(x, base):
        numberinbase = x
        number = reverse_base_conversion(numberinbase, base)
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print(numberinbase)
      else:
        print("That is not a legal number in base " + str(base) + ".")
    else:
      print('Invalid number!!!!!!!!!!!!!!!!')
  elif x == nextnumberinbase:
    number = nextnumberbase10
    nextnumberbase10 = int(number + multi * increment)
    numberinbase = nextnumberinbase
    nextnumberinbase = base_conversion(nextnumberbase10, base)
    print(numberinbase)
  else:
    print("Sorry, your number is invalid, please try agian.")

def b(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if x == 2:
    print('Sorry, this feature has not been introduced yet, please wait for the next update.')
  if x == 3:
    if inac1 == False:
      if base == 4:
        if ac1complete == True:
          if numberinbase >= 200:
            number = incremetyinbase*multi
            base = 3
            numberinbase = base_conversion(number, base)
            nextnumberbase10 = int(number + multi * increment)
            nextnumberinbase = base_conversion(nextnumberbase10, base)
            print('Congratulations! You have reset for base 3!')
          else:
            print('Sorry, you cannot reset for base 3 yet, you need a number of at least 200 to do that.')
        elif numberinbase >= 1000:
          number = incremetyinbase*multi
          base = 3
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 3!')
        else:
          print('Sorry, you cannot reset for base 3 yet, you need a number of at least 1000 to do that.')
      else:
        print('Sorry, you cannot reset for base 3 yet, you must first reset for base 4.')
    else:
      print('AC1 has disabled base 3.')
  elif x == 4:
    if base == 5:
      if inac1 or ac1complete == True:
        if numberinbase >= 200:
          number = incremetyinbase*multi
          base = 4
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 4! You need 200 to reset for base 3.')
        else:
          print('Sorry, you cannot reset for base 4 yet, you need a number of at least 200 to do that.')
      elif numberinbase >= 400:
        number = incremetyinbase*multi
        base = 4
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 4! You need 1000 to reset for base 3.')
      else:
        print('Sorry, you cannot reset for base 4 yet, you need a number of at least 400 to do that.')
    else:
      print('Sorry, you cannot reset for base 4 yet, you must first reset for base 5.')
  elif x == 5:
    if base == 6:
      if inac1 or ac1complete == True:
        if numberinbase >= 150:
          number = incremetyinbase*multi
          base = 5
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 5! You need 200 to reset for base 4.')
        else:
          print('Sorry, you cannot reset for base 5 yet, you need a number of at least 150 to do that.')
      elif numberinbase >= 300:
        number = incremetyinbase*multi
        base = 5
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 5! You need 400 to reset for base 4.')
      else:
        print('Sorry, you cannot reset for base 4 yet, you need a number of at least 400 to do that.')
    else:
      print('Sorry, you cannot reset for base 5 yet, you must first reset for base 6.')
  elif x == 6:
    if base == 7:
      if inac1 or ac1complete == True:
        if numberinbase >= 125:
          number = incremetyinbase*multi
          base = 6
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 6! You need 150 to reset for base 5.')
        else:
          print('Sorry, you cannot reset for base 6 yet, you need a number of at least 125 to do that.')
      elif numberinbase >= 250:
        number = incremetyinbase*multi
        base = 6
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 6! You need 300 to reset for base 5.')
      else:
        print('Sorry, you cannot reset for base 6 yet, you need a number of at least 250 to do that.')
    else:
      print('Sorry, you cannot reset for base 6 yet, you must first reset for base 7.')
  elif x == 7:
    if base == 8:
      if ac1complete or inac1 == True:
        if numberinbase >= 100:
          number = incremetyinbase*multi
          base = 7
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 7! You need 125 to reset for base 6.')
      elif numberinbase >= 200:
        number = incremetyinbase*multi
        base = 7
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 7! You need 200 to reset for base 6.')
      else:
        print('Sorry, you cannot reset for base 7 yet, you need a number of at least 200 to do that.')
    else:
      print('Sorry, you cannot reset for base 7 yet, you must first reset for base 8.')
  elif x == 8:
    if base == 9:
      if inac1 or ac1complete:
        if numberinbase >= 75:
          number = incremetyinbase*multi
          base = 8
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 8! You need 100 to reset for base 7.')
        else:
          print('Sorry, you cannot reset for base 8 yet, you need a number of at least 75 to do that.')
      elif numberinbase >= 150:
        number = incremetyinbase*multi
        base = 8
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 8! You need 200 to reset for base 7.')
      else:
        print('Sorry, you cannot reset for base 8 yet, you need a number of at least 150 to do that.')
    else:
      print('Sorry, you cannot reset for base 8 yet, you must first reset for base 9.')
  elif x == 9:
    if base == 10:
      if inac1 or ac1complete:
        if numberinbase >= 50:
          number = incremetyinbase*multi
          base = 9
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi * increment)
          nextnumberinbase = base_conversion(nextnumberbase10, base)
          print('Congratulations! You have reset for base 9! You need 75 to reset for base 8.')
        else:
          print('Sorry, you cannot reset for base 9 yet, you need a number of at least 50 to do that.')
      elif numberinbase >= 100:
        number = incremetyinbase*multi
        base = 9
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have reset for base 9! You need 150 to reset for base 8.')
      else:
        print('Sorry, you cannot reset for base 9 yet, you need a number of at least 100 to do that.')
    else:
      print('Sorry, you cannot reset for base 9 yet, you must first reset for base 10.')
  else:
    print('Invalid base!')

def m(x):
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if x < 2:
    print('You cannot reset for a multi less than 2!!! Please try again.')
  elif isinstance(x, int):
    if sp1 == True:
      if x >= multi + 1:
        if number>= multi_formula(x):
          number = incremetyinbase*multi
          base = 10
          multi = x
          numberinbase = base_conversion(number, base)
          nextnumberbase10 = int(number + multi *   increment)
          nextnumberinbase = base_conversion  (nextnumberbase10, base)
          print('Congratulations! You have done a multi reset!')
        else:
          'Sorry, you need a number of'
    elif x > multi + 1:
      print('Sorry, you have not unlocked sp1 yet, so you cannot reset for multiple multis at a time.')
    elif x == multi + 1:
      if number>=multi_formula(x):
        number = incremetyinbase*multi
        base = 10
        multi = x
        numberinbase = base_conversion(number, base)
        nextnumberbase10 = int(number + multi * increment)
        nextnumberinbase = base_conversion(nextnumberbase10, base)
        print('Congratulations! You have done a multi reset!')
    else:
      print('You cannot reset for a multi less than your current one!')
  else:
    print('You can only reset to an integer multi, sorry.')

def ac1():
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if numberinbase >= 100000:
    base = 10
    multi = 1
    increment = multi
    number = 0
    numberinbase = base_conversion(number, base)
    nextnumberbase10 = int(number + multi * increment)
    nextnumberinbase = base_conversion(nextnumberbase10, base)
    inac1 = True
    print('You have entered ac1! Reach 100000 and then do completeac1() to complete the challenge!')

def exitac1():
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if inac1:
    inac1 = False
    print('You have exited ac1!')
  else:
    print("You can't exit ac1 if you are not in ac1 ya idiot")

def completeac1():
  global inac1
  global ac1complete
  global sp1
  global sp2
  global multiplier
  global multi
  global base
  global increment
  global number
  global numberinbase
  global nextnumberbase10
  global nextnumberinbase
  global incremety
  global incremetyinbase
  global nextincremetybase10
  global nextincremetyinbase
  if numberinbase >= 100000 and inac1 == True:
    base = 3
    multi = 1
    increment = multi
    number = 0
    numberinbase = base_conversion(number, base)
    nextnumberbase10 = int(number + multi * increment)
    nextnumberinbase = base_conversion(nextnumberbase10, base)
    inac1 = False
    ac1complete = True
    print('Congratulations on completing ac1! The boost from this challenge is now permenant!')
  elif inac1 == True:
    print('Reach 100000 before completing ac1.')
  else:
    print('You are not in ac1!')