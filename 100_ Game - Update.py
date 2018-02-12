import random 
sum = 0 
x = 0
y = 0
print 'If you want to play with player press 1'
print 'If you want to play with  computer press 2'
z = int (input (' press  here  :'))
while True:
    while (z >2 or z <0 ):
          print  'press again :'
          z = int (input (' press  here  :'))

    if (x<=10 and y<=10 and sum <= 100):
         print ('player one')
         x = int (input('Enter your number :'))
         while (x > 10 or x < 0):
             print 'TRY again '
             x= int (input('Enter your number player one : '))
         if (x <=10):
            if (sum <= 100):
                 while (x <= 10):
                    sum = sum + x
                    print 'Now the sum is :',sum 
           
                    break
                 if (sum >= 100 ): 
                    print ('your winner 1')
                    break

    if (z == 1 ):
        if (x<=10 and y<=10 and sum <= 100):
                  
             print ('player two')
             y = int (input('Enter your number :'))
             while (y > 10 or y < 0):
                 print 'TRY again '
                 y= int (input('Enter your number player two : '))
             if (y <=10):
                if (sum <= 100):
                     while (y <= 10 ):
                        sum = sum + y
                        print 'Now the sum is :',sum 
                        break
                     if (sum>=100 ):
                        print ('your winner 2')
                        break
    elif (z == 2 ):               
         size = random.randint(0,10)                          
         if (sum <= 100 and size <= 10):
             while (size <= 10):
                 sum = sum + size
                 print 'Computer will play ',size
                 print 'Now the sum is :',sum 
                 break
                 if (sum >= 100):
                    print 'Computer winner'
  
