from flask import Flask

app = Flask(__name__)

# You can perform additional setup or imports here if needed
# For example, you might import routes or configure extensions.

# Import your routes to make them accessible
from app import route
