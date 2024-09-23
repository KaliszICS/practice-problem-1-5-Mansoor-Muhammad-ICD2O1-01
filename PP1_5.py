'''
Lesso: Typecasting
Author: Mansoor Muhamamd
Date Last Modified: September 23, 2024
'''
def q1():
  wondr = input("Input an integer: ")
  wondr = int(wondr + 3)
  print(wondr)


def q2():
  wicker = input("Input a number: ")
  wicker = float(str(wicker) + "4") + 2
  print(wicker)


def q3():
  id = input("Input a radius: ")
  id = float(id)
  print(id*id*3.14)


def q4():
  did = input("Input a number: ")
  did = float(did)
  did = int(did*12)
  print(did)

def q5():
  new = input("Input an integer: ")
  new = int(new + 5)
  print(f"Your number + 5 is {new}")

#Comment this code out when running tests
#Do not comment this out when running your program normally
'''
q1()
q2()
q3()
q4()
q5()
'''