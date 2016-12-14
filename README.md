# booksearch
A book searching app for readers

[![Build Status](https://travis-ci.org/andela-ggikera/booksearch.svg?branch=master)](https://travis-ci.org/gitgik/djangular-bucketlist-app) [![Coverage Status](https://coveralls.io/repos/github/andela-ggikera/djangular-bucketlist-app/badge.svg?branch=develop)](https://coveralls.io/github/andela-ggikera/djangular-bucketlist-app?branch=develop) [![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
A Django-powered Bucketlist API with an AngularJS consumption client.

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [Bootstrap] (https://getbootstrap.com/getting-started/): Most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/gitgik/booksearch.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
            $ cd booksearch
        ```

    2. Create and fire up your virtual environment:
        ```
            $ virtualenv env
            $ source env/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```
            $ pip install -r requirements.txt```
        ```


* #### Run It
    Fire the engines using this one simple command:
        ```
            $ python manage.py makemigrations && python manage.py migrate
            $ python manage.py runserver
        ```
    You can now access the bucketlist service on your browser by using
        ```
            http://localhost:8000/
        ```
