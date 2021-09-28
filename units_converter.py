
#some history
print("Hello! This is a humorous unit converter that converts from the \"Potrzebie System of Weights and Measures\" \ndeveloped by 19-year-old Donald E. Knuth, later a famed computer scientist, \ninto the metric system units and vice versa. According to Knuth, \nthe basis of this new revolutionary system is the potrzebie, \nwhich equals the thickness of Mad issue 26, or 2.263348517438173216473 mm. \nYou can visit https://en.wikipedia.org/wiki/List_of_humorous_units_of_measurement#Potrzebie for more information")

table_request = input("Do you want to see the Potrzebie table of units? (yes/no): ")
if table_request == "yes":
    print("\n1 potrzebie = 2.2633 mm \n1 Furshlugginer potrzebie = 2.2633 km \n1 cm = 4.4182 potrzebie \n1 km = 0.44182 Fur-potrzebie \n1 wood = 144 minutes \n1 kovac = 0.864 seconds \n1 year = 3.6524 Cowznofskis \n1 watt = 3.499651 Whatmeworries")

units_check_list = ["year", "month", "day", "hour", "minute", "second", "km", "m", "cm", "mm", "W"]
while True:

    print("You can convert time (y, w, d, h, min, s), length (km, m, cm, mm), and power (W). \nPlease enter the decimal number you want to convert, then whitespace, and then unit how it was shown in the previous sentence.")
    #check if there is a whitespace
    try:
        num, unit = input("number unit").split(' ')
    except:
        print("looks like you forgot about the whitespace")
        continue
    #check if number is decimal
    try:
        num = float(num)
    except:
        print("looks like your number is not decimal")
        continue

    outer_unit = 0
    if unit in units_check_list:
        if unit == "y":
            print("%s y = %d clarke (cl)" % (num, num))
        elif unit == "w":
            print("%s w = %d kovac (kv)" % (num, num * 1.918))
        elif unit == "d":
            print("%s d = %d kovac (kv)" % (num, num * 0.274))
        elif unit == "h":
            print("%s h = %d wolverton (wl)" % (num, num * 11.415))
        elif unit == "min":
            print("%s min = %d wolverton (wl)" % (num, num * 0.19))
        elif unit == "s":
            print("%s s = %d wolverton (wl)" % (num, num * 0.0032))
        elif unit == "km":
            print("%s km = %d Fur-potrzebie" % (num, num * 0.44182))
        elif unit == "m":
            print("%s m = %d Fur-potrzebie" % (num, num * 441.82))
        elif unit == "cm":
            print("%s cm = %d potrzebie" % (num, num * 4.4182))
        elif unit == "mm":
            print("%s mm = %d centipotrzebie" % (num, num * 4.4182))
        elif unit == "W":
            print("%s W = %d Whatmeworries" % (num, num * 3.499651))
    else:
        print("looks like the unit is not the one i can convert from")

