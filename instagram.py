from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os


def login():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1)

    # メアドと、パスワードを入力
    driver.find_element_by_name('username').send_keys('')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('')
    time.sleep(1)

    # ログインボタン
    driver.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(2, 5))
    time.sleep(1)


def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(2, 10))
    time.sleep(1)


def clicklike():
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    time.sleep(1)

    try:
        driver.find_elements_by_class_name('_9AhH0')[9].click()
        time.sleep(random.randint(2, 10))
        time.sleep(1)
        driver.find_element_by_class_name('fr66n').click()
        time.sleep(1)

    except WebDriverException:
        return

    for i in range(random.randint(100, 200)):
        try:
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            time.sleep(random.randint(random.randint(15, 18), random.randint(20, 22)))

        except WebDriverException:
            time.sleep(5)

        try:
            driver.find_element_by_class_name('fr66n').click()
            time.sleep(4)
        except WebDriverException:
            time.sleep(2)


if __name__ == '__main__':

    taglist = ['プログラミング', 'エンジニア', '駆け出しエンジニア']

    while True:
        driver = webdriver.Chrome('/Users/yudaiudtake/Python/Project/instagram/chromedriver')
        time.sleep(3)
        login()

        tagsearch(random.choice(taglist))
        clicklike()

        driver.close()

        abc = random.randint(random.randint(20, 100), random.randint(120, 1800))
        time.sleep(abc)
