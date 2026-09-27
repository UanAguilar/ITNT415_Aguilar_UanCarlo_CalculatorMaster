# ITNT415_Aguilar_UanCarlo_CalculatorMaster

> UAN CARLO AGUILAR

> BIT41

> Python-based calculator developed using GitHub and GitHub branching.

> Branch Structure
  * main: Core branch containing the final calculator script.
  * addition_aguilar: Feature branch dedicated to addition implementation.
  * subtraction_aguilar: Feature branch dedicated to subtraction implementation.
  * multiplication_aguilar: Feature branch dedicated to multiplication implementation.
  * division_aguilar: Feature branch dedicated to division implementation with zero-division handling.

> Program Features
  * Interactive Menu: A clean loop-based interface allowing users to choose operations (1-5) or exit.
  * Basic Arithmetic: Supports Addition, Subtraction, Multiplication, and Division.
  * Error Handling: 
      ** Validates numeric input to catch ValueError exceptions if strings or letters are entered.
      ** Prevents runtime crashes by checking for division-by-zero errors.
    
> Sample Execution

--- Python Calculator ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter choice (1-5): 4
Enter first number: 10
Enter second number: 0
Result: 10.0 / 0.0 = Error: Division by zero is not allowed.
