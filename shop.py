inventry={
    1:{1: 'soap', 100: '30'},
    2:{2: 'jel', 100: '40'},
    3:{3: 'vim', 100: '20'},
    4:{4: 'deo', 100: '50'}}
cart={}

def banner():

    print("\n\t\t         ****welcome to Store****         ")
    print("\t\t.............................................")
    print("\t\t# 1       open Inventory\n")
    print("\t\t# 2       add product\n")
    print("\t\t# 3       show cart\n")
    print("\t\t# 4        exit"); 
    print("\t\t.............................................\n")

def display():
   print("\t*********************************************")
   print("\t\t\t***INVENTRY***")
   print("\t*********************************************")
   print("\tSNO  Prodcut  In Stock  Price")
   i=1
   for i in inventry:
    print("\t\t\t",str(inventry[i]))

   print("\t********************************************")
while(1):
 banner()
 choise=int(input("Choose number:- "))
 if choise==1:
     display()

     
 elif choise==2:
     display()
     prod_id=int(input("Enter the product id:- "))
     for i in inventry:
         if i == prod_id:
                 cart = inventry.copy()
                 print(cart.get(i))
                 
        
 elif choise==3:
      #for i in cart:
              print(cart.values())


 elif choise==4:
      print("thanks, visit again")
      break

      
            