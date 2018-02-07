sum = 0
x = 0
y = 0
while True:
    if (x<=10 and y<=10 and sum <= 100):
         print ('player one')
         x = int (input('Enter your number :'))
         if (x > 10):
             print 'error '
             break 
         if (x <=10):
            if (sum <= 100):
                 while (x <= 10):
                    sum = sum + x
                    break
                 if (sum == 100 ):
                    print ('The winner is : player one ')
                    break               
                        
         print ('player two')
         y = int (input('Enter your nunmber :'))
         if (y <=10):
            if (sum <= 100):
                while (y <= 10):
                    sum = sum + y       
                    break
                if (sum == 100 ):
                    print ('The winner is : player two ')
                    break              
    else :   
         print ('error')
         break
#-------------------------------------------------------------------------------------
# Note :->
#------------------     
# This is the game idea : 100 game. Two players start from 0 , 
# and alternatively add a number from 1 to 10 to the sum.
#   The player who reaches 100 wins
#--------------------------------------------------------------------------------------
# This game create by mohamed hamdy 
