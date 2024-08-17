import subprocess

files = ['web_scraping.py', 'selenium_scraping.py', 'selenium_web_scraping.py', 'scrape_and_summarize.py']

for file in files:
    print(f"Running {file}...")
    result = subprocess.run(['python', file], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error in {file}:")
        print(result.stderr)
