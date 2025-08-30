# Colors
GREEN = "\033[92m"

# Banner
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
   b'ger|________|       |__|______|     '=>/  \
                                         /  \ /|/
                                       ,___/|

""")

# BMI Calculator start
weight = float(input(GREEN + "Weight (kg): "))
feet = int(input(GREEN + "Height (feet): "))
inch = int(input(GREEN + "Then inches: "))

height = (feet * 0.3048) + (inch * 0.0254)
bmi = weight / (height ** 2)

print(GREEN + f"\nHeight: {height:.2f} m")
print(GREEN + f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print(GREEN + "Underweight")
elif 18.5 <= bmi <= 24.9:
    print(GREEN + "Normal weight")
elif 25 <= bmi <= 29.9:
    print(GREEN + "Overweight")
else:
    print(GREEN + "Obese")
