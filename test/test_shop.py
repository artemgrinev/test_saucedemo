import time

from pages.shop_page import RegistrationForm, UsersInfo, ProductCardPage


class LoginPage:

    @staticmethod
    def login(driver, user: str, password: str) -> str:
        url = "https://www.saucedemo.com/"
        registration_page = RegistrationForm(driver, url)
        registration_page.open()
        registration_page.sign_in(user, password)
        return driver.current_url


class TestProductCardPage(LoginPage):

    def test_get_product_card(self, driver):
        url = self.login(driver, UsersInfo.standard_user, UsersInfo.password)
        products_page = ProductCardPage(driver, url)
        products = products_page.get_product_dict()
        list_id = products_page.select_random_product(products)
        count_product_in_cart = products_page.count_product_in_cart()
        test_dict = dict.fromkeys(list_id, "REMOVE")
        result_dict = products_page.get_text_btn(list_id, products)
        if test_dict != result_dict:
            broken_btn = [k for k, v in result_dict.items() if v != "REMOVE"]
        assert test_dict == result_dict, f"Кнопка продукта: {broken_btn} не изменила состояние"

        assert len(list_id) == count_product_in_cart, "Количество выбранных продуктов отличается " \
                                                      "от количества продуктов в корзине"
