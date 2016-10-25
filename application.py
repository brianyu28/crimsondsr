from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Crimson Daily Story Report'

if __name__ == "__main__":
    port = int(os.envion.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

