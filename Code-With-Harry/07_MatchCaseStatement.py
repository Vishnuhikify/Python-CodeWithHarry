# Match case statement : It's just like swiitch statement ins Js

a = input("Enter day : ")

match a:
    case "Monday":
        print("It's Mondayyy!!")
    case "Tuesday":
        print("It's Tuesdayyy!!")
    case "Wednesday":
        print("It's Wednesdayyy!!")
    case "Thursday":
        print("It's Thursdayyy!!") 
    case "Friday":
        print("It's Fridayyy!!")
    case "Saturday":
        print("It's Saturdayyy!!")
    case "Sunday":
        print("It's Sundayyy!!")
    case _:
        print("No match found")   