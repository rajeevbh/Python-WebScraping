from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create WebDriver instance
driver = webdriver.Chrome()  # Or use Firefox, Edge, etc., based on your preference and installed drivers.

try:
    # Navigate to the webpage
    url = "https://azuredevopslabs.com/"  # Replace with the URL of the webpage you want to search.
    driver.get(url)

    # Wait for elements to be visible for up to 10 seconds
    search_text = "DevOps"  # Replace with the text you want to search.
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(text(), '{}')]".format(search_text))))

    # Debugging messages
    print("Found Elements:", elements)
    count = len(elements)
    print("Number of occurrences of '{}': {}".format(search_text, count))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
