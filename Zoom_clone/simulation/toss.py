#simulating the process of tossing a coin
import random
#function to model toss process
def toss():
    return random.choice(['Heads','Tails'])
#Main function
def Main():
    #A variable to hold number of tosses
    n_tosses = int(input("Enter number of tosses: "))
    head_count=0
    tail_count=0
    for i in range(n_tosses):
        #list to hold toss results
        ListA=[]
        #Calling the toss function 
        results= toss()

        if results=="Heads":
            head_count+=1

        else:
            tail_count+=1
    print(f"Results after{n_tosses} tosses:")
    print("Heads:", head_count)
    print("Tails:", tail_count)
   

    #call main function
    Main()