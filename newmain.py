import math
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
    
number = 0
numberbase10
base = 10

def valid_count(x):
  return x == number + 1


def c(x):
  if valid_count(x):
    number = x
    return x
