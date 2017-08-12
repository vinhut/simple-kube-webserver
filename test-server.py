from flask import Flask, escape, request, render_template, redirect, url_for

import random
import hashlib, binascii
import string

app = Flask(__name__)
app.config['DEBUG'] = True

num = random.randint(1, 10)

@app.route('/')
def home():
     passwd = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))
     salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
     dk = hashlib.pbkdf2_hmac('sha256', passwd.encode(), salt.encode(), 100000)
     hash = binascii.hexlify(dk)
     return "Green "+str(num)+" "+hash.decode()

@app.route('/health')
def health():
     return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
