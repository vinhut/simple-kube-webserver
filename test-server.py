from flask import Flask, escape, request, render_template, redirect, url_for

import random

app = Flask(__name__)
app.config['DEBUG'] = True

num = random.randint(1, 10)

@app.route('/')
def home():
     return "Hello World! "+str(num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
