def going_to_movies():
    age = eval(input("How old are you?: "))
    weather = input("what's the weather like?: ")
    if age < 10:
        price = 0
    if age < 15 and age >= 10:
        price = 5
    if age >= 15 and age <= 18:
        price = 7
    else:
        price = 12
    if weather.lower() == "rainy":
        if price == 0:
            return price
        else:
            return(price-2)
    if weather.lower() == "sunny":
        return(price+2)
    if weather.lower() == "hailing":
        return("everybody free!")
    if weather.lower() == "snowing":
        price += 1.50
        return(price)
    else:
        return(price)
    
    
