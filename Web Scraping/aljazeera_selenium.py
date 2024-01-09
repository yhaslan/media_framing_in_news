from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service




# Initialize Chrome WebDriver
driver_path = '/usr/local/bin/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

url = 'https://www.aljazeera.com/tag/israel-war-on-gaza/'
driver.get(url)

privacy_info_link = driver.find_element(By.XPATH, '//a[@aria-label="More information about your privacy"]')
driver.execute_script("arguments[0].scrollIntoView();", privacy_info_link)

i = 0
while i<300:
    try:
        show_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="show-more-button"]')))
        driver.execute_script("arguments[0].scrollIntoView();", show_more_button)  # Scroll to the button
        driver.implicitly_wait(3)
        show_more_button.click()
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-spinner-class')))
        i+=1
    except:
        print("No more 'Show more' button found or it's not clickable.")
        break
else:
    print("End of Search Results.")


aljazeera_html_content = driver.page_source
with open('aljazeera_html_content.html', 'w', encoding='utf-8') as file:
    file.write(aljazeera_html_content)

driver.quit()