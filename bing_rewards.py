import pyautogui
import time
import webbrowser
import requests
import random

# Set bing url
url = 'https://www.bing.com/'

# Set the keyword list url
word_site = "https://www.myhelpfulguides.com/keywords.txt"

# Retrieve the keyword list
response = requests.get(word_site)
# Extract the content
words = response.text.splitlines()

# Open the browser tab
webbrowser.open_new_tab(url)
# Wait a while for the tab to be completely loaded
time.sleep(random.randint(5, 10))
# Start an empty search
pyautogui.press("enter")

# Set the number of search
for i in range(30):
  # Set a random keyword
  search = random.choice(words)

  # Use pyautogui.position() to determine the search box position
  # The position here is detected in a maximised tab on a 4K screen
  pyautogui.click(700, 260)
  # Select texts from previous search using Ctrl + A (windows)
  pyautogui.hotkey("ctrl", "a")
  # Type the selected keyword
  pyautogui.typewrite(search, interval=0.1)
  # Press enter to search
  pyautogui.press("enter")
  # Wait a while and start again.
  time.sleep(random.randint(2, 10))

# Close the browser tab
pyautogui.hotkey("ctrl", "w")

