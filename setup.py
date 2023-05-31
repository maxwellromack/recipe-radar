from setuptools import setup

setup(
    name = 'Recipe-Radar-API',
    version = '0.1.1',
    description = 'Backend API for CS 321 project at George Mason University',
    author = 'Maxwell Romack',
    url = 'https://github.com/maxwellromack/recipe_radar',
    packages = ['backend'],
    install_requires = [
        'Flask',
    ],
)
