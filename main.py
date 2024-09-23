def calculatePercentage(percent, value):
    product =  (percent/100) * value 
    return product


def get_category_info():
    ask_category = int(input("How many categories would you like? "))
    if ask_category < 1:
        print("Enter a valid number.")
        return
    categoryArray = []
    i = 1
    while i<= ask_category:
        categoryName = input(f"{i} : What would your name this category? ")
        categoryArray.append(categoryName)
        i += 1
    return categoryArray

def percentageValidator(Sumpercent):
    if Sumpercent > 100:
        return False
    elif Sumpercent < 100: 
        return False
    else:
        return True
    
def main(): 
    salary = int(input("Enter your salary: "))
    if salary < 0 :
        print("Enter a valid number")
        return
    
    categoryArray = get_category_info()
    output = {}
    sumPercent = 0
    for category in categoryArray:
        askPercentage = int(input(f"How much percent would you like to dedicate for {category}? "))
        sumPercent = sumPercent + askPercentage
        percentageValidator(sumPercent) 
        output[category] = calculatePercentage(askPercentage, salary)

    if percentageValidator(sumPercent) is False:
        print("Please make sure that your percentage adds up to 100")
    else:
        for category, value in output.items():
            print(f"Your budgeted amount for {category} is {value}")

if __name__ == "__main__":
    main()     
