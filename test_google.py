from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Ścieżka do ChromeDrivera
chrome_driver_path = "D:/Pliki/Python/WebDriver-GX/chromedriver-win64/chromedriver.exe"

# Konfiguracja przeglądarki
options = Options()
options = webdriver.ChromeOptions()
options.binary_location = "C:/Users/micpe/AppData/Local/Programs/Opera GX/opera.exe"
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--incognito")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36")
options.add_argument("start-maximized")  # Maksymalizuj okno
options.add_argument("disable-infobars")  # Wyłącz pasek informacji
options.add_argument("--disable-blink-features=AutomationControlled")  # Ukryj Selenium
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Uruchomienie przeglądarki
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
import time
time.sleep(5)  # Poczekaj 3 sekundy na załadowanie strony


# Załaduj stronę Google
driver.get("https://www.google.com")
import time
time.sleep(7)  # Poczekaj 3 sekundy na załadowanie strony

try:
    reject_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Odrzuć wszystko')]"))
    )
    reject_cookies.click()
    print("✅ Kliknięto 'Odrzuć wszystko'")
except:
    print("⚠️ Nie znaleziono popupu cookies, przechodzę dalej...")


# Poczekaj na załadowanie strony
time.sleep(3)

# Spróbuj znaleźć pole wyszukiwania i sprawdź, czy Selenium je widzi
try:
    search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "APjFqb"))
)
    print("✅ Element znaleziony!")
except Exception as e:
    print("❌ Błąd: Nie można znaleźć elementu.")
    print(e)

for char in "Selenium WebDriver":
    search_box.send_keys(char)
    time.sleep(0.2)  # Opóźnienie pomiędzy naciśnięciami klawiszy
search_box.send_keys(Keys.RETURN)

import time
time.sleep(10)  # Poczekaj 3 sekundy na załadowanie strony

# Zamknij przeglądarkę
driver.quit()
