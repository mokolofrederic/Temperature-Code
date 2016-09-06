
def menu():
    print("\n1. Celsius to Farenheit")
    print("\n2. Farenheit to Celsius")
    print("3. To continue")
    print("4. Exit")
    
    pick = int(input("Enter a choice: "))
    return (pick)

def toCelsius(f):
    return int((f - 32) / 1.8)

def toFarenheit(c):
    return int((c * 1.8 + 32))
    
def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            #to convert from C to F
            c = eval(input("Enter degrees Celsius: "))
            print(str(toFarenheit(c)))
        elif choice == 2:
            #covert from F to C
             f = eval(input("Enter degrees Celsius: "))
             print(str(toCelsius(f)))
             print(" ")

        elif choice == 3:
            print 
        
        if choice == 4:
            quit()
        else:
            print("invalid entry")
        choice = menu ()
        
     
main()
            






















'''print("Welcome to our Tem Conversion Program")
temp = input("What temp would you like to conver to? Please type Celsius or Fahrenheit. ")
usertemp = float(input("What is your temp to be converted. "))

if temp == "Celsius":
    usertemp = float(input("What is your temp to be converted. ")) 
    cel = round((usertemp-32) * 5 / 9, 1)
    print("Your temp in Celsius is {}".format(cel))
elif temp == "Fahrenheit":
    fah = round(usertemp * 9 / 5 + 32 ,1)
    print("Your temp in Fahrenheit is {}".format(fah))
    
print(cel, fah)'''
