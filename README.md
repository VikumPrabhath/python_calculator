# Simple Calculator - Python

A lightweight command-line calculator application built with Python that performs basic arithmetic operations with error handling capabilities.


## Features

- **Basic Arithmetic Operations**:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Power (^)
  - Remainder (%)
  
- **Error Handling**:
  - Division by zero protection
  - Modulo by zero protection
  - Invalid input validation
  - Exception handling for unexpected errors

- **User-Friendly Interface**:
  - Interactive menu-driven system
  - Reset functionality ($)
  - Program termination (#)
  - Continuous operation until explicit termination


## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/VikumPrabhath/python_calculator.git
```
**2. Navigate to the project directory:**
```bash
cd python_calculator
```


## Usage

**Run the calculator:**
```bash
python Simple_Calculator.py
```


## Operation Guide

**1. Select an operation from the menu:**
- `+` for Addition
- `-` for Subtraction
- `*` for Multiplication
- `/` for Division
- `^` for Power
- `%` for Remainder
- `#` to Terminate the program
- `$` to Reset the current operation

**2. Enter numbers when prompted**

**3. View the result**

**4. Continue with new operations or terminate with `#`**


## Example Session
```bash
Select operation.
1.Add      : + 
2.Subtract : - 
3.Multiply : * 
4.Divide   : / 
5.Power    : ^ 
6.Remainder: % 
7.Terminate: # 
8.Reset    : $ 

Enter choice(+,-,*,/,^,%,#,$): +
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
```



## Code Structure
- add(a, b): Performs addition
- subtract(a, b): Performs subtraction
- multiply(a, b): Performs multiplication
- divide(a, b): Performs division with zero division check
- power(a, b): Calculates power
- remainder(a, b): Calculates remainder with zero division check
- select_op(choice): Main operation handler with input validation



## Error Handling

The calculator gracefully handles:

- Invalid mathematical operations
- Non-numeric inputs
- Division by zero scenarios
- Unexpected exceptions



## Requirements

- Python 3.x
- No external dependencies


 
## Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request



## License

This project is licensed under the MIT License - see the LICENSE file for details.



## Author

**Vikum Prabhath**
- GitHub: @VikumPrabhath

