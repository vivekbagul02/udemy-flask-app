import json
import os

from flask import Flask, render_template

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'), verbose=True)

app = Flask(__name__)

app.config.from_mapping(SECRET_KEY=os.environ['SECRET_KEY'])

@app.route('/')
def index():
    instance_id = 'Unknown'
    try:
        response = requests.get('http://169.254.169.254/latest/meta-data/instance-id/', timeout=3)
        instance_id = response.content.decode('utf-8')
    except:
        pass

    return render_template('index.html', instance_id=instance_id)
