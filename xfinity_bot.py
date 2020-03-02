from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time


class XfinityBot:
    def __init__(self):
        self.url = "http://10.0.0.1"
        self.index_url = f"{self.url}/index.php"
        self.port_forwarding_url = "{}/port_forwarding.php".format(self.url)
        self.add_service_port_url = "{}/port_forwarding_add.php".format(self.url)

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def shutdown(self):
        self.driver.close()

    def wait(self, seconds):
        time.sleep(seconds)
        return self

    def login(self, username, password):
        self.driver.get(self.index_url)

        elem = self.driver.find_element_by_id("username")
        elem.clear()
        elem.send_keys(username)

        elem = self.driver.find_element_by_id("password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)

        return self

    def toggle_port_forwarding(self, enable=False):

        if enable:
            _class = "radioswitch_on"
        else:
            _class = "radioswitch_off"

        self.driver.get(self.port_forwarding_url)
        elem = self.driver.find_element_by_class_name(_class)
        elem.click()

        return self

    def add_service_port(self, service_name, source_ip, port):
        self.driver.get(self.add_service_port_url)

        elem = self.driver.find_element_by_id("service_name")
        elem.clear()
        elem.send_keys(service_name)

        ip = source_ip.split(".")
        for i in range(4):
            elem = self.driver.find_element_by_id("server_ip_address_{}".format(i + 1))
            elem.clear()
            elem.send_keys(ip[i])

        elem = self.driver.find_element_by_id("start_port")
        elem.clear()
        elem.send_keys(port)

        elem = self.driver.find_element_by_id("end_port")
        elem.clear()
        elem.send_keys(port)

        elem = self.driver.find_element_by_id("btn-save")
        elem.click()

        return self
