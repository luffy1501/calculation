from replit import clear
import art
print(art.logo)

def add(num1,num2):
  return num1 + num2
def sub(num1,num2):
  return num1 - num2
def multiply(num1,num2):
  return num1 * num2
def divide(num1,num2):
  return num1 / num2

operation = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide
}
repeat = True
while repeat:

  num1 = int(input("What is the first number?"))
  num2 =int(input("What is the second number?"))
  
  for symbols in operation:
    print(symbols)
  operation_symbol=input("Pick an operation from the line above: ")
  calculation_function = operation[operation_symbol]
  answer = calculation_function(num1,num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  repeat = input("Do you want to continue?")
  if repeat =="yes":
    clear()
  else:
    repeat = False
  
 
  


