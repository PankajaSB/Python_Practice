def readinput():
    "This function reads users height and weight"
    users_height = float(input("Enter height in m\n"))
    users_weight = float(input("Enter weiight in kg\n"))
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
    #bmi = calculate_bmi(users_height,users_weight)
    #print("bmi is " + str(bmi))
    category(users_height,users_weight)