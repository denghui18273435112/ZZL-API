import  requests
from utils.RequestsUtil import *
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml



class question_bank:
    def question_bank_add(self):
        url="http://192.168.1.202:8114//manageapi/testquestionbank/add"
        data = {
                      "bank_type": 1,
                      "name": "23 ",
                      "organization_id": 1}
        cookies={"safetyapplication":"o3wmzA7NrDc7vPGj38-r17r8pBKzQiNyP6bOKWAd97VkmqaGH-yy5-rNJEP7fLwBTGDbIg7v-WBTxjz473rJcpov3rg20ZH2-BgiYXIXOgODGiHOMIKWW2Jht3q1qG6BQo14U4EykpP6kyL8e7gWulpbh8iop6u7tsKSsA8FPplWUOafHUwyTpLflLr9RC5f1KgshB_cloX9F8mF8tQzr6EyqNzdKmgz3tt51anl1ESqzEC8IQNj5iM7tdopUEZZKBZb9gWdWi5NCUV8Ir43lGb3v71a8WiFFyO1HzdiTYT73VoyQIg6q-ZItEjtigv6FTg58YHYvHBQXmjjorBvfxg850lSJXvptFlO0ACI_HFHPwXxlKxdeR-SJPe1pJJOraBi9aMv0-fExIUG0XbifJ0CYZ5egimokPd4JmhnRKPdurhHydTF9nXfq3IffRtvuSwBww"}

        return   Request().post(url=url,data=data,cookies=cookies)

    def question_bank_list(self):
        url="http://192.168.1.202:8114//manageapi/testquestionbank/getlist"
        data = {
            "bank_type": 0,
            "by": "1",
            "kw": "",
            "order": "created_time",
            "organization_id": "1",
            "pageNum": 1,
            "pageSize": 2000
                     }
        cookies={"safetyapplication":"o3wmzA7NrDc7vPGj38-r17r8pBKzQiNyP6bOKWAd97VkmqaGH-yy5-rNJEP7fLwBTGDbIg7v-WBTxjz473rJcpov3rg20ZH2-BgiYXIXOgODGiHOMIKWW2Jht3q1qG6BQo14U4EykpP6kyL8e7gWulpbh8iop6u7tsKSsA8FPplWUOafHUwyTpLflLr9RC5f1KgshB_cloX9F8mF8tQzr6EyqNzdKmgz3tt51anl1ESqzEC8IQNj5iM7tdopUEZZKBZb9gWdWi5NCUV8Ir43lGb3v71a8WiFFyO1HzdiTYT73VoyQIg6q-ZItEjtigv6FTg58YHYvHBQXmjjorBvfxg850lSJXvptFlO0ACI_HFHPwXxlKxdeR-SJPe1pJJOraBi9aMv0-fExIUG0XbifJ0CYZ5egimokPd4JmhnRKPdurhHydTF9nXfq3IffRtvuSwBww"}
        res = Request().post(url=url,data=data,cookies=cookies)
        return    res["body"]["data"]

    def login(self):
        url="http://192.168.1.202:8114/manageapi/accountapi/Login"
        data = {
            "email": "admin",
            "password": "3baf6566eeaeb9f154db656002c010c6",
            "rememberme": 0,
            "verifycode": "xicheng"
        }
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                 "Cookie":"zzllgnvlc=6e9564528e1fe65c4fcef3a59b83459eg1598344327; safetyapplication=uk-mMeykPPffWKnDZ7dlsjj5dc1spatMiSDwJ9UM6726_vRNbg3l410yP8WljX77rzepI8nFxl2WU022kD38eYPihAuWaW_4yAIeGzRkt5_AjEZITIVmoaMG59_lYFjBLos6vipfdwDqDmKTguh1dlyiaZVvPxkNnaXhbrKkvUCGK414tgkJetz9pWCL2lhkGLib6ADVF-hMQJ9Y9YwEApShDB-tNtFVMgfRx335llIwev1oWBTq1BPu4GZq9rgY0rZNIYjSbAmhNNZRnYadsBAqd6qFzGQF9YNUsxQMqtw0LEV6IyF9MBz2btgUmjTUoEOl8HDJWhDwkXdzZFUTxZtu41PNMngbVahMLSo0bkh3rk-lFNDFtMd88XkNIA1iXO2SxE9dJSggumVV9f7vZZ7CGGCH8Lsi42BHuEfclvCM0XcHgONfjoQnbCM4uDWCPfY47w"
                 }
        cookies={"zzllgnvlc":"1465118dda9790923d72f2482bf016afg1598343499",
                 "safetyapplication":"wncq3H6F0o2TwQ5VvzUd8s0vC2I9QSlzA4dxgNH-J7fGBNcnxzbW5hvX4vwRU7XD3sN3c5laJ6G_WqLmu6Kw0V7K87JMS5DCC_49nIx8vA3ClGb9TwXnNsLM31rhv9RgmyyQI6axY-ytPwvjoiPraWxzGYaqadQaYconAJc4XU89tgU0hZBIYwNniEKkcG-CsoXJfmm0EMuURLo49asA9Hc6YNFYQ-t94lSyY0F7y9yewNuRxqgOD5Mpjs5O33BL9oTNkBee83w2DXj08AWTSNo-HuRUwTc_f5DsacaNIiEqJFUEx9ECaDbnl6JVddPZp7BBLy04QNWYTni7AF-uMZ4Z0t1sQOo986eplnBWkwRKNnRhFNSE-UQLdS-LemRSFYMFsjD2cYq03WifVv3gsNono2OG37PCfkTQVKTwMHZriryTcILlCfBfbr7EN7JwFZKg3Q"
                 }

        return  Request().post(url=url,data=data,cookies=cookies)

    def index(self):
        return  Request().post(url="http://192.168.1.202:8114//manageapi/homeapi/index")
if __name__ == '__main__':
    question_bank().login()
    #question_bank().index()
    # print(question_bank().question_bank_list())
    #print(question_bank().question_bank_add())
    #print(Request().post(url="http://192.168.1.202:8114//manageapi/accountapi/VerifyCodeImg?height=35&width=100&fontsize=20&"))
    #