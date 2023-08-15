# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Pashvi" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    return "Hi Dad, here's a little about me."

# define the route to mother webpage
@app.route("/mother")
def father():
    return "Hi Mom, here's a little about me."

# define the route to friends webpage
@app.route("/friend")
def father():
    return "Hi friend, here's a little about me."

# add other routes, if you want


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
