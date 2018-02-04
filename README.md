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
* Open http://localhost:5000 on your browser
* ```deactivate``` virtual environment when dne

#### TODO
- Understand/explain directory structure, what package does what and what file does what
- [Flask reference](http://flask.pocoo.org/docs/0.12/)