# Intentionally Vulnerable Python Code - SQL Injection

def login(username, password):
    # This is a simple example vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # Imagine executing the query against a database, but here we'll just print it
    print("Executing query:", query)

# User input (simulating input from a form)
user_input_username = "admin' OR '1'='1' --"
user_input_password = "password123"

# Calling the login function with user input
login(user_input_username, user_input_password)


var datadogAPIKey= "38339db033691fcadda4984f5d1acb5a"