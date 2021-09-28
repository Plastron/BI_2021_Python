
#some history
print("Hello! This is a humorous unit converter that converts from the \"Potrzebie System of Weights and Measures\" \ndeveloped by 19-year-old Donald E. Knuth, later a famed computer scientist, \ninto the metric system units and vice versa. According to Knuth, \nthe basis of this new revolutionary system is the potrzebie, \nwhich equals the thickness of Mad issue 26, or 2.263348517438173216473 mm. \nYou can visit https://en.wikipedia.org/wiki/List_of_humorous_units_of_measurement#Potrzebie for more information")

#the table from https://polaris93.livejournal.com/2046896.html
table_request = input("Do you want to see the Potrzebie table of units? (yes/no): ")
if table_request == "yes":
    print("\n1 potrzebie = 2.2633 mm \n1 Furshlugginer potrzebie = 2.2633 km \n1 cm = 4.4182 potrzebie \n1 km = 0.44182 Fur-potrzebie \n1 wood = 144 minutes \n1 kovac = 0.864 seconds \n1 year = 3.6524 Cowznofskis \n1 watt = 3.499651 Whatmeworries")

units_check_list = ["year", "month", "day", "hour", "minute", "second", "km", "m", "cm", "mm", "W"]


while True:
    print("You can convert time (y, w, d, h, m, s), length (km, m, cm, mm), and power (W). \nPlease enter the decimal number you want to convert, then whitespace, and then unit how it was shown in the previous sentence.")
    #check if there are two separate variables in the input
    try:
        value, unit = input("number unit").split(' ')
    except:
        print("looks like you forgot about the whitespace")
        continue

    #check if the first value is a number
    try:
        value = int(value)
    except:
        print("looks like your number is not decimal")
        continue

    outer_unit = 0
    if unit in units_check_list:

if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "ft" and unit2 == "cm":
    ans = float(num1)*30.48
    print(ans)
elif unit1 == "ft" and unit2 == "mm":
    ans = float(num1)*304.8
    print(ans)
elif unit1 == "ft" and unit2 == "inch":
    ans = float(num1)*12
    print(ans)
elif unit1 == "inch" and unit2 == "cm":
    ans = float(num1)*2.54
elif unit1 == "inch" and unit2 == "mm":
    ans = float(num1)*25.4
    else:
        print("looks like the unit is not the one i can convert from")

