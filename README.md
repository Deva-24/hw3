# Home work 3
# Calculator Project

This is a simple calculator project implemented in Python. The calculator can perform basic arithmetic operations: addition, subtraction, multiplication, and division. It also maintains a history of calculations and includes error handling for division by zero.

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- Store a history of calculations
- Retrieve the last calculation
- 100% test coverage with pytest
- Code linted using pylint

## Requirements

- Python 3.7 or higher

## Setup Instructions

### 1. Clone the Repository

To get started, clone this repository to your local machine:

## bash command
git clone https://github.com/your-username/python-calculator.git

### 2. Navigate to the Project Directory
Change your current working directory to the project folder:

## bash command
cd python-calculator

### 3. Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies:

## bash command
python -m venv venv
Activate the virtual environment:

1.On Windows:
venv\Scripts\activate

2.On macOS/Linux:
source venv/bin/activate

### 4. Install Required Dependencies
Install the required packages using pip:

### bash command
pip install -r requirements.txt


### pylint & pytest
Check Test Coverage
To check the test coverage, use the following command:
## bash command
pytest --cov=calculator --cov-report=term-missing
Code Linting
To check the code quality, you can run pylint:

###  bash
pylint calculator.py

### Contribution
Feel free to fork the repository and submit pull requests. Your contributions are welcome!

### Notes:
Let me know if you need any modifications or additional information!
