# Selenium WebDriver Test for Opera GX

### 📌 Opis
Ten skrypt automatyzuje proces wyszukiwania w Google za pomocą **Selenium WebDriver** i przeglądarki **Opera GX**.

🚀 **Działanie skryptu:**
- Otwiera Google w trybie incognito.
- Kliknięcie "Odrzuć wszystko" na pop-upie cookies.
- Wpisanie "Selenium WebDriver" w wyszukiwarce znak po znaku.
- Symulacja losowego czasu reakcji użytkownika.
- Uruchamianie testu w sposób jak najbardziej "naturalny" dla przeglądarki.

⚠️ **Uwaga:** Skrypt zawiera **dużo opóźnień** (`time.sleep()`), ponieważ testowany komputer działa wolniej. Można je zmniejszyć, jeśli sprzęt jest szybszy.

---

## 📥 Instalacja

### 1️⃣ **Wymagania**
- **Python** (3.8+)
- **Selenium**
- **Opera GX**
- **ChromeDriver dopasowany do wersji Opery GX**

### 2️⃣ **Instalacja zależności**
```sh
pip install selenium
```

### 3️⃣ **Pobranie ChromeDrivera** (do Opery GX)
ChromeDriver można pobrać z: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)

📌 **WAŻNE:**
- Pobierz wersję `chromedriver` pasującą do Twojej wersji **Opery GX**
- Upewnij się, że ścieżka do `chromedriver.exe` jest poprawna w skrypcie

---

## ▶️ **Uruchamianie**
W katalogu z plikami uruchom:
```sh
python test_google.py
```

---

## ⚠️ **Najczęstsze problemy i rozwiązania**

### ❌ **Nie znaleziono ChromeDrivera**
**Błąd:**
```sh
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH
```
✅ **Rozwiązanie:**
- Sprawdź, czy `chromedriver.exe` jest w podanej ścieżce.
- Możesz dodać folder do zmiennych środowiskowych lub podać pełną ścieżkę w kodzie.

---

### ❌ **Nie znaleziono elementu wyszukiwarki**
**Błąd:**
```sh
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element
```
✅ **Rozwiązanie:**
- Google czasami pokazuje pop-upy. Dlatego najpierw **zamykamy cookies** przed wpisaniem zapytania.
- Jeśli nadal nie działa, możliwe że **zmienił się XPath** pola wyszukiwania.

---

### ❌ **Blokada Google (CAPTCHA)**
**Błąd:** Google wykrywa automatyczne zapytania i wyświetla reCAPTCHA.
✅ **Rozwiązanie:**
- Wydłuż czas pomiędzy akcjami (`time.sleep(random.uniform(2,5))`).
- Zmień User-Agent (`options.add_argument("user-agent=Mozilla/5.0...")`).
- W razie potrzeby dodaj dodatkowe losowe ruchy kursorem lub scrollowanie strony.

---

## 📌 **Podsumowanie**
✅ Gotowy do użycia test w Selenium dla Opery GX. 
✅ Skrypt omija cookies i wyszukuje w Google.
✅ Zastosowano opóźnienia dla lepszego działania.
✅ W przyszłości można rozbudować testy np. o klikanie wyników.

💡 **Jeśli masz pytania lub chcesz ulepszyć skrypt, fork repozytorium i stwórz pull request!** 🚀
