# coding=utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging

PLATFORM = 'Android'
deviceName = 'NEM_AL10'
app_package = 'com.qidian.QDReader'
app_activity = '.ui.activity.MainGroupActivity'
driver_server = 'http://127.0.0.1:4723/wd/hub'


class Moments:
    def __init__(self):
        self.desired_caps = {
            'noReset': "True",
            'platformName': PLATFORM,
            'deviceName': deviceName,
            'appPackage': app_package,
            'appActivity': app_activity}
        self.driver = webdriver.Remote(driver_server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 1000)

    def login(self):
        print('正在登陆中——————')

    def checkin(self):
        print('开始签到')
        driver = self.driver
        # 打开签到
        el1 = driver.find_element_by_id("com.qidian.QDReader:id/tvBtnText")
        if el1.text == "签到":
            el1.click()
            # 关闭签到
            el2 = driver.find_element_by_id("com.qidian.QDReader:id/ivClose")
            el2.click()
        else:
            print('已经签到')

    def toupiao(self):
        print('开始投票')
        driver = self.driver
        # 书架点击 书籍详情
        el1 = driver.find_element_by_id("com.qidian.QDReader:id/moreImg")
        el1.click()

        # 点击投推荐票
        el2 = driver.find_element_by_id("com.qidian.QDReader:id/tuijian_layout")
        el2.click()

        # 判断
        el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
        if el3.text == "拥有0女生推荐票":
            print('没有推荐票')
            self.driver.back()
        else:
            print('投票')
            el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.LinearLayout[10]/android.widget.TextView")
            el4.click()
            # 点击投推荐票
            el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
            el5.click()

    def choujiang(self):
        print('开始抽奖')
        driver = self.driver

        el1 = driver.find_element_by_id("com.qidian.QDReader:id/tvBtnText")
        if el1.text == "抽奖":
            # 打开去抽奖
            el1.click()
            # 抽奖
            el2 = driver.find_element_by_id("j-toggle")
            el2.click()
            # 关闭抽奖
            el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View/android.view.View[5]")
            el3.click()
            # 关闭抽奖后界面
            self.driver.back()
        else:
            print('已经抽过')

    def main(self):
        self.login()
        actions = [self.toupiao, self.checkin, self.choujiang]
        for action in actions:
            try:
                action()
            except Exception:
                logging.exception("error")


M = Moments()
M.main()
