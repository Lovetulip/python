from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def _format_addr(s):
    
    name , addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))


def sendemail(email,content,attach):
    # 你的邮箱
    from_addr = '18591785265@163.com' 

    # 你的授权码，注意了，大写的注意，不是你邮箱的登录密码，是授权码
    password = 'QW1234'

    # 你要发送到的邮箱
    to_addr = email
    print("test",email,content)
    # 163 的 smtp 服务器
    smtp_server = 'smtp.163.com'
    #对于邮件中包含多个元素必须要添加下面语句
    msg = MIMEMultipart()
    #msg = MIMEText(content, 'plain', 'utf-8')
    #下面三条是构造邮件的发送标题
    msg['From'] = _format_addr("郁金香<%s>"%from_addr)
    msg['To'] = _format_addr("我的兄弟<%s>"%to_addr)
    msg['Subject'] = Header('人丑就要多读书', 'utf-8')
    #邮件的正文部分
    eml_content = MIMEText(content)
    msg.attach(eml_content)

    #发送文本附件(其他文件类似，只是读取相应的名字，录音，视频除外)
    eml_attach = MIMEApplication(open(attach, 'rb').read())
    eml_attach.add_header('Content-Disposition', 'attachment', filename='rty.py')
    msg.attach(eml_attach)
    
    
    # 连接服务器，163的smtp端口号，为25
    server = smtplib.SMTP(smtp_server, 25)

    server.set_debuglevel(1)

    # 登录邮箱
    server.login(from_addr, password)

    # 发送邮件
    try:
        server.sendmail(from_addr, to_addr, msg.as_string())
    except Exception as e:
        print(e)
    # 退出服务器
    server.quit()
if __name__ == "__main__":
    eml     = "401022627@qq.com"
    content = "这是不是最新的文章？"
    attach  = "/home/tulip/wenxuecheng/直把人生付戏中（七）.txt"
    sendemail(eml,content,attach)
