from selenium.webdriver.common.by import By


# Registration Page
class LoginPageLocator:
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, "login-button")


# Product map page
class ProductCardLocator:
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item_description")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_badge")
    BUTTON = ".inventory_item_price+button"
