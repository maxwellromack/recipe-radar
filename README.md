# Recipe Radar

## Description

WIP

## Getting Started

### Dependencies

* [Flask](https://pypi.org/project/Flask/)
* Recipe-Radar-API (Included)

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

For adding recipes to the database, execute the following command inside of the project folder, also in a seperate terminal window:
```
flask --app backend add-recipes
```

## Authors

* Maxwell Romack
* Saurabh Khanal
* Laiba Farhan
* Tanni Barua

## Version History

* 0.1
  *  Initial release

## Acknowledgments

* Recipes used in project are from [archive.org](https://archive.org/details/cooking-recipes)
