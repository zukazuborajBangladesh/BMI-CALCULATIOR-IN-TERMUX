# BMI Calculator with Feet-Inch to Meter Conversion

# Take inputs
weight = float(input("Enter your weight (kg): "))
feet = int(input("Enter height (feet): "))
inch = int(input("Enter remaining height (inch): "))

# Convert height to meters
height = (feet * 0.3048) + (inch * 0.0254)

# Calculate BMI
bmi = weight / (height ** 2)

# Show result
print("\nYour height in meters:", round(height, 2))
print("Your BMI is:", round(bmi, 2))

# BMI category
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")