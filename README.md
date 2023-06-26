# Recipe Radar

## Description

A web app for recommending recipes based on ingredients that a user already has in their kitchen. Created for CS 321 at George Mason University. Repository set to read-only as of 6/26/23.

## Getting Started

### Dependencies

* Python 3.8.x or newer
* [Flask](https://pypi.org/project/Flask/)
* Recipe-Radar-API (Included)
* [React](https://react.dev/)
* [Node.js](https://nodejs.org/en)
* [typed.js](https://github.com/mattboldt/typed.js/)
* [React Router](https://reactrouter.com/en/main)

### Installing

The backend API and all dependencies can be installed with the following command from inside the project folder:
```
pip install -e .
```

### Executing program

To start the Flask backend, execute the following command from inside the project folder:
```
flask --app backend run
```

To initialize the database, execute the following command in a seperate terminal window:
```
flask --app backend init-db
```

For updating recipes in the database, execute the following command inside of the project folder, also in a seperate terminal window:
```
flask --app backend update-recipes
```

## Authors

* Maxwell Romack
* Saurabh Khanal
* Laiba Farhan
* Tanni Barua

## Acknowledgments

* Recipes used in project are from [archive.org](https://archive.org/details/cooking-recipes)
