from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lçsSAJFD87kjfs9s8'

    return app