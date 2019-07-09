import requests
import sys
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

choices = [
        "option_model148_1_0",
        "option_model148_2_1",
        "option_model148_3_2",
        "option_model148_4_3",
        "option_model148_5_0",
        "option_model148_6_1",
        "option_model148_7_2",
        "option_model148_8_3",
        "option_model148_9_0",
        "option_model148_10_2",
        "option_model148_11_2",
        ]


def get_urls(cookies):
    url = "http://schoopia.com/course/assessment/listCourse?cmd=student"
    headers = {"Cookie":cookies,"User-Agent":"okhttp/3.11.0"}
    try:
        res = requests.get(url,headers=headers).json()
        link = res["data"]["list"]
        urls = [i.get('url') for i in link]
    except Exception:
        if res:
            print(res)
            exit(0)
    return urls



def fill_survey(urls:list):
    length = len(urls)
    for i,url in enumerate(urls):
        if not isinstance(url,str):
            continue
        print(f"正在填写第{i+1}个，一共有{length}个")
        driver.get(url)
        sleep(1)
        for choice in choices:
            driver.find_element_by_xpath(f"//label[@for='{choice}']").click()
        driver.find_element_by_id("answer_model148_12").send_keys("老师讲的非常好，课堂气氛也很不错")
        driver.find_element_by_class_name("survey_submit").click()
        sleep(0.5)

if __name__ == "__main__":
    cookies = sys.argv[1]
    fill_survey(get_urls(cookies))
    driver.close()
    print("填写问卷完成!")
