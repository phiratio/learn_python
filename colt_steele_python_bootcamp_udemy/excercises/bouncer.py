# ask for age
# 18-21 wristband
# 21+ normal entry
# too young
import sys

try:
    age = int(input("How old are ya lad?"))
except:
    print("Valid numbers please!")
    sys.exit()
print(age)
if age >= 21:
    print('cul')
elif age >= 18:
    print('cul')
else:
    print('get lost lad')
