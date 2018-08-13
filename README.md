# TicTacToe

### Intro

Play TicTacToe with a server!

### Dev Tools

The API has been developed using the following tools:
* [Python 3.6.1](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Flask_Restful](http://flask-restful.readthedocs.io/en/stable/)

### Installation

> Clone this repo to your local machine: Open terminal in any folder and type:
```
git clone https://github.com/peterpaints/bl.git
```

> Create a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) on your machine and install the dependencies via:
```
pip install -r requirements.txt`
```

> Activate the virtualenv like so:
```
source virtualenv/bin/activate
```

> Finally, start the app!
```
python run.py
```

> You should see this in your terminal:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### The Endpoints

You can play around with the API by:
* Using [`Postman`](https://www.getpostman.com/)
* Using [`Curl`](https://curl.haxx.se/)

Here are the endpoints:

| URL Endpoint | HTTP Methods | Action |
| -------- | ------------- | --------- |
| `/board="   x      "` | `POST`  | Play a new game|

Provide a board with nine characters, which may be either `x`, `o` or a space ` `
