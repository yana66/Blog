from . import *
from models.mail import MailMessage
from flask import jsonify
import config
import smtplib
from email.mime.text import MIMEText

main = Blueprint('mail', __name__)


# 邮件配置
# 设置服务器所需信息
# qq邮箱服务器地址
mail_host = config.MAIL_SERVER
# 163用户名
mail_user = config.MAIL_USERNAME
# 密码(第三方登录授权码)
mail_pass = config.MAIL_PASSWORD
# 邮件发送方邮箱地址
sender = config.MAIL_USERNAME
# 邮件接收方邮箱地址列表
receivers = [config.MAIL_RECIEVER]


def mail(form):
    ret = True
    # 设置email信息
    # 邮件内容设置
    # 三个参数: 第一个为文本内容, 第二个文本格式, 第三个编码
    message = MIMEText(form.get('message'), 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'WATERCODE WEBSITE Email from {}, phoneNumber: {}, email: {}'.format(
        form.get('name'), form.get('phone'), form.get('email'))
    # 发送方信息
    message['From'] = sender
    # 接收方信息
    message['To'] = sender
    try:
        # 登录并发送邮件
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
    except Exception:
        ret = False
    return ret


@main.route('/mail', methods=['POST'])
def send():
    form = request.json
    ret = mail(form)
    if ret:
        print('successfully sent')
        MailMessage.new(form)
    else:
        print('发送失败')

    return jsonify()
