from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)

    add_to_basket_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    )

    assert add_to_basket_button.text == 'Ajouter au panier'
