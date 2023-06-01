# Backend Documentation

## /auth

The '/auth' prefix is used for every API endpoint that deals with user account creation or login.

### /register

URL : '/auth/register'    
Request Type: POST

The register endpoint takes a JSON payload containing a username and password and creates a new user account if the user is not already registered. Both the username and the password are required.

Example Payload:
```
payload = {
        'username': 'freeman',
        'password': 'blackMesa1998'
    }
```

Returns status code 400 if the username or password is missing from the request, or if the username is already registered with an account. Returns status code 201 for a successful registration.
