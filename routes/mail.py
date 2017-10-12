from . import *
from app import app
from flask_mail import Mail, Message
import config

main = Blueprint('mail', __name__)


# 邮件配置
app.config.update(
    DEBUG=config.DEBUG,
    MAIL_SERVER=config.MAIL_SERVER,
    MAIL_PORT=config.MAIL_PORT,
    MAIL_USE_TLS=config.MAIL_USE_TLS,
    MAIL_USE_SSL=config.MAIL_USE_SSL,
    MAIL_USERNAME=config.MAIL_USERNAME,
    MAIL_PASSWORD=config.MAIL_PASSWORD,
)


mail = Mail(app)


@main.route('/mail', methods=['POST'])
def send():
    form = request.form
    title = ' An Email from {} / phoneNumber: {} /email: {}'.format(
        form.get('name'), form.get('phone'), form.get('mail'))

    msg = Message(title, sender=config.MAIL_USERNAME, recipients=[config.MAIL_USERNAME])
    msg.body = form.get('message')
    mail.send(msg)
    return 'Successfully Sent!'
