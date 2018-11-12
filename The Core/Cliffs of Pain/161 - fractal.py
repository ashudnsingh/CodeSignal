'''
Created on Nov 12, 2018

@author: sinashu
'''

def fractal(n):
    
    def algo1(quarter, quarter2):
        half1 = [quarter[i] + quarter2[i] for i in range(len(quarter))]
        half2 = [quarter[i] + quarter2[i] for i in range(len(quarter)-1, -1, -1)]
        for i in range(len(half2) - 1, -1, -1):
            for j in range(len(half2[i])):
                if half2[i][j] == '|':
                    half2[i][j] = ' '
                    half2[i + 1][j] = '|'
        half2[0][-len(quarter[0])+1] = '|'
        return half1 + half2
        
    def algo2(quarter, quarter2):
        quarter2[0][0] = '|'
        half1 = quarter + quarter2
        half2 = [row[::-1] for row in half1]
        half1 = [row + [' '] for row in half1]
        half1[len(quarter)][-1] = '_'
        return [half1[i] + half2[i] for i in range(len(half1))]
    
    def normal(n):
        if n == 1:
            return [[' ', '_', ' '], [' ', '_', '|']]
        quarter, quarter2 = normal(n - 1), turned(n - 1)
        if n % 2:
            quarter = [row + [' '] for row in quarter]
            quarter[0][-1] = '_'
            quarter[0][-2] = '_'
            return algo1(quarter, quarter2)
        return algo2(quarter, quarter2)
            
    def turned(n):
        if n == 1:
            return [[' ', ' ', ' '], ['|', '_', '|']]
        quarter, quarter2 = turned(n - 1), normal(n - 1)
        if n % 2:
            quarter2[0][-1] = '_'
            return algo2(quarter, quarter2)
        quarter = [row + [' '] for row in quarter]
        quarter[0][-1] = '_'
        quarter2[0][0] = '_'
        return algo1(quarter, quarter2)
    
    return normal(n)


for n in range(1,7) :
    print ("For n = " + str(n) + " : ")
    print ( fractal(n) )

"""

For n = 1, the fractal looks as follows:
[[' ', '_', ' '],
 [' ', '_', '|']]

In other words, it should represent the following picture:
                  _
                  _| 


For n = 2, the fractal looks as follows:

[[' ', '_', ' ', ' ', ' ', '_', ' '],      
 [' ', '_', '|', ' ', '|', '_', ' '],                                  
 ['|', ' ', ' ', '_', ' ', ' ', '|'],                                 
 ['|', '_', '|', ' ', '|', '_', '|']]

Or, to put it differently:  _   _
                            _| |_
                           |  _  |
                           |_| |_| 

For n = 3, the fractal looks as follows:

                      _   ___   ___ 
                      _| |_  |_|  _|
                     |  _  |  _  |_ 
                     |_| |_| | |___|
                      _   _  |  ___ 
                     | |_| | |_|  _|
                     |_   _|  _  |_ 
                      _| |___| |___|
# For n = 4, the fractal looks as follows:

               _   ___   ___   ___   ___   _ 
               _| |_  |_|  _| |_  |_|  _| |_ 
              |  _  |  _  |_   _|  _  |  _  |
              |_| |_| | |___| |___| | |_| |_|
               _   _  |  ___   ___  |  _   _ 
              | |_| | |_|  _| |_  |_| | |_| |
              |_   _|  _  |_   _|  _  |_   _|
               _| |___| |___| |___| |___| |_ 
              |  ___   ___   _   ___   ___  |
              |_|  _| |_  |_| |_|  _| |_  |_|
               _  |_   _|  _   _  |_   _|  _ 
              | |___| |___| | | |___| |___| |
              |_   _____   _| |_   _____   _|
               _| |_   _| |_   _| |_   _| |_ 
              |  _  | |  _  | |  _  | |  _  |
              |_| |_| |_| |_| |_| |_| |_| |_|

"""
