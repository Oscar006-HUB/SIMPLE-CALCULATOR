
#FOUR BASIC OPERATIONS Multiplication,Subtraction,Addition, and Division.
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def start_Calculator():
    print("---WELCOME TO  SIMPLE CALCULATOR---")
            
    while  True:
        try:
            Num1 = int(input("\nENTER YOUR FIRST NUMBER:"))
            
#SELECTING OPERATION
            OPERATION = input("\n ENTER OPERATION(+,-,/,*) OR Q TO QUIT:").upper()
                    
            if OPERATION =="Q":
                print("Shutting Down...")
                break
                    
            Num2 = int(input("ENTER YOUR SECOND NUMBER:"))
            
#Logic Process   
            if OPERATION =="+":
                result = add(Num1,Num2)
            elif OPERATION =="-":
                result = subtract(Num1,Num2)
            elif OPERATION =="*":
                result = multiply(Num1,Num2)
            elif OPERATION =="/":
                if Num2 == 0:
                    result ="Error:Division by Zero!"
                else:
                    result = Num1 / Num2        
            else:
                print("Invalid Operator")
                continue
                    
#RESULT OUTPUT             
            print(f"Result:{Num1}{OPERATION}{Num2} = {result}")
                        
        except ValueError:
            print("Invalid Input!Please enter a number.")                 
if __name__ == "__main__":
    start_Calculator()
    
