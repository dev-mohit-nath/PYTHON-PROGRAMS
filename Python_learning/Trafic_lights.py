light = input("Enter the trafic light color (rad, yellow, green): ")
print("The trafic light is",light)

if (light == "rad"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")
else:
    print("Enter a invalid light color")