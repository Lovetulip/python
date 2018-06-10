import send_email

import re
import werobot
from werobot.replies import ArticlesReply, Article
from werobot import WeRoBot 

# token 换成你的微信后台 token 值
robot = werobot.WeRoBot(token='4010')

#自定义菜单
#robot                      = WeRoBot()
#robot.config["APP_ID"]     = "wx66721fb351d82d01"
#robot.config["APP_SECRET"] = "d700d403a8ee63bc90f1efd468570a60"

#client = robot.client
#创建自定义菜单

#client.create_menu({
#    "button":[{
#        "type":"click",
#        "name":"今日歌曲",
#        "key" :"music"
#
#            }]
#                    })
@robot.key_click("music")
def music(message):
    return "你点了一首歌"


@robot.handler
def welcome(message):
    return "hello world"
@robot.image
def echo(message):
    reply = ArticlesReply(message=message)
    article = Article(
            title = "Learn by doing",
            description = "相信自己",
            img="http://img.taopic.com/uploads/allimg/120727/201995-120HG1030762.jpg",
            url="https://www.baidu.com/"

            )

    reply.add_article(article)
    return reply






@robot.text
def sendEmail(message):

    usermessage = message.content

    #得到用户的邮箱
    email       = re.search("\w.*.com",usermessage)
    if email:
        email       = str(email.group())
        #得到用户想发的内容，规定格式为：发邮件到XXXXXX@.com，内容叉叉叉，这个是为了找到 .con 的索引
        index       = usermessage.find("com")
        # [index+4:] 其中，index+4代表 'com,' 这四个字符串，也就是说，这四个字符串后面开始算是内容

        content     = str(usermessage[index+4:])
        if email[:4] == "我的邮箱":
            try :
                    
                #因为不会用正则匹配出文字中的邮箱，所以设置成第五个字符开始
                send_email.sendemail(email[4:],content)
            except:
                return "发送失败"
            return "发送成功"
        else:
            return("请输入‘我的邮箱’‘email地址’以逗号分隔发送内容")
    else:
    # 非发邮件状态下，返回的文字
        return "this is tulip"

robot.run(host='127.0.0.1',port=80)
