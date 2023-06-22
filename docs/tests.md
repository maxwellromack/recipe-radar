# Testing Documentation

## AuthActions

The AuthActions in the test configuration provides two functions that make running tests that involve user accounts easy! To use AuthActions in a test, simply include 'auth' in the function parameters like so:
```
def test_example(auth):
```

### auth.register()

Registers a user account with the following username and password:

Username: guitarhero    
Password: jimihen

In the testing app environment, the user ID for this account is '3'.

### auth.login()

Logs into the testing app environment using the username and password registered in 'auth.register()', which **must** be run before calling 'auth.login()'!
