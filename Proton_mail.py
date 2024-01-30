# from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui


# noinspection PyDeprecation
def send_proton_email(email_to, email_subject, email_message):

    # display = Display(visible=0, size=(1920, 1080))   # Used to create a virtual display to be able to run selenium in a terminal without GUI
    # display.start()
    driver = webdriver.Firefox()
    driver.get('https://mail.protonmail.com/login')
    sleep(10)
    driver.find_element(By.ID, 'username').send_keys('IbV38GimJNf7Nnr@proton.me')
    sleep(2)
    driver.find_element(By.ID, 'password').send_keys('ij+)+R)NqrY@Mkhl')
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button").click()

    sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button").click()
    sleep(10)

    # print(dir(driver))
    driver.switch_to.active_element.send_keys(email_to)
    driver.find_element(By.CSS_SELECTOR, '[id^="subject-composer-"]').send_keys('test')
    el = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]')
    driver.execute_script("arguments[0].textContent = 'Your New Text';", el)

    # driver.find_element(By.CSS_SELECTOR, '/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]/span').click()
    # driver.find_element(By.CSS_SELECTOR, '/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]/span').click()
    sleep(3)
    # pyautogui.typewrite('\t\t\n')
    # sleep(10)
    
    # driver.switch_to.active_element.send_keys(email_subject)
    # pyautogui.typewrite('\t\t')
    # sleep(10)
    # input_el = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]')
    # driver.execute_script(f"arguments[0].textContent = '{email_message}'", input_el)
    sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]/span').click()
    sleep(5)

# //*[@id="to-composer-2268"]
# //*[@id="subject-composer-2125"]




    # driver.find_element(By.XPATH, '//*[@id="pm_sidebar"]/section/a').click()
    # sleep(2)
    # driver.switch_to_active_element().send_keys(email_to + '\n' + '\t' + email_subject + '\t')
    # sleep(0.5)
    # driver.switch_to_active_element().send_keys(email_message + '\t' + '\t' + '\t' + '\t' + '\t' + '\t')
    # sleep(0.5)
    # driver.switch_to_active_element().click()
    
    # driver.quit()
    # display.stop()
    # print('E-mail Sent!')
    # del email_subject
    # del email_message
    # del driver
    # del display
 

send_proton_email('receiver_email@gmail.com', 'test', 'testmsg')
#TEST