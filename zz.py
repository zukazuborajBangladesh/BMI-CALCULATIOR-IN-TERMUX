import pyfiglet
import time

# Colors
GREEN = "\033[92m"

# Mini Human Body Banner
print(GREEN + """
     _________________________
       (, ______________________ )
       | |                      ||
       | |          @@@@        ||            @@@@
       | |        @@@@@@@       ||          @@@@@@@
       | |         @@ - -       ||          - @@@@
       | |          @  c/       ||         '_ @@@
       | |        _@| |_        ||         __\@ \@
       | |       ( \ )/_\ /_    ||  _\\  (/ ) @\_/)
       | |        \ \|) / \)    ||   |(__/ /     /|
       | |        |\_/ ( -/     ||    \___/ ----/_|
       | |        /     \       ||       ,:   '(
       | |       :    _/|       ||       |:     \
       | |       :      |       ||       |:      )
       | |       :      |       ||       |:      |
       | |_______'____,_|_______||       |_____,_|
   .---('________________________)--.     |   / (
   |____          __________       _|     |  /\  )
    |___|   -o-  |       |__|  -o- |      (  \| /
    |___|   -o-  |       |__|  -o- |      |  /'=.
   b'ger|________|       |__|______|      '=>/  \
                                         /  \ /|/
                                       ,___/|
""" + GREEN)

time.sleep(0.3)

# Weight input
weight_banner = pyfiglet.figlet_format("Weight (kg):", font="small")
print(GREEN + weight_banner)
weight = float(input(GREEN + "> "))

# Height input
feet_banner = pyfiglet.figlet_format("Feet:", font="small")
print(GREEN + feet_banner)
feet = int(input(GREEN + "> "))

inch_banner = pyfiglet.figlet_format("Inch:", font="small")
print(GREEN + inch_banner)
inch = int(input(GREEN + "> "))

# Calculate BMI
height = (feet * 0.3048) + (inch * 0.0254)
bmi = weight / (height ** 2)

# Display results
height_banner = pyfiglet.figlet_format(f"Height: {height:.2f} m", font="small")
bmi_banner = pyfiglet.figlet_format(f"BMI: {bmi:.2f}", font="small")

print(GREEN + height_banner)
time.sleep(0.3)
print(GREEN + bmi_banner)
time.sleep(0.3)

# Category
if bmi < 18.5:
    print(GREEN + pyfiglet.figlet_format("Underweight", font="small"))
elif 18.5 <= bmi <= 24.9:
    print(GREEN + pyfiglet.figlet_format("Normal weight", font="small"))
elif 25 <= bmi <= 29.9:
    print(GREEN + pyfiglet.figlet_format("Overweight", font="small"))
else:
    print(GREEN + pyfiglet.figlet_format("Obese", font="small"))
