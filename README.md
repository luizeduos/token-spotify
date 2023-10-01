# Web-Scraping em Python, para burlar o sistema de ***token*** do Spotify

Este script Python usa o Selenium WebDriver para automatizar a interação com a página de login do Spotify e a página de documentação do SDK de reprodução na web. Ele efetua login na conta do Spotify, navega até a página de documentação do SDK de reprodução na web, clica no botão para gerar um token e salva o token em um arquivo JSON.

## Requisitos

- Python 3
- Selenium WebDriver
- Google Chrome

## Como usar
1. Instale as dependências necessárias:
   <code class="language-bash">pip install selenium</code>
2. Baixe o [ChromeDriver](https://chromedriver.chromium.org/home) correspondente à versão do seu Google Chrome e adicione-o ao seu PATH.
3. Substitua <code>'seuemail@aqui.example'</code> e <code>'suaSenha123'</code> pelas suas credenciais do Spotify no script.
4. Execute o script:
   <code class="language-bash">python spotify_token.py</code>
5. O script irá efetuar login na sua conta do Spotify, navegar até a página de documentação do SDK de reprodução na web, clicar no botão para gerar um token e salvar o token em um arquivo chamado <code>token.json</code>.

## Avisos

Este script foi criado apenas para fins educacionais. Não nos responsabilizamos por qualquer uso indevido deste script. Lembre-se sempre de respeitar os Termos de Serviço ao usar scripts de automação.
