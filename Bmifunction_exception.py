def readinput():
    "This function reads users height and weight"
    while True:
        print("Enter the height in mts")
       
        try:
            users_height = float(input())

            if users_height==0 or users_height < 0:
                
            
                print("please enter a valid height")
            else: #valid height 
                break   

    # If user inputs wrong type then the except will run
        except ValueError:
            print("The value you have enteed is not a float value.Please enter the input in float value and in mts")
    while True:
       
        try:
            users_weight = float(input("Enter weiight in kg\n"))
            if users_weight==0 or users_weight < 0:
                print("Please enter a valid weight")
            else:
                break   
            # If user inputs wrong type then the except will run
        except ValueError:
            print("The value you have enteed is not a float value.Please enter the input in float value and in kilograms")
    return users_height, users_weight

def calculate_bmi(users_height,users_weight):
    "This function calculates bmi"
    
    bmi=users_weight/(users_height*users_height)
    return bmi


def category(users_height,users_weight):
    "This function decides the category"
    
    bmi = calculate_bmi(users_height,users_weight)
    print("bmi is " + str(bmi))
    if bmi<18.5:
        print ("normal")
    elif bmi>=18.5 and bmi<=24.9:
        print ("normal")
    elif bmi>=25 and bmi<=29.9:
        print ("over weight")
    elif bmi>30:
        print ("obese")

        # Program starts here

if __name__== "__main__":
    users_height,users_weight = readinput()
    category(users_height,users_weight)