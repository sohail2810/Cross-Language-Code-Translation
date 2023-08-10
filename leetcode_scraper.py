from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver
driver = webdriver.Firefox()  
count = 0

driver.get("https://leetcode.com/accounts/login/")
time.sleep(2)

driver.find_element(By.ID, "id_login").send_keys("sripallavidamuluri@gmail.com")
driver.find_element(By.ID, "id_password").send_keys("Leetcode@2207")
driver.find_element(By.ID, "signin_btn").click()

time.sleep(2)

for i in range(1,40):
    driver.get("https://leetcode.com/problemset/all/?page=" + str(i))
    time.sleep(2)
    row_group = driver.find_element(By.XPATH, "//*[@role='rowgroup']")
    html = row_group.get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find_all("div", attrs={"role": "row"})
    
    for row in rows:
        a_element = row.find('a')
        href = a_element['href']
        link = "https://leetcode.com" + href + "editorial"
        driver.get(link)

        time.sleep(2)
        html_source = driver.page_source
        start_index = html_source.find("https://leetcode.com/playground")
        end_index = html_source.find('"', start_index+1)
        playground_link = html_source[start_index:end_index]
        try:
            driver.get(playground_link)
            time.sleep(2)
        except:
            continue

        # iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        tag = '<textarea name="lc-codemirror" autocomplete="off" style="display: none;">'
        start_index = driver.page_source.find(tag)
        end_index = driver.page_source.find('</textarea>')
        # print(start_index)
        # print(driver.page_source[start_index + len(tag):end_index])

        div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lang-btn-set")))

        # Find all buttons within the div
        buttons = div.find_elements(By.TAG_NAME, "button")

        # Iterate over the buttons and print their text or perform other actions
        flag = 0
        for button in buttons:
            if button.text == "Java":
                flag += 1
            if button.text == "Python3" or button.text == "Python":
                flag += 1

        if flag == 2:
            for button in buttons:
                if button.text == "Java":
                    button.click()
                    start_index = driver.page_source.find(tag)
                    end_index = driver.page_source.find('</textarea>')
                    with open("java/" + str(count) + ".java", "w") as file:
                        file.write(driver.page_source[start_index + len(tag):end_index])
                elif button.text == "Python3" or button.text == "Python":
                    button.click()
                    start_index = driver.page_source.find(tag)
                    end_index = driver.page_source.find('</textarea>')
                    with open("python/" + str(count) + ".py", "w") as file:
                        file.write(driver.page_source[start_index + len(tag):end_index])
            count += 1
        
driver.quit()



























