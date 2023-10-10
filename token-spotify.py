from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import threading

def scrape_spotify_token():
    print('Seja Bem-vindo(a), ao nosso Web-scraping em Python, \npara burlar o sistema do Spotify, e conseguir pegar o token \n')
    time.sleep(3)

    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://accounts.spotify.com/')
    time.sleep(2)
    driver.find_element(By.ID, 'login-username').send_keys('') # Adicione aqui seu e-mail ou nome de usuário
    driver.find_element(By.ID, 'login-password').send_keys('') # Adicione aqui sua senha
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(5)

    while True:
        try:
            driver.get('https://developer.spotify.com/documentation/web-playback-sdk/tutorials/getting-started')
            time.sleep(2)
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src='/token-button']")
            driver.execute_script("arguments[0].scrollIntoView();", iframe)
            driver.switch_to.frame(iframe)
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-encore-id='buttonPrimary']")))
            button.click()
            token = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-encore-id='type']"))).text
            with open('token.json', 'w') as f:
                json.dump({'token': token}, f)
            driver.switch_to.default_content()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        for i in range(3620, 0, -1):
            time_remaining = '{} minutos e {} segundos restantes para atualizar a pagina'.format(i // 60, i % 60)
            print(time_remaining)
            time.sleep(1)

# Iniciar a execução em segundo plano
background_thread = threading.Thread(target=scrape_spotify_token)
background_thread.start()

# Você pode continuar executando outras tarefas aqui enquanto o código roda em segundo plano
# Certifique-se de não encerrar o programa principal até que o trabalho em segundo plano seja concluído