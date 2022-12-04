from selenium.webdriver.common.by import By


# Registration Page
class LoginPageLocator:
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, "login-button")


class ProductCardLocator:
    # Product map page
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item_description")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    BTN = ".inventory_item_price+button"

    # Product Sort
    SELECT_SORT = (By.CLASS_NAME, "product_sort_container")
    A_Z = (By.CSS_SELECTOR, "[value$=az]")
    Z_A = (By.CSS_SELECTOR, "[value$=za]")
    LOV_TO_HIGH = (By.CSS_SELECTOR, "[value$=lohi]")
    HIGH_TO_LOV = (By.CSS_SELECTOR, "[value$=hilo]")