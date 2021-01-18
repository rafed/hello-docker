from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now() # current date and time

    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    return {
        "date": date,
        "time": time
    }

app.run(host='0.0.0.0', port=8000)
