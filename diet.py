def bmi_calculator(weight, height):
    bmi=weight/((height/100)**2)
    return round(bmi,2)

def bmr_calculator(gender,age,weight,height):
    if gender=='male':
        bmr= (10*weight)+ (6.25*height)-(5*age)+5
        return bmr
    elif gender=='female':
        bmr=(10*weight)+ (6.25*height)-(5*age)-161
        return bmr
    
def tdee_calculator(bmr,activity):
        activity_factor={
            "Sedentary" : 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725,
            "Extra Active": 1.90
            }
        tdee=bmr*activity_factor[activity]
        return tdee
    
def calorie_target(tdee,aim):
        if aim =="weight maintain":
            calorie=tdee
        elif aim== "weight loss":
            calorie= tdee-400
        elif aim== "weight gain":
            calorie= tdee+300
        return calorie
        
print(bmi_calculator(60,150))
bmr=bmr_calculator("male", 25,60,150)
print("BMR:", bmr)
tdee=tdee_calculator(bmr, 'Very Active')
print("TDEE:", tdee)
print (calorie_target(tdee,"weight loss"))