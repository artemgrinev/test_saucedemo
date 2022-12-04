import time

from pages.shop_page import RegistrationForm, UsersInfo, ProductCardPage
from pytest_check import check


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
        shop_page = ProductCardPage(driver, url)
        products = shop_page.get_product_dict()
        list_id = shop_page.select_random_product(products)
        count_product_in_cart = shop_page.count_product_in_cart()
        for _id in list_id:
            btn_text = shop_page.get_btn_text(_id, products)
            with check:
                assert btn_text == "REMOVE", f"Кнопка продукта: {_id} не изменила состояние"
        assert len(list_id) == count_product_in_cart, "Количество выбранных продуктов отличается " \
                                                      "от количества продуктов в корзине"

    def test_sorted_products(self, driver):
        url = self.login(driver, UsersInfo.standard_user, UsersInfo.password)
        shop_page = ProductCardPage(driver, url)
        sorted_method = ["a_z", "z_a", "low_high", "high_low"]
        for method in sorted_method:
            with check:
                assert shop_page.sort_products(method) == shop_page.correctly_sorted_data(method), \
                    f"Сортировка {method} не работает"

