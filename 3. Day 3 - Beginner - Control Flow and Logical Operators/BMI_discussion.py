# BMI = body mass index
# BMI = (weight)/ (height * height )


height = input("Enter your height in meter : ")
weight =  input("Enter your weight in kg : ")

# new_height = float (height)
# new_weight= float(weight)

your_bmi =  ( float(weight) / float( height)* 2 )
BMI = float(your_bmi)

#print( "Your BMI is " + str(BMI)   )

if BMI<= 18.5:
    print(f"Your BMI is {BMI}. You are Under Weighted")
elif BMI <= 25 :
    print(f"Your BMI is {BMI}. You are Normal Weighted")
elif BMI <= 30 :
    print(f"Your BMI is {BMI}. You are overweighted")
elif BMI <= 35: 
    print(f"Your BMI is {BMI}. You are obese ")
elif BMI >35:
    print(f"Your BMI is {BMI}. You are clinically Obese ")