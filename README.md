# API Assignment 

 ## Executing the Tests:

- Make sure you have Python and the required libraries (requests and pytest) installed on your system.
- Download or create the API testing framework structure as described in the previous responses.
- Navigate to the root directory of your API testing framework using a terminal.
- Run the tests by executing the main.py file: python main.py
- The tests will run, and the terminal will display the test results, including passed and failed tests.


## Details of Tools and Frameworks Used:
Programming Language: Python

Testing Framework: pytest

HTTP Library: requests

## Assumptions Made While Developing the Test Cases:

- API Authentication: The assignment does not explicitly mention API authentication. The assumption is that the API does not require authentication, or authentication details (e.g., API tokens, usernames, passwords) are provided in the API requests.

- Data Generation: The test scripts assume that the data used for creating, updating, and deleting bookings are generated within the scripts.

- Test Data Isolation: Each test script creates its own booking(s) and does not rely on the existence of previous bookings. This assumption ensures test data isolation and prevents dependencies between tests.

- Static Base URL: The base URL of the API (https://restful-booker.herokuapp.com) is hardcoded in the APIHelpers class.

