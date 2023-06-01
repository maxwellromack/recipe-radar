# Backend Documentation

## /auth

The '/auth' prefix is used for every API endpoint that deals with user account creation or login.

### /register

URL: '/auth/register'    
Request Type: POST

The register endpoint takes a JSON payload containing a username and password and creates a new user account if the user is not already registered. Both the username and the password are required.

Example Payload:
```
payload = {
        'username': 'freeman',
        'password': 'blackMesa1998'
    }
```

Returns status code 400 if the username or password is missing from the request, or if the username is already registered with an account.    
Returns status code 201 for a successful registration.


### /login

URL: '/auth/login'    
Request Type: POST

Like the register endpoint, the login endpoint also takes a JSON payload containing a username and a password. If the username is registered in the database and the password matches, the user ID is tied to the current session. 

See the '/register' documentation for an example payload.

Returns status code 400 if the username or password is incorrect.    
Returns status code 200 for a successful login.
