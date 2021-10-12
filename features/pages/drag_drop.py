from selenium.webdriver import ActionChains
from Browser import Browser

class drag_drop(Browser):

    def drag (self):
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

    def drop (self):
        message = self.driver.find_element_by_id('dropText').text
        return message


    def perform (self):
        slider = self.driver.find_element_by_xpath('//*[@id="regform"]/div/div[5]/input')
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 280, 16).perform()

    def verify (self):
        msg_2 = self.driver.find_element_by_id('range').text
        return msg_2