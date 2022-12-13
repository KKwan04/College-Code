# Programmer: Kyle Kwan
# Date 11/7/2022
# File Name: Kwan-HealthCalculator.py
# Description: This program is a BMI and heart rate calculator where the user inputs their height, weight, age, and resting heart rate.
#              This program uses the imperial BMI formula and the Karvonen Formula.

print("Please enter the following values for the user...")

# A BUNCH of checks for each input to protect the code from string inputs.
while True:
    try:
        height = int(input("Height in inches: "))
    except ValueError:
        continue
    else:
        break
while True:
    try:
        weight = int(input("Weight in pounds: "))
    except ValueError:
        continue
    else:
        break
while True:
    try:
        age = int(input("Current age: "))
    except ValueError:
        continue
    else:
        break
while True:
    try:
        heart_rate = int(input("Resting heart rate: "))
    except ValueError:
        continue
    else:
        break

# I'm using the Imperial formula for BMI since the formula you gave us was using metric.
bmi = round(weight / (height * height) * 703, 2)

# Checks what the calculated BMI is and within certain ranged tells you your health.
print("\nResults...")
if bmi <= 18.4:
    print("Your BMI is:", bmi, "-- Underweight")
elif bmi <= 24.9:
    print("Your BMI is:", bmi, "-- Healthy")
elif bmi <= 29.9:
    print("Your BMI is:", bmi, "-- Overweight")
elif bmi > 30:
    print("Your BMI is:", bmi, "-- Obese")

print(f"\nExercise Intensity Heart Rates:\nIntensity\t\tMax Heart Rate")

intensity = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# Formats the list of intensities into a percent form without decimals.
percentages = [f'{i*100:.0f}%' for i in intensity]

# Loops the Karvonen Formula until it reaches 95% intensity.
i = 0
while i < 10:
    max_heart_rate = (((220 - age) - heart_rate) * intensity[i]) + heart_rate
    print(percentages[i], "\t\t\t", round(max_heart_rate))
    i += 1

input(f"\nPress enter to exit")