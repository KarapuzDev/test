from selenium import webdriver
import time

driver = webdriver.Chrome()
g = 1
driver.get("https://www.livelib.ru/reviews/~"+str(g)+"#reviews")
# time.sleep(10)
# btn = driver.find_elements_by_css_selector('#a-list-page-next-2')
# btn = driver.find_elements_by_class_name("lenta-card__mymark")

btn = driver.find_elements_by_id('lenta-card__text-review-escaped')
for k in btn:
    print(k.text)
