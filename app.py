from flask import Flask
from flask_mail import Mail, Message
import time
import config
from routes import current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = config.secret_key


from routes.blog import main as home_routes
from routes.mail import main as mail_routes
app.register_blueprint(home_routes)
app.register_blueprint(mail_routes)


@app.template_filter('timeformat')
def timeformat(value, format='%d/%m/%Y'):
    x = time.localtime(value)
    return time.strftime(format, x)


@app.context_processor
def inject_user():
    user = current_user()
    return dict(user=user)


if __name__ == '__main__':
    app.run(debug=True)