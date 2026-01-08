# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:

        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    browser = webdriver.Chrome(options=chrome_options)

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 100
    options = '--headless', '--disable-gpu', # --headless, executa as ações sem abrir o navegador
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    pesquisar = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@aria-label="Pesquisar"]')
        )
    ) # localiza a barra de pesquisa

    pesquisar.send_keys('youtube')
    pesquisar.send_keys(Keys.ENTER)

    # aqui estaria o código da aula 322, como o chrome bloqueia o uso com captcha, não tenho como fazer agora

    # Dorme por 10 segundos
    sleep( TIME_TO_WAIT)