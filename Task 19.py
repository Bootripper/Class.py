user=input("enter traffic light colour: ")
match user.lower():
    case "red":
        print("Stop! The light is red")
    case "yellow":
        print("Slow down! The light is yellow")
    case "green":
        print("Go! The light is green")
    case _:
        print("Select Green, Red, Green")
    
