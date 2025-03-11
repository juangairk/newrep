from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Путь к ChromeDriver
service = Service(executable_path="./chromedriver.exe")

# Создаём экземпляр WebDriver
driver = webdriver.Chrome(service=service)

# Открываем сайт
driver.get("https://www.yandex.ru")

# Находим поле ввода и вводим текст
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Привет, мир!")

# Нажимаем Enter
search_box.submit()

# Ждём 5 секунд, чтобы увидеть результат
import time
time.sleep(5)

# Закрываем браузер
driver.quit()