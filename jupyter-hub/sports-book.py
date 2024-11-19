# https://www.zebet.fr/paris-football
# https://www.bet365.com/#/AC/B1/C1/D1001/E13/G40/
# https://www.winamax.fr/paris-sportifs/sports/1
# https://powbet3.com/en/sports?sportids=66

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")

# Disable images and JavaScript for faster loading
prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.managed_default_content_settings.javascript": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Set page load timeout
    driver.set_page_load_timeout(10)  # Adjust the timeout as needed

    # Open the website
    driver.get("https://www.bet365.com/#/AC/B1/C1/D1001/E13/G40/")

    # Wait for the page to load completely
    driver.implicitly_wait(10)  # Adjust the wait time as needed

    # Get the page source
    page_source = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all elements with the class "gl-MarketGroupContainer"
    containers = soup.find_all(class_="gl-MarketGroupContainer")

    # Check if any containers were found
    if containers:
        # Print the content of each container
        for container in containers:
            print(container.get_text(strip=True))
    else:
        # Print the first 10,000 characters of the HTML content for debugging
        print("No containers found. Dumping first 10,000 characters of HTML:")
        print(page_source[:10000])

finally:
    # Close the WebDriver
    driver.quit()