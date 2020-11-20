# Ukufu Lunch App

## Features:
	- Flask as a micro framework in order to serve application api
	- Redirection from root to /lunch endpoint added.
	- Empty recipe case handled gracefully.
	- App main logic is very concie and uses Python built-in Set library for efficiency.
	- Python unittest library is used for integeration testing.
	- Jinja 2 template is used to prettify back-end returned result.
	- Dockerfile is added for quick reproduction of the app.

## How to run:
	Dockerfile:
		```sh
		$ git clone https://github.com/ampbj/jadidi-ryan-techtask-201120.git
		$ cd jadidi-ryan-techtask-201120
		$ docker build -t ukufu-lunch-app .
		$ docker run -p 5000:5000 -d ukufu-lunch-app
		```
		Go to http://localhost:5000/lunch