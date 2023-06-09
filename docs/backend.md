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


### /logout

URL: '/auth/logout'    
Request Type: GET

Clears the current session, logging out the user.

Returns status code 200 for a successful logout.

## /user

The '/user' prefix is used for updating entries in the user table that is not related to authentication

### /add

URL: '/user/add'    
Request Type: POST

The add endpoint takes a JSON payload containing an user-inputted text string that will be added to the user's ingredients, given that the input is valid.

Example Payload:
```
payload = {
    'input': 'butter'
}
```

Returns status code 400 if no input is passed in the payload, any non-alphabetic characters are included, or a match is not found. 
Returns status code 201 for a successful addition.

### /rec

The '/rec' prefix is used for anything relating to the recipe recommendation system.

### /update

URL: '/rec/update'    
Request Type: GET


The update endpoint updates the recommended recipes and should be run every time that the user accesses the page of recipes. The JSON payload that is returned will have a field 'recipes' that contains a string of recipe ids, separated by spaces in descending order by how much of a match the recipe is to the user's ingredients.

Returns status code 400 if user ingredients are not set.
Returns status code 200 if recommendation system ran successfully.
