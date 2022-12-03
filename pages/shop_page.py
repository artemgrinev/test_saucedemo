import random

from selenium.webdriver.common.by import By

from locators.locators import LoginPageLocator, ProductCardLocator
from pages.base_page import BasePage


class UsersInfo:
    standard_user = "standard_user"
    locked_out_user = "locked_out_user"
    problem_user = "problem_user"
    performance_glitch_user = "performance_glitch_user"
    password = "secret_sauce"


class RegistrationForm(BasePage):
    locator = LoginPageLocator()

    def sign_in(self, user: str, password: str):
        self.element_is_visible(self.locator.USER_NAME).send_keys(user)
        self.element_is_visible(self.locator.PASSWORD).send_keys(password)
        self.element_is_visible(self.locator.BUTTON).click()


class ProductCardPage(BasePage):
    locator = ProductCardLocator()

    def get_product_dict(self) -> dict:
        product_list = self.element_are_visible(self.locator.PRODUCT_ITEM)
        products = {}
        count = 1
        for prod in product_list:
            product = {
                "name": prod.find_element(By.CLASS_NAME, "inventory_item_name").text,
                "price": prod.find_element(By.CLASS_NAME, "inventory_item_price").text,
                "description": prod.find_element(By.CLASS_NAME, "inventory_item_desc").text,
                "button_name": prod.find_element(By.CLASS_NAME, "btn_inventory").get_attribute("name"),
                "element": prod
            }
            products.update({f"id_{count}": product})
            count += 1
        return products

    def select_random_product(self, products: dict) -> list:
        product_id_list = list(products.keys())
        list_id = []
        for _id in random.sample(product_id_list, random.randint(0, 5)):
            locator = (By.NAME, products[_id]['button_name'])
            self.element_is_visible(locator).click()
            list_id.append(_id)
        return list_id

    def count_product_in_cart(self) -> int:
        return int(self.element_is_visible(self.locator.SHOPPING_CART).text)

    def get_prod(self, list_id: list, products: dict) -> str:
        for _id in list_id:
            text_btn = products[_id]["element"].find_element(By.CSS_SELECTOR, self.locator.BUTTON).text
            name = products[_id]["name"]
            yield text_btn, name

    def get_text_btn(self, product_id: list, products: dict) -> dict:
        result = {}
        for _id in product_id:
            text_btn = products[_id]["element"].find_element(By.CSS_SELECTOR, self.locator.BUTTON).text
            result.update({_id: text_btn})
        return result
