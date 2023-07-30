import tkinter as tk
import tkinter.messagebox as mbox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
import chromedriver_autoinstaller

class WebContentFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_text_from_web(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            return driver.page_source
        except Exception as e:
            print("Error:", e)
            return None
        finally:
            driver.quit()

    def close_message_box(self):
        self.root.destroy()

    def fetch_and_alert(self):
        text = self.fetch_text_from_web()
        if text is not None:
            self.root = tk.Tk()
            self.root.withdraw()
            mbox.showinfo("Web Page Content", text)
            self.root.after(5000, self.close_message_box)  # Close the message box after 5000 milliseconds (5 seconds)
            self.root.mainloop()

if __name__ == "__main__":
    # Replace this URL with the desired webpage URL
    webpage_url = "https://example.com"

    web_content_fetcher = WebContentFetcher(webpage_url)

    # Fetch the text from the webpage in the background using a separate thread
    thread = Thread(target=web_content_fetcher.fetch_and_alert)
    thread.start()
