from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hazWordz

driver= webdriver.Chrome()
driver.get("https://icanhazwordz.appspot.com/")
MyDict= hazWordz.init()
# 10 rounds
highest= 0

for i in range(500):
    total= 0
    for i in range(10):

        content= driver.find_element_by_xpath('/html/body/table/tbody/tr/td').text   #get one word one line
        striped= content.replace("Qu", "Q")
        striped= striped.replace("\n", "").lower()

        resultString, score = hazWordz.main(striped, MyDict)

        if score == 0 :
            driver.find_element_by_xpath("//input[@type='submit' and @value='PASS']").click()
            continue

        driver.find_element_by_id('MoveField').send_keys(resultString[0])
        driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
        total+= score

    print("total score is {}".format(total))
    if total >= 1800:
        break
    else:
        driver.get("https://icanhazwordz.appspot.com/")





