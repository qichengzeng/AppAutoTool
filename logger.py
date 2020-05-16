import logging
import os
class Logger:
    title =""
    def __init__(self,title,name="test_case"):
        self.logger = logging.getLogger(name)
        self.title = title
    def my_log(self,msg,level):
        self.logger.setLevel(logging.DEBUG)
        base_path = os.path.dirname(__file__)
        logger_path = os.path.join(base_path,"test_case_log",self.title)
        #添加文件日志和控制台日志
        if os.path.exists(os.path.join(base_path,"test_case_log")):
           self.filehandler=logging.FileHandler(filename=logger_path,mode="a+",encoding="utf-8")
        else:
            os.mkdir(os.path.join(base_path,"test_case_log"))
            self.filehandler = logging.FileHandler(filename=logger_path, mode="a+", encoding="utf-8")
        self.consolehandler = logging.StreamHandler()
        #为文件日志和控制台日志添加日志级别
        self.filehandler.setLevel("DEBUG")
        self.consolehandler.setLevel("DEBUG")
        #文件日志处理器和控制台日志处理器添加日志输出格式
        formatt = logging.Formatter("%(asctime)s____%(name)s___%(levelname)s___%(message)s")#___[%(filename)s:%(lineno)d]
        self.filehandler.setFormatter(formatt)
        self.consolehandler.setFormatter(formatt)
        self.logger.addHandler(self.filehandler)
        self.logger.addHandler(self.consolehandler)
        if level =="DEBUG":
            self.logger.debug(msg)
        elif level =="INFO":
            self.logger.info(msg)
        elif level =="ERROR":
            self.logger.error(msg)
        elif level =="CRITICAL":
            self.logger.critical(msg)
        self.logger.removeHandler(self.consolehandler)
        self.logger.removeHandler(self.filehandler)

    def debug(self,msg):
        self.my_log(msg,"DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")
    def error(self,msg):
        self.my_log(msg,"ERROR")

    def critical(self,msg):
        self.my_log(msg,"CRITICAL")
if __name__ == '__main__':
   l=Logger("login.log")
   l.info("我是info1信息")
   l.info("我是info2信息")