import  requests
from utils.RequestsUtil import *
from utils.RequestsUtil import Request

if __name__ == '__main__':

    # url = ConfigYaml().get_conf_url()+"/authorizations/"
    # url = "http://192.168.1.202:8114"+"//manageapi/testquestionbank/add/"
    # data = {
    #               "bank_type": 1,
    #               "name": "ces22hi",
    #               "organization_id": 1
    #
    #             }
    # cookies={"safetyapplication":"fabpc29FNsrIwcWLkN6o5xjA_YWVI_PKxHBn1gspxGIpnN5BOSe9_tZ23UZlBqcrAFyKYkPXt5xlG2adInbFNRkV8R-cDtA0SeFqssSLNzZUOJyaqUrp-QdOm7Qft7MWdprj0NSAqxzE6i8bZ7iy4Dwaz2zZm0W9QGAu6Gy1Pzf3XPOyDaSP6Cq0f8xcALzjxPA6k44eeRNZCyI-Uu40h01NWMAVfCebIEhiXKNIMM49FhL4iSU8_qLzkBTT_2Chw4zkAmSvi7cD6-yK75tq36kCkYiO950l9ya5XQeZDCOFUcTcXhmXwLOYl77C3H5QCMOc_Y-TtfBevzajcgHPYySk_bwTHdWO0BHNnKQA6V8eVot9E5jTVmn0bCL60ipHJhxlSwF3oyE3yK6IsaDNf2oVCjKJxjKJ_6XM5D8HOvy5cC-SoBmZ590hfhzzLVsCCz8kbw"}
    # print(Request().post(url=url,data=data,cookies=cookies))

    url = "http://192.168.1.202:8114"+"/manageapi/accountapi/Login"
    data = {
                 "email": "admin", "password": "3baf6566eeaeb9f154db656002c010c6", "verifycode": "3e4i", "rememberme": 0

                }
    cookies={"safetyapplication":"fabpc29FNsrIwcWLkN6o5xjA_YWVI_PKxHBn1gspxGIpnN5BOSe9_tZ23UZlBqcrAFyKYkPXt5xlG2adInbFNRkV8R-cDtA0SeFqssSLNzZUOJyaqUrp-QdOm7Qft7MWdprj0NSAqxzE6i8bZ7iy4Dwaz2zZm0W9QGAu6Gy1Pzf3XPOyDaSP6Cq0f8xcALzjxPA6k44eeRNZCyI-Uu40h01NWMAVfCebIEhiXKNIMM49FhL4iSU8_qLzkBTT_2Chw4zkAmSvi7cD6-yK75tq36kCkYiO950l9ya5XQeZDCOFUcTcXhmXwLOYl77C3H5QCMOc_Y-TtfBevzajcgHPYySk_bwTHdWO0BHNnKQA6V8eVot9E5jTVmn0bCL60ipHJhxlSwF3oyE3yK6IsaDNf2oVCjKJxjKJ_6XM5D8HOvy5cC-SoBmZ590hfhzzLVsCCz8kbw"}
    print(Request().post(url=url,data=data))