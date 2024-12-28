from flask import Flask
from scripts.models import init_app

app = Flask(__name__)

# ...existing code...

init_app(app)

if __name__ == '__main__':
    app.run()
