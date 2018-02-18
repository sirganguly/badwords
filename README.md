#### BUILD INSTRUCTIONS
* Fork repo
* Install python 2.7.13, pip and virtualenv (google for how-to's)
* cd into project dir and create a virtual environment:
    ```$ virtualenv env```
* Activate the virtual environment
   ```$ source env/bin/activate``` on macOS and Linux,
    ```$ env\Scripts\activate``` on Windows
* Install python packages (virtual environment should be activated)
    ```$ pip install -r requirements.txt```
* Now run the app.py script
  ```(env)$ python app.py```
* Open http://localhost:8080 on your browser
* ```deactivate``` virtual environment when done

#### Directory structure
* ```templates```: contains HTML files
* ```static```: contains sub-folders for javascript, css and image files
* ```uploads```: for temporary file uploads (better to use S3 for permanent storage)

#### Important files
* ```app.py```: contains server side code responsible for serving HTML files and hosts the API (backend logic). Once we host this app on Heroku, the TG bot can call this API for data
* ```_config.py```: contains configuration information like app secret key, database location and other metadata required for flask to render the web app
* ```models.py```: contains the definition of the database model for SQLAlchemy to consume
* ```Procfile```: Information required by heroku to deploy the app on the cloud
* ```requirements.txt```: list of python packages required. Every time you need to install a new package with pip, run ```pip freeze > requirements.txt``` to save the current state of required packages
* ```.gitignore```: files and file extensions which shouldn't be on github (like .pyc files and your virtualenv folder)

#### NOTE
* Do a ```git pull``` everytime ```master``` branch is updated to keep your local copy of the project up to date

#### TODO
- ~~Understand/explain directory structure, what package does what and what file does what~~
- Explain flask app flow
- List of simple technologies to learn to wrap this app up
- [Flask reference](http://flask.pocoo.org/docs/0.12/)

#### Bot handle and heroku details
Bot's telegram handle is gaalibot and is currently hosted on heroku here: https://thegalibot.herokuapp.com/