#B shape

#       0    1   2   3   4     

#   0   *    *   *   *    *

#   1   *                 *

#   2   *                 *

#   3   *    *   *   *    *

#   4   *                 *

#   5   *                 *

#   6   *    *   *   *   *




#B shape

#       0    1   2   3   4     

#   0   *    *   *   *    

#   1   *                 *

#   2   *                 *

#   3   *    *   *   *    

#   4   *                 *

#   5   *                 *

#   6   *    *   *   *   



for row in range(0,7):

    for col in range(0,5):

        #if (col==0 or col==4) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):

        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)): 


         print("*" , end=" ")

        else:

         print(" ", end=" ")


    print("")  