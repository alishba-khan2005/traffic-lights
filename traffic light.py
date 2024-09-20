    #TRAFFIC LIGHT:
traffic_light=str(input("enter colour of light: "))
if traffic_light=="red":
    print("car has to  stop: ")
elif traffic_light=="yellow":
    print("car has to wait: ")
elif traffic_light=="green":
    print("car is allowe dto go:")
else:
    print("unrecognized signal")
    