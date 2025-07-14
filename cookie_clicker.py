from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule


edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
url = "https://ozh.github.io/cookieclicker/"

driver = webdriver.Edge(options=edge_options)
driver.get(url)

driver.implicitly_wait(20)
english_button = driver.find_element(By.XPATH, "//*[@id='langSelect-EN']")
english_button.click()

# Try to close cookie consent banner if present
try:
    consent_button = driver.find_element(By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all")
    consent_button.click()
    print("Cookie consent accepted.")
except Exception as e:
    print("No cookie consent banner found or could not click:", e)

def Check_store_items():
    store_items_price = [item_price.text for item_price in driver.find_elements(By.CLASS_NAME, "price")]
    store_items_price = [int(price.replace(",", "")) for price in store_items_price if price]
    store_items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    print(f"Prices: {store_items_price}")
    print(f"Store items found: {len(store_items)}")
    current_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0].replace(",", ""))
    affordable_indices = []
    print(current_cookies)
    for idx, item_price in enumerate(store_items_price):
        if item_price <= current_cookies:
            affordable_indices.append(idx)
    if affordable_indices:
        max_price = -1
        max_idx = -1
        for idx in affordable_indices:
            if idx < len(store_items_price) and store_items_price[idx] > max_price:
                max_price = store_items_price[idx]
                max_idx = idx
        print(f"Trying to click store_items[{max_idx}]")
        # Try to close cookie consent banner again if present
        try:
            consent_banner = driver.find_element(By.CSS_SELECTOR, ".cc_banner.cc_container.cc_container--open")
            close_btn = driver.find_element(By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all")
            close_btn.click()
            print("Cookie consent banner closed before store click.")
        except Exception:
            pass  # Banner not present, continue
        if max_idx != -1 and max_idx < len(store_items):
            store_items[max_idx].click()
        else:
            print("No valid affordable item to buy.")
    print(f"Affordable item indices: {affordable_indices}")
    affordable_indices.clear()

schedule.every(15).seconds.do(Check_store_items)


start_time = time.time()
start_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0].replace(",", ""))

cookie_button = driver.find_element(By.ID, "bigCookie")
while True:
    schedule.run_pending()
    cookie_button.click()
    time.sleep(0.1)
    if time.time() - start_time > 300:  # 5 minutes
        break

end_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0].replace(",", ""))
elapsed = time.time() - start_time
cps = (end_cookies - start_cookies) / elapsed
print(f"Cookies per second (calculated): {cps:.2f}")

# Read the game's displayed cookies per second before quitting
try:
    cps_element = driver.find_element(By.ID, "cps")
    print("Cookies per second (game):", cps_element.text)
except Exception as e:
    print("Could not find cps element:", e)

driver.quit()










