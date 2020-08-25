import  requests
from utils.RequestsUtil import *
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml



class question_bank:
    def question_bank_add(self,url):
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
if __name__ == '__main__':
    print(question_bank().question_bank_list())
    #print(question_bank().question_bank_add(url=ConfigYaml().get_testYaml_question_bank_url()))
    #print(Request().post(url="http://192.168.1.202:8114//manageapi/accountapi/VerifyCodeImg?height=35&width=100&fontsize=20&"))
