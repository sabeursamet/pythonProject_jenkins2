from behave import given,when, then
from numpy.testing import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains

URL = 'https://qavbox.github.io/demo/dragndrop/'

@given(u'user is in designed URL')
def step_impl(context):
    context.browser.get(URL)

@given(u'two boxes appeared')
def step_impl(context):
    print('page opened')

@when(u'user select "Drag" Box')
def step_impl(context):
    context.dd.drag()

    print('action done')

@when(u'Drop it to "Drop here" box')
def step_impl(context):
    print("drag and drop done")

@then(u'Dropped text appears')
def step_impl(context):
    msg = context.dd.drop()
    assert_equal(msg, "Dropp")


