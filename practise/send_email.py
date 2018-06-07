from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    
    name , addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))


def sendemail(email,content):
    
    
    print("this send",email,content)
    from_addr = "18591785265@163.com"

    # 你的授权码，注意了，大写的注意，不是你邮箱的登录密码，是授权码
    password = 'QW1234'

    # 你要发送到的邮箱
    to_addr = email 


    # 163 的 smtp 服务器
    smtp_server = 'smtp.163.com'

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr("郁金香<%s>"%from_addr)
    msg['To'] = _format_addr("我的兄弟<%s>"%to_addr)
    msg['Subject'] = Header('业务招聘', 'utf-8')

    # 连接服务器，163的smtp端口号，为25
    server = smtplib.SMTP(smtp_server, 25)

    server.set_debuglevel(1)

    # 登录邮箱
    server.login(from_addr, password)

    # 发送邮件
    server.sendmail(from_addr, [to_addr], msg.as_string())

    # 退出服务器
    server.quit()
