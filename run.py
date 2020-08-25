import pytest
from common import Base

if __name__ == '__main__':
    pytest.main(["-s","testcase","--alluredir",Base.report_path()])
    Base.allure_report(Base.report_path(),Base.report_html_path())
    # Base.send_mail(content=Base.report_path(),title="测试自动发送邮件")
