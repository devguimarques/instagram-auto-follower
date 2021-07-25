from selenium import webdriver
from time import sleep


with open('followers.txt', 'r') as seguidores:
    followers = list(seguidores)


def main():

    url = 'https://www.instagram.com'
    driver = webdriver.Chrome('C:/webdrivers/chromedriver')
    driver.get(url)

    sleep(1)
    driver.find_element_by_class_name('aOOlW').click()  # cookies
    sleep(2)
    driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input').send_keys('your user')  # user
    sleep(0.6)
    driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input').send_keys('your pass')  # pass
    sleep(0.7)
    driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div').click()  # login
    sleep(4)
    try:
        driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()  # nao guardar info
        sleep(4)
    except:
        pass

    for n in followers:
        driver.get('https://www.instagram.com/' + followers.pop(0))  # pagina para ir
        sleep(3)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click() # seguir
            print(f'\033[1;33mfollowed:\033[m {n}')
            sleep(3)
        except:
            print(f'\033[1;31mprivate acc:\033[m {n}')
            pass

main()