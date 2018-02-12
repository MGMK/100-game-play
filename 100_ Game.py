sum = 0 
x = 0
y = 0
while True:
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
                               
                        
        
