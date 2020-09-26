from flask import Flask

from server.routes import user

app = Flask(__name__)

app.register_blueprint(user.userRoutes, url_prefix="/user")

app.run(host="127.0.0.1", port=8081, debug=True)
