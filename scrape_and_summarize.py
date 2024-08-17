import time
from selenium import webdriver
from bs4 import BeautifulSoup
import openai
import pandas as pd

openai.api_key = 'Navya key'

def summarize_section(content,section):
    try:
        prompt = f"Summarize the '{section}' section from the following content:\n{content}"
        response = openai.Completion.create(
            model = "gpt-4",
            prompt = f"Summarize the folowing content: {content}",
            max_token = 150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error summarizing section '{section}': {e}")
        return "Error"
def get_page_content(url, driver):
    try:
        driver.get(url)
        time.sleep(5)
        DOM = driver.page_source
        soup = BeautifulSoup(DOM, 'html.parser')
        return soup.get_text()
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return ""

def save_to_excel(summaries, filename = "summaries.xlsx"):
    try:
        df = pd.DataFrame(summaries)
        df.to.excel(filename, index=False)
    except Exception as e:
        print(f"Error saving to Excel: {e}")


driver = webdriver.Chrome()
domain = 'http://www.google.com/search?q='
search = 'Top companies in manufacturing sector in Asia'
driver.get(domain + search)
time.sleep(5)

DOM = driver.page_source
soup = BeautifulSoup(DOM, 'html.parser')

def scarpe_and_summarize(query):
    driver = webdriver.Chrome()
    domain = 'http://www,google.com/search?q='
    search = query
    driver.get(domain + search)
    time.sleep(5)

    DOM = driver.page_source
    soup = BeautifulSoup(DOM, 'html.parser')


links = [x['href'] for x in soup.select('a') if x.has_attr('href') and x['href'].startswith('https')]

summaries = []

for link in links:
    print(f'Main URL: {link}')
    try:
        page_content = get_page_content(link, driver)


        location = summarize_section(page_content, "Location")
        product_services = summarize_section(page_content, "Product Services")
        about_us = summarize_section(page_content, "About Us")

        summaries.append({
            "URL": link,
            "Location": location,
            "Product Services": product_services,
            "About Us": about_us
        })
    except Exception as e:
        print(f"Error saving to Excel: {e}")

    sub_urls = [x['href'] for x in BeautifulSoup(page_content, 'html.parser').select('a') if
                x.has_attr('href') and x['href'].startswith('https')]
    for sub_url in sub_urls:
        print(f'Sub URL: {sub_url}')
        try:
            sub_page_content = get_page_content(sub_url, driver)

            # Get summaries and other details for sub-links
            sub_location = summarize_section(sub_page_content, "Location")
            sub_product_services = summarize_section(sub_page_content, "Product Services")
            sub_about_us = summarize_section(sub_page_content, "About Us")

            summaries.append({
                "URL": sub_url,
                "Location": sub_location,
                "Product Services": sub_product_services,
                "About Us": sub_about_us
            })

        except Exception as sub_ex:
            print(f"Error in sub URL {sub_url}: {sub_ex}")

        except Exception as ex:
            print(f"Error in main URL {link}: {ex}")

        driver.quit()

        save_to_excel(summaries)

if __name__ == "__main__":
    query = "Top companies in manufacturing sector in Asia"
    scarpe_and_summarize(query)










