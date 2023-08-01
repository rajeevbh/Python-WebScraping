from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Create WebDriver instance
driver = webdriver.Chrome()  # Or use Firefox, Edge, etc., based on your preference and installed drivers.

try:
    # Navigate to the webpage
    url = "https://cnswebtechnologies.com/"  # Replace with the URL of the webpage you want to search.
    driver.get(url)

    # Wait for dynamic content to load
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dynamic_content")))

    # Retrieve the HTML content
    page_source = driver.page_source

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Search for the individual text and get its count
    search_text = "design"  # Replace with the text you want to search.
    count = soup.get_text().count(search_text)

    # Print the count
    print(f"Number of occurrences of '{search_text}': {count}")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
