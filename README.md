# Budget Allocation Program

## Description
This Python program helps users allocate their salary into different budget categories based on specified percentages. The program takes the user's salary and divides it among custom categories, ensuring that the total percentage adds up to 100%. If the percentage exceeds or falls short of 100%, the user is prompted to correct the input.

## Features
- **Custom Budget Categories**: Users can create multiple budget categories with unique names.
- **Salary Allocation**: Allocates a percentage of the salary to each category.
- **Validation**: Ensures the sum of the percentages equals 100%, otherwise prompts the user to adjust their inputs.
- **Output**: Displays the allocated budget for each category.

## Functions

### `calculatePercentage(percent, value)`
- **Input**: `percent` (percentage to allocate), `value` (the total salary).
- **Output**: Returns the calculated product of the given percentage and salary.

### `get_category_info()`
- **Input**: Asks the user for the number of categories and their names.
- **Output**: Returns a list of category names.

### `percentageValidator(Sumpercent)`
- **Input**: `Sumpercent` (total percentage).
- **Output**: Returns `True` if the sum is exactly 100, otherwise `False`.

### `main()`
- Handles the main workflow:
  - Asks for the salary and validates it.
  - Prompts for budget categories and their percentage allocations.
  - Validates the total percentage and displays the allocated budget for each category.

## Usage
1. Run the program.
2. Input your salary.
3. Define how many budget categories you'd like to create.
4. Name each category.
5. Assign a percentage of your salary to each category (the sum should equal 100%).
6. The program will calculate and display how much of your salary is allocated to each category.

## Example
```
Enter your salary: 5000
How many categories would you like? 2
1 : What would you name this category? Rent
2 : What would you name this category? Food
How much percent would you like to dedicate for Rent? 50
How much percent would you like to dedicate for Food? 50
Your budgeted amount for Rent is 2500.0
Your budgeted amount for Food is 2500.0
```

## Requirements
- Python 3.x

## Notes
- Ensure that the sum of percentages equals exactly 100%, or the program will prompt you to adjust it.
- Enter a valid salary (greater than 0).

## License
This project is free to use and modify.