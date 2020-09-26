from flask import Flask

from server.routes import user, mail

app = Flask(__name__)

print("\033[93m" + "server/__init__.py " + "Initializing the server instance and registering blueprints" + "\033[0m")
app.register_blueprint(user.userRoutes, url_prefix="/user")
app.register_blueprint(mail.mailRoutes, url_prefix="/mail")

print("\033[93m" + "=========== Try to visit localhost:8080/mail/ with HTTP GET and POST method =========== " + "\033[0m")
app.run(host="127.0.0.1", port=8081, debug=True)