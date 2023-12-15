import time
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def run_script(username, password, ctime, otime):
    # make into cool interface later
    message1 = "in"
    message2 = "out"
    routeforjob = '//*[@id="statusid_0_0"]'



    # Path to your updated Chrome WebDriver executable
    chromedriver_path = r'C:\Users\chris\PycharmProjects\OSUClockinClockout\chromedriver.exe'

    # Set up the ChromeDriver service
    service = webdriver.chrome.service.Service(chromedriver_path)

    # Initialize Chrome WebDriver with the service argument
    driver = webdriver.Chrome(service=service)
    driver.get(
        'https://stwcas.okstate.edu/cas/login?service=https%3A%2F%2Fapps.okstate.edu%2Fportal%2Fokstate%2Findex.php%2Fmodule%2FDefault%2Faction%2FVPDI')

    try:
        # Wait until the username field is present and interactable
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )

        # Input your username
        username_field.send_keys(username)

        # Locate the password field using name attribute
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )

        # Input your password
        password_field.send_keys(password)

        # Wait for the login button using different strategies
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))  # Adjust locator if necessary
        )

        # Click the login button using Selenium click() method
        login_button.click()

        # Wait for the verification button and click it as soon as it's clickable
        verification_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Yes, this is my device")]'))
        )
        verification_button.click()

        self_service_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//img[@alt="Self Service"]/parent::a'))
            # Modify the XPath as needed based on the image's alt text and its parent anchor element
        )

        # Click the self-service button using Selenium click() method
        self_service_button.click()

        driver.switch_to.window(driver.window_handles[1])

        # Find and click the anchor link for the Employee Dashboard
        employee_dashboard_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Employee Dashboard"]'))
            # Adjust the XPath to locate the anchor link to the Employee Dashboard by its text
        )
        employee_dashboard_link.click()

        enter_time_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Enter Time")]'))
            # Adjust the XPath to locate the "Enter Time" button by its text or attributes
        )

        enter_time_button.click()

        status_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, routeforjob))
            # Adjust the XPath to locate the element by its ID
        )
        status_element.click()

        days_of_week_xpath = {
            'Sunday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div[1]',
            'Monday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[3]/div[3]/div[1]',
            'Tuesday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[4]/div[3]/div[1]',
            'Wednesday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[5]/div[3]/div[1]',
            'Thursday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[6]/div[3]/div[1]',
            'Friday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[7]/div[3]/div[1]',
            'Saturday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div[8]/div[3]/div[1]',
        }

        # Loop through each day and click on it
        for day, xpath in days_of_week_xpath.items():
            day_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            day_element.click()
            try:
                # Try clicking the first button
                first_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/div[2]/div/div/button'))
                )
                first_button.click()
            except TimeoutException:
                try:
                    # If the first button is not found, try clicking the second button
                    second_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/button'))
                    )
                    second_button.click()
                except TimeoutException:
                    # If neither button is found, skip this step and continue with the loop
                    pass

            try:
                # Try to locate the clock input field 1
                clock_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="clockInInput00"]'))

                )
                clock_input.send_keys(ctime)
            except TimeoutException:
                try:
                    # If the first input field is not found, try to locate the second one
                    clock_input = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="clockInInput01"]'))
                    )
                    clock_input.send_keys(ctime)
                except TimeoutException:
                    pass  # Handle if both input fields are not found

                # Input the string "01:00 PM" into the clock input field (if found)
            try:
                # If the first input field is not found, try to locate the second one
                clock_output = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="clockOutInput_0_0"]'))
                )
                clock_output.send_keys(otime)
            except TimeoutException:
                try:
                    # If the first input field is not found, try to locate the second one
                    clock_input = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="clockOutInput_0_1'))
                    )
                    clock_input.send_keys(ctime)
                except TimeoutException:
                    pass  # Handle if both input fields are not found

            try:
                # Click on the comment in input
                comment_in_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="commentInInput_0_0"]'))
                )
                comment_in_input.click()

                # Input the comment in text
                comment_in_input.send_keys(message1)  # Modify the comment as needed

                # Click on the associated button
                associated_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'))
                )
                associated_button.click()
            except TimeoutException:
                pass  # Handle if comment in input or button is not found

            try:
                # Click on the comment out input
                comment_out_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="commentOutInput_0_0"]'))
                )
                comment_out_input.click()

                # Input the comment out text
                comment_out_input.send_keys(message2)  # Modify the comment as needed

                # Click on the associated button
                associated_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'))
                )
                associated_button.click()
            except TimeoutException:
                pass

            time.sleep(3)

        arrow = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/a[2]/span[1]'))
            # Replace the above XPath with the actual XPath of your desired button
        )
        arrow.click()

        days_of_week_xpath = {
            'Sunday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]',
            'Monday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[3]/div[3]/div[1]',
            'Tuesday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[4]/div[3]/div[1]',
            'Wednesday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[5]/div[3]/div[1]',
            'Thursday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[6]/div[3]/div[1]',
            'Friday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[7]/div[3]/div[1]',
            'Saturday': '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div[8]/div[3]/div[1]',
        }

        for day, xpath in days_of_week_xpath.items():
            day_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            day_element.click()
            try:
                # Try clicking the first button
                first_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/div[2]/div/div/button'))
                )
                first_button.click()
            except TimeoutException:
                try:
                    # If the first button is not found, try clicking the second button
                    second_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/button'))
                    )
                    second_button.click()
                except TimeoutException:
                    # If neither button is found, skip this step and continue with the loop
                    pass

            try:
                # Try to locate the clock input field 1
                clock_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="clockInInput00"]'))

                )
                clock_input.send_keys(ctime)
            except TimeoutException:
                try:
                    # If the first input field is not found, try to locate the second one
                    clock_input = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="clockInInput01"]'))
                    )
                    clock_input.send_keys(ctime)
                except TimeoutException:
                    pass  # Handle if both input fields are not found

                # Input the string "01:00 PM" into the clock input field (if found)
            try:
                # If the first input field is not found, try to locate the second one
                clock_output = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="clockOutInput_0_0"]'))
                )
                clock_output.send_keys(otime)
            except TimeoutException:
                try:
                    # If the first input field is not found, try to locate the second one
                    clock_input = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="clockOutInput_0_1'))
                    )
                    clock_input.send_keys(ctime)
                except TimeoutException:
                    pass  # Handle if both input fields are not found

            try:
                # Click on the comment in input
                comment_in_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="commentInInput_0_0"]'))
                )
                comment_in_input.click()

                # Input the comment in text
                comment_in_input.send_keys("Comment for clock in")  # Modify the comment as needed

                # Click on the associated button
                associated_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'))
                )
                associated_button.click()
            except TimeoutException:
                pass  # Handle if comment in input or button is not found

            try:
                # Click on the comment out input
                comment_out_input = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="commentOutInput_0_0"]'))
                )
                comment_out_input.click()

                # Input the comment out text
                comment_out_input.send_keys("Comment for clock out")  # Modify the comment as needed

                # Click on the associated button
                associated_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'))
                )
                associated_button.click()
            except TimeoutException:
                pass



    finally:
        # Close the browser window
        driver.quit()

def open_window():
    def start_automation():
        # Get values from entry fields
        username = comment1_var.get()
        password = comment2_var.get()
        ctime = comment3_var.get()
        otime = comment4_var.get()

        # Call run_script with provided values
        run_script(username, password, ctime, otime)

    window = tk.Toplevel(root)
    window.title("Yorke Gay System Configuration")

    # Entry for username
    comment1_label = tk.Label(window, text="Username:")
    comment1_label.grid(row=0, column=0, padx=10, pady=5)
    comment1_var = tk.StringVar()
    comment1_entry = tk.Entry(window, textvariable=comment1_var)
    comment1_entry.grid(row=0, column=1, padx=10, pady=5)

    # Entry for password
    comment2_label = tk.Label(window, text="Password:")
    comment2_label.grid(row=1, column=0, padx=10, pady=5)
    comment2_var = tk.StringVar()
    comment2_entry = tk.Entry(window, textvariable=comment2_var, show="*")
    comment2_entry.grid(row=1, column=1, padx=10, pady=5)

    # Entry for clock in
    comment3_label = tk.Label(window, text="Clock in:")
    comment3_label.grid(row=2, column=0, padx=10, pady=5)
    comment3_var = tk.StringVar()
    comment3_entry = tk.Entry(window, textvariable=comment3_var)
    comment3_entry.grid(row=2, column=1, padx=10, pady=5)

    # Entry for clock out
    comment4_label = tk.Label(window, text="Clock Out:")
    comment4_label.grid(row=3, column=0, padx=10, pady=5)
    comment4_var = tk.StringVar()
    comment4_entry = tk.Entry(window, textvariable=comment4_var)
    comment4_entry.grid(row=3, column=1, padx=10, pady=5)

    # Button to trigger automation
    automation_button = tk.Button(window, text="Start Automation", command=start_automation)
    automation_button.grid(row=4, columnspan=2, padx=10, pady=10)


# GUI setup
root = tk.Tk()
root.title("Yorke Gay System")

# Menu setup
menubar = tk.Menu(root)
root.config(menu=menubar)

# Configuration menu
config_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Configuration", menu=config_menu)
config_menu.add_command(label="Open Configuration", command=open_window)

root.mainloop()





'//*[@id="clockOutInput_0_0"]'
'//*[@id="clockOutInput_0_0"]'
'//*[@id="clockOutInput_0_1"]'

'//*[@id="commentInInput_0_0"]'
'//*[@id="commentOutInput_0_0"]'

'/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'
'/html/body/div[7]/div[4]/ui-view/div/ui-view/div/ui-view/div[1]/div/form/div[2]/ui-view/div[5]/div/div/div/div[2]/ng-include/div[4]/div[2]/input'