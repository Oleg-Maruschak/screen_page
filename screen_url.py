from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




class Screen:
    def __init__(self, url, id_user):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument('hide-scrollbars')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)
        self.driver.implicitly_wait(5)
        self.returnAnsver = {'err': False}
        format_url = self.format_url(url)
        try:
            self.driver.get(format_url)
            self.driver.save_screenshot(f'./{id_user}.png')
            self.returnAnsver['screen'] = f'{id_user}.png'
        except Exception:
            self.returnAnsver['err'] = True
        self.driver.quit()

    def format_url(self, url):
        find_http = url.lower().find('http')
        if find_http == 0:
            return url
        else:
            return f'https://{url}'

    def return_result(self):
        return self.returnAnsver

