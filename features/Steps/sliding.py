from selenium import webdriver
from os import getcwd
from numpy.testing import assert_equal
from selenium.webdriver import ActionChains

@when(u'drag and drop slider')
def step_impl(context):
    context.dd.perform()


@then(u'slide dropped')
def step_impl(context):
    msg_2 = context.dd.verify()
    assert_equal(msg_2, "100")



