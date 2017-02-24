from selenium import webdriver
import urllib

driver = webdriver.Chrome()
driver.get("https://anime-odcinki.pl/anime/all-out/1")

try:
    driver.implicitly_wait(10)
    #kod = driver.find_element_by_class_name("vjs-tech")
    kod = driver.find_element_by_tag('video')
    print(kod)

except Exception as e:
    print("Wyjatek znaleziony",format(e))
#//*[@id="player_html5_api"]/source
driver.close()
