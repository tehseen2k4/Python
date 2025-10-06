locations = ["A", "B"]
status = ["dirty", "dirty"] 

def getStatus(location):
    
    if location in locations:
        index = locations.index(location)
        if status[index] == "dirty":
            print(f" {location} found dirty so i cleaned it up.")
            status[index]="clean"
            return "suck"
        else:
            
            if location == "A":
                return "right"
            elif location == "B":
                return "left"
    else:
        return "do nothing"
while(1):
    location = input("Enter Location (A/B): ").strip().upper()
    action = getStatus(location)
    print("Action performed: ", action)
    if action == "do nothing":
        print("Invalid location. Please enter A or B.")
    elif action == "suck":
        print(f"Location {location} is now clean.")
    else:
        print(f"Moving {action} from location {location}.")