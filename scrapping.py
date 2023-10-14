from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Launch the Chrome browser
path = "/Users/jackson/Downloads/chromedriver"
driver = webdriver.Chrome(path)

website = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"
# Navigate to Amazon's bestseller page
driver.get(website)

driver.quit()
# # Wait for the page to load and the element to become visible
# wait = WebDriverWait(driver, 10)
# element = wait.until(
#     EC.visibility_of_element_located(
#         (By.XPATH, "//div[@class='a-section aok-relative s-image-fixed-height']")
#     )
# )

# # Find the top 10 books and extract their titles
# books = driver.find_elements(
#     By.XPATH,
#     "//div[@class='a-section aok-relative s-image-fixed-height']/following-sibling::div[@class='a-section a-spacing-none aok-inline-block zg-item']/div/a/div[2]/div[1]",
# )
# titles = [book.text for book in books[:10]]

# # Print the titles
# for title in titles:
#     print(title)

# # Close the browser
# driver.quit()
