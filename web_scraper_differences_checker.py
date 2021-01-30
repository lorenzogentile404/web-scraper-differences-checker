from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import filecmp
import os
import sys

# Alarm time (s)
T_ALARM = 1000

# Minimum time (s) between checks
T_MIN = 60

def alarm(t_alarm):
	for i in range(0,t_alarm):
		os.system('play -nq -t alsa synth {} sine {}'.format(1, 100*randint(3,10))) # s, Hz

def random_sleep(t_min):
	z = t_min + randint(0,10) # Sleep at least t_min
	print("Random sleep " + str(z) + " s...")
	time.sleep(z)

def difference_found():
	print("Difference found!")
	alarm(T_ALARM) # Alarm time (s)
	exit()

# Parse parameters
page = sys.argv[1]
approach = sys.argv[2] # "file:///home/user/e_commerce_test.html"
if approach == "check_n_objects":
	name = sys.argv[3] # "buy-btn"

# Load page
driver = webdriver.Firefox()
driver.get(page)
print("Sleep " + str(5) + " s to let the page load...\n")
time.sleep(5)

# Refresh counter
i = 0

# Check number of objects
check_n_objects = approach == "check_n_objects"
previous_n = 0

# Check HTML
check_html = approach == "check_html"
previous_html = ""

# Check screenshot
check_screenshot = approach == "check_screenshot"

while True:
	if check_n_objects:
		elems = driver.find_elements_by_name(name)
		current_n = len(elems)
		print("Number of " + name + ": " + str(current_n))
		if previous_n != 0 and current_n != previous_n:
			difference_found()
			# Action
			# elems[0].send_keys(Keys.RETURN)
		previous_n = current_n

	if check_html:
		current_html = str(driver.page_source)
		print("Current HTML: " + current_html)
		if previous_html != "" and current_html != previous_html:
			difference_found()
		previous_html = current_html

	if check_screenshot:
		driver.save_screenshot("current_screenshot.png")
		print("Screenshot saved...")
		if os.path.exists("previous_screenshot.png") and not filecmp.cmp("current_screenshot.png","previous_screenshot.png"):
			difference_found()
		if os.path.exists("previous_screenshot.png"):
			os.remove("previous_screenshot.png")
		os.rename("current_screenshot.png","previous_screenshot.png")

	random_sleep(T_MIN)

	i += 1
	driver.refresh()
	print("Page refreshed (" + str(i) + ")!\n")
