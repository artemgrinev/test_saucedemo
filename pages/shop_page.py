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

    def get_btn_text(self, product_id: str, products: dict) -> str:
        return products[product_id]["element"].find_element(By.CSS_SELECTOR, self.locator.BTN).text

    def get_text_btn_dict(self, product_id: list, products: dict) -> dict:
        res = {_id: products[_id]["element"].find_element(By.CSS_SELECTOR, self.locator.BTN).text for _id in product_id}
        return res

    def correctly_sorted_data(self, sort_method: str) -> list:
        if sort_method == "a_z":
            return sorted([i.text for i in self.element_are_visible(self.locator.PRODUCT_NAME)])
        elif sort_method == "z_a":
            return sorted([i.text for i in self.element_are_visible(self.locator.PRODUCT_NAME)], reverse=True)
        elif sort_method == "low_high":
            return sorted([float(i.text.replace("$", "")) for i in self.element_are_visible(self.locator.PRODUCT_PRICE)])
        elif sort_method == "high_low":
            return sorted([float(i.text.replace("$", "")) for i in self.element_are_visible(self.locator.PRODUCT_PRICE)],
                          reverse=True)

    def sort_products(self, sort_method: str) -> list:
        self.element_is_visible(self.locator.SELECT_SORT).click()
        if sort_method == "a_z":
            self.element_is_visible(self.locator.A_Z).click()
            return [i.text for i in self.element_are_visible(self.locator.PRODUCT_NAME)]
        elif sort_method == "z_a":
            self.element_is_visible(self.locator.Z_A).click()
            return [i.text for i in self.element_are_visible(self.locator.PRODUCT_NAME)]
        elif sort_method == "low_high":
            self.element_is_visible(self.locator.LOV_TO_HIGH).click()
            return [float(i.text.replace("$", "")) for i in self.element_are_visible(self.locator.PRODUCT_PRICE)]
        elif sort_method == "high_low":
            self.element_is_visible(self.locator.HIGH_TO_LOV).click()
            return [float(i.text.replace("$", "")) for i in self.element_are_visible(self.locator.PRODUCT_PRICE)]




