# User Management API Test Suite

## Description

The **User Management API Test Suite** is a comprehensive collection of automated tests designed to validate the functionality and reliability of the User Management API. This suite ensures that user creation endpoints behave as expected under various conditions, including both positive and negative scenarios. By leveraging Python's `requests` library, the tests interact with the API to verify response codes, data integrity, and error handling.

## Features

- **Positive Test Cases:**
  - Create users with valid first names (2, 15, and Latin characters).
  - Verify successful user creation and authentication token retrieval.
  - Confirm user entries in the users table.

- **Negative Test Cases:**
  - Handle invalid first names (too short, too long, special characters, numbers).
  - Ensure appropriate error responses when required parameters are missing or invalid.

## Unit Tests

A series of **unit tests** have been implemented to ensure the robustness of the User Management API. Below are the detailed test requirements and their corresponding scenarios:

1. **Allowed Number of Characters (2)**
   - **Body:**
     ```json
     {
       "firstName": "Aa",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `201 Created`
     - **Body:**
       ```json
       {
         "authToken": "generated_token_here"
       }
       ```
     - **Users Table:** Contains the passed values.

2. **Allowed Number of Characters (15)**
   - **Body:**
     ```json
     {
       "firstName": "Aaaaaaaaaaaaaaa",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `201 Created`
     - **Body:**
       ```json
       {
         "authToken": "generated_token_here"
       }
       ```
     - **Users Table:** Contains the passed values.

3. **Number of Characters Below Allowed (1)**
   - **Body:**
     ```json
     {
       "firstName": "A",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
       }
       ```

4. **Number of Characters Above Allowed (16)**
   - **Body:**
     ```json
     {
       "firstName": "Аааааааааааааааа",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
       }
       ```

5. **Spaces Not Allowed**
   - **Body:**
     ```json
     {
       "firstName": "A Aaa",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
       }
       ```

6. **Special Characters Not Allowed**
   - **Body:**
     ```json
     {
       "firstName": "№%@",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
       }
       ```

7. **Numbers Not Allowed**
   - **Body:**
     ```json
     {
       "firstName": "123",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
       }
       ```

8. **Missing `firstName` Parameter**
   - **Body:**
     ```json
     {
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "No se enviaron todos los parámetros requeridos"
       }
       ```

9. **Empty `firstName` Parameter**
   - **Body:**
     ```json
     {
       "firstName": "",
       "phone": "+1234567890",
       "address": "123 Elm Street, Hilltop"
     }
     ```
   - **Expected Response:**
     - **Status Code:** `400 Bad Request`
     - **Body:**
       ```json
       {
         "code": 400,
         "message": "No se enviaron todos los parámetros requeridos"
       }
       ```

10. **Incorrect Type for `firstName` Parameter (Number)**
    - **Body:**
      ```json
      {
        "firstName": 12,
        "phone": "+1234567890",
        "address": "123 Elm Street, Hilltop"
      }
      ```
    - **Expected Response:**
      - **Status Code:** `400 Bad Request`
      - **Body:**
        ```json
        {
          "code": 400,
          "message": "No se enviaron todos los parámetros requeridos"
        }
        ```

## Technologies Used

- **Programming Language:** Python
- **Libraries:** `requests`
- **Testing Framework:** [Pytest](https://docs.pytest.org/en/7.2.x/) (optional for running tests)
- **Version Control:** GitHub

## Prerequisites

- **Python 3.6 or higher** installed on your machine.
- **pip** package manager.
- Access to the User Management API service.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Fredy002/User-Management-API-Test-Suite.git
   cd User-Management-API-Test-Suite
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install the required library manually:*

   ```bash
   pip install requests
   ```

## Configuration

1. **Set Up Configuration**

   The `configuration.py` file contains the API service URLs. Ensure that the `URL_SERVICE`, `CREATE_USER_PATH`, and `USERS_TABLE_PATH` are correctly set to match your API endpoints.

   ```python
   # configuration.py

   URL_SERVICE = "https://your-api-service-url.com"
   CREATE_USER_PATH = "/api/v1/users/"
   USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
   ```

2. **Update Headers (If Necessary)**

   The `data.py` file includes the headers used in API requests. Modify them if your API requires different headers.

   ```python
   # data.py

   headers = {
       "Content-Type": "application/json"
   }
   ```

## Running the Tests

1. **Execute Test Scripts**

   You can run the tests using a Python interpreter. Navigate to the project directory and execute the test file.

   ```bash
   python test_user_creation.py
   ```

   *If you are using Pytest for better test management and reporting:*

   ```bash
   pytest test_user_creation.py
   ```

2. **Review Test Results**

   The tests will output the status of each assertion. Successful tests will pass silently or with a success message, while failed tests will provide detailed error messages.

## Project Structure

```
User-Management-API-Test-Suite/
├── configuration.py         # API endpoint configurations
├── data.py                  # Request headers and sample user data
├── sender_stand_request.py  # Functions to interact with the API
├── test_user_creation.py    # Unit test cases for user creation
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Contact

**GitHub:** [Fredy002](https://github.com/Fredy002)  
**LinkedIn:** [Fredy Antonio Almeyda Alania](https://www.linkedin.com/in/fredy-antonio-almeyda-alania)

Feel free to explore the code to understand how the styling is achieved and maybe tweak some values to see how the design changes. Happy coding!
