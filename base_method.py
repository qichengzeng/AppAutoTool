from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import Logger
from appium import webdriver
from appium.webdriver.common.mobileby import  MobileBy
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import pymysql
import os
import inspect
import random
import time
class BasePage:
    def __init__(self,driver,title):
        self.driver=driver
        self.logger = Logger(title)

    def get_window_size(self):
        self.logger.info("正在准备获取当前窗口的大小")
        try:
            size = (self.driver.get_window_size()["width"],self.driver.get_window_size()["height"])
            self.logger.info("获取当前窗口大小成功为_{}".format(size))
            return size
        except Exception as e:
            self.logger.error("获取当前窗口大小失败")
            raise e

    def click_by_object(self,ele_object):
        self.logger.info("正在准备点击{}对象".format(ele_object))
        try:
            ele_object.click()
            self.logger.info("{}对象点击成功".format(ele_object))
        except Exception as e:
            self.logger.error("{}对象点击失败".format(ele_object))
            raise e

    def click_elements_for_one(self, loc, index):
        self.logger.info("正在准备点击{}元素下标为{}的元素".format(loc, index))
        try:
            self.find_elements(loc, index).click()
            self.logger.info("{}元素下标为{}的元素点击成功".format(loc, index))
        except Exception as e:
            self.logger.error("{}元素下标为{}元素点击失败".format(loc, index))
            raise  e
    def click_element(self,loc):
        self.logger.info("正在准备点击{}元素".format(loc))
        try:
            self.find_element(loc).click()
            self.logger.info("{}元素点击成功".format(loc))
        except Exception as e:
            self.logger.error("{}元素点击失败".format(loc))
            raise e
    def clear(self,loc):
        self.logger.info("正在准备清除{}元素输入框内容".format(loc))
        try:
              self.find_element(loc).clear()
              self.logger.info("{}元素输入框内容清除成功".format(loc))
        except Exception as e:
              self.logger.error("{}元素输入框内容清除失败".format(loc))
              raise  e

    def find_element(self,loc):
        self.logger.info("正在准备查找{}元素".format(loc))
        try:
            ele_object=self.driver.find_element(*loc)
            self.logger.info("{}元素查找成功".format(loc))
            return ele_object
        except Exception as e:
            self.logger.error("{}元素查找失败")
            raise e

    def find_elements_back_object(self,loc,index):
        self.logger.info("正在准备查找一些{}元素".format(loc))
        try:
            ele_object=self.driver.find_elements(*loc)
            self.logger.info("一些{}元素查找成功".format(loc))
            index=int(index)
            return ele_object[index]
        except Exception as e:
            self.logger.error("一些{}元素查找失败".format(loc))
            raise e

    def find_elements_back_objects(self,loc):
        self.logger.info("正在准备查找一些{}元素".format(loc))
        try:
            ele_objects=self.driver.find_elements(*loc)
            self.logger.info("一些{}元素查找成功".format(loc))
            return ele_objects
        except Exception as e:
            self.logger.error("一些{}元素查找失败".format(loc))
            raise e

    def text(self,loc):
        self.logger.info("正在准备获取{}元素的文本值".format(loc))
        try:
            text_value=self.find_element(loc).text
            self.logger.info("获取{}元素文本值成功_{}".format(loc,text_value))
            return text_value
        except Exception as e:
            self.logger.error("获取{}元素文本值失败".format(loc))
            raise e

    def send_keys(self,loc,value):
        self.logger.info("正在准备在{}元素输入框输入内容".format(loc,value))
        try:
            self.find_element(loc).send_keys(value)
            self.logger.info("{}元素输入框输入_{}_内容成功".format(loc,value))
        except Exception as e:
            self.logger.error("{}元素输入框输入{}内容失败".format(loc,value))
            raise e

    def scroll_and_click(self,loc):
        self.logger.info("正在准备滚动屏幕到目标元素{}".format(loc))
        while True:
            try:
                   time.sleep(1)
                   self.find_element(loc).click()
                   self.logger.info("滚动到目标元素{}成功".format(loc))
                   break
            except Exception as e:
                   self.logger.error("滚动到目标元素{}失败".format(loc))
                   self.swipe_up()
    def enter_public(self,loc):
        self.logger.info("正在准备进入名字为{}公众号".format(loc))
        self.visibility_of_element_located(("-android uiautomator",'new UiSelector().text("通讯录")'),20,1)
        try:
            self.click_element(("-android uiautomator",'new UiSelector().text("通讯录")'))
            self.visibility_of_element_located(("-android uiautomator", 'new UiSelector().text("公众号")'), 20, 1)
            self.click_element(("-android uiautomator", 'new UiSelector().text("公众号")'))
            self.scroll_and_click(loc)
            self.logger.info("进入公众号成功")
        except Exception as e:
            self.logger.error("进入公众号失败")
            raise e
    def switch_to_h5(self,loc,wait_time):
        self.logger.info("正在准备切换为h5页面")
        self.visibility_of_element_located(loc,20,1)
        wait_time = int(wait_time)
        try:
            self.click_element(loc)
            time.sleep(wait_time)
            self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
            self.logger.info("从原生native切换到H5页面成功")
        except Exception as e:
            self.logger.error("从原生native切换到H5页面失败")
            raise e

    def sql_search_one(self,sql):
        self.logger.info("正在准备查询数据库值")
        try:
            file_path = os.path.join(os.path.dirname(__file__),"MYSQL.ini")
            with open(file_path,"r") as f:
                read_text = f.read()
                read_list = read_text.split(";")
                ip = read_list[0]
                username = read_list[1]
                password= read_list[2]
                port = int(read_list[3])
                database = read_list[4]
                conn = pymysql.connect(host=ip, port=port, user=username, password=password,
                                       database=database)
                cursor = conn.cursor()
                cursor.execute(sql)
                text = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                self.logger.info("数据库查询成功为_{}".format(text))
                return  text
        except Exception as e:
            self.logger.error("数据库查询失败")
            raise e
    def swipe_up(self):
        self.logger.info("正在准备向上滑动屏幕")
        try:
            size = self.get_window_size()
            start_x = size[0]*0.5
            start_y = size[1]*0.8
            end_x = size[0]*0.5
            end_y = size[1]*0.2
            self.driver.swipe(start_x,start_y,end_x,end_y,500)
            self.logger.info("向上滑动成功")
        except Exception as e:
            self.logger.error("向上滑动失败")
            raise e

    def swipe_down(self):
        self.logger.info("正在准备向下滑动屏幕")
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.5
            start_y = size[1] * 0.2
            end_x = size[0] * 0.5
            end_y = size[1] * 0.8
            self.driver.swipe(start_x, start_y, end_x, end_y, 500)
            self.logger.info("向下滑动成功")
        except Exception as e:
            self.logger.error("向下滑动失败")
            raise e

    def swipe_right(self):
        self.logger.info("正在准备向右滑动屏幕")
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.2
            start_y = size[1] * 0.5
            end_x = size[0] * 0.8
            end_y = size[1] * 0.5
            self.driver.swipe(start_x, start_y, end_x, end_y, 500)
            self.logger.info("向右滑动成功")
        except Exception as e:
            self.logger.error("向右滑动失败")
            raise e
    def swipe_left(self):
        self.logger.info("正在准备向左滑动屏幕")
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.8
            start_y = size[1] * 0.5
            end_x = size[0] * 0.2
            end_y = size[1] * 0.5
            self.driver.swipe(start_x, start_y, end_x, end_y, 500)
            self.logger.info("向左滑动成功")
        except Exception as e:
            self.logger.error("向左滑动失败")
            raise e
    def presence_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素被加载到dom树并不一定可见"""
        self.logger.info("正在准备等待元素{}被加载到dom树中".format(loc))
        try:
            timeout =int(timeout)
            frequency=float(frequency)
            text = WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(loc)).text
            self.logger.info("{}元素被成功加载到dom树".format(loc))
            return text
        except Exception as e:
            self.logger.error("{}元素不存在dom树中".format(loc))
            raise e
    def visibility_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素可见"""
        self.logger.info("正在准备等待{}元素可见".format(loc))
        try:
             WebDriverWait(self.driver,int(timeout),float(frequency)).until(EC.visibility_of_element_located(loc))
             self.logger.info("{}元素可见成功".format(loc))
        except Exception as e:
             self.logger.error("等待{}元素可见失败".format(loc))
             raise e

    def invisibility_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素不可见"""
        self.logger.info("正在准备等待{}元素不可见".format(loc))
        try:
             timeout = int(timeout)
             frequency =int(frequency)
             WebDriverWait(self.driver,timeout,frequency).until_not(EC.visibility_of_element_located(loc))
             self.logger.info("{}元素不可见成功".format(loc))
        except Exception as e:
             self.logger.error("等待{}元素不可见失败".format(loc))
             raise e

    def get_attribute(self,loc,name):
        self.logger.info("正在准备获取元素_{}_的{}的值".format(loc,name))
        try:
            value = self.find_element(loc).get_attribute(name)
            self.logger.info("取元素_{}_的{}的值成功为_{}".format(loc,name,value))
            return value
        except Exception as e:
            self.logger.error("获取元素属性值失败")
            raise e
    def test_screenshot_png(self,filename):
        self.logger.info("正在准备截图")
        try:
            self.driver.get_screenshot_as_file(filename)
            self.logger.info("截图成功")
        except Exception as e:
            self.logger.error("截图失败")
            raise e
    def get_register_name(self):
        self.logger.info("正在准备创建注册用户名")
        try:
           name = "zqc_test_" + str(random.randint(0,100000))
           self.logger.info("创建用户名成功为_{}".format(name))
           return  name
        except Exception as e:
            self.logger.error("创建用户名失败")
            raise e
    def get_mobile_phone(self):
        self.logger.info("正在准备创建手机号")
        try:
            mobile = "182"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
            self.logger.info("创建手机号成功为_{}".format(mobile))
            return mobile
        except Exception as e:
            self.logger.error("创建手机号失败")
            raise e
    def quit(self):
        self.logger.info("正在准备关闭程序")
        try:
            self.driver.quit()
            self.logger.info("关闭程序成功")
        except Exception as e:
            self.logger.error("关闭程序失败")
            raise e
    def sleep(self,s):
        self.logger.info("正在准备强制等待_{}秒".format(s))
        try:
            s= int(s)
            time.sleep(s)
            self.logger.info("强制等待_{}秒_成功".format(s))
        except Exception as e:
            self.logger.error("强制等待失败")
            raise e

    def back_method_dict(self):
        return {"sleep":self.sleep,"quit":self.quit,"get_mobile_phone":self.get_mobile_phone,"switch_to_h5":self.switch_to_h5,
                "enter_public":self.enter_public,
                "get_register_name":self.get_register_name,"test_screenshot_png":self.test_screenshot_png,
                "get_attribute":self.get_attribute,"invisibility_of_element_located":self.invisibility_of_element_located,
                "visibility_of_element_located":self.visibility_of_element_located,"presence_of_element_located":self.presence_of_element_located,
                "swipe_left":self.swipe_left,"swipe_right":self.swipe_right,"swipe_down":self.swipe_down,"swipe_up":self.swipe_up,
                "sql_search_one":self.sql_search_one,"scroll_and_click":self.scroll_and_click,"send_keys":self.send_keys,"text":self.text,
                "clear":self.clear,"click_element":self.click_element,"click_elements_for_one":self.click_elements_for_one}

if __name__ == '__main__':
    # {cmp=com.lemon.lemonban/.activity.MainActivity}
    desired_caps = {
        "platformName": "Android",
        "deviceName": "e8dfc3c6",
        "platformVersino": "9.0",
        "appPackage": "com.tencent.mm",
        "noReset" :"True",
        "appActivity": ".ui.LauncherUI",
        "chromedriverExecutable":os.path.join(os.path.dirname(__file__),"chromedriver.exe"),
        'unicodeKeyboard': "True",
        'resetKeyboard': "True",
        "chromeOptions":{'androidProcess':'com.tencent.mm:tools'}
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    base =BasePage(driver,"test.log")
    # base.visibility_of_element_located((By.ID,"largeLabel"))
    base.enter_public(("-android uiautomator",'new UiSelector().text("涿州爱婴房")'))
    base.switch_to_h5(("-android uiautomator", 'new UiSelector().text("微商城")'),7)
    # test_dict["visibility_of_element_located"](("-android uiautomator",'new UiSelector().text("通讯录")'),20,1.0)
    # test_dict["click_element"](("-android uiautomator",'new UiSelector().text("通讯录")'))
    # test_dict["visibility_of_element_located"](("-android uiautomator", 'new UiSelector().text("公众号")'), 20, 1.0)
    # test_dict["click_element"](("-android uiautomator",'new UiSelector().text("公众号")'))
    # test_dict["visibility_of_element_located"](("-android uiautomator", 'new UiSelector().text("BOSS直聘APP")'), 20, 1.0)
    # test_dict["scroll_and_click"](("-android uiautomator", 'new UiSelector().text("涿州爱婴房")'))
    # test_dict["click_element"](("-android uiautomator", 'new UiSelector().text("涿州爱婴房")'))
    # test_dict["visibility_of_element_located"](("-android uiautomator", 'new UiSelector().text("微商城")'), 20, 1.0)
    # test_dict["click_element"](("-android uiautomator", 'new UiSelector().text("微商城")'))
    # time.sleep(7)
    # contexts=driver.contexts
    # print(contexts)
    # print(driver.current_context)
    # driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
    # print("切换成功")
    # time.sleep(1)
    # driver.find_element_by_xpath("//button[text()='关闭']").click()
    #


