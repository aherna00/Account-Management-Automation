from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

valid_accounts = ["roth", "ira", "brokerage", "rollover", "joint"]
valid_data = ["primary", "spouse", "joint"]


def get_valid_input(prompt, valid_responses):
    response_is_valid = False
    while not response_is_valid:
        print(prompt)
        response = input().lower()
        if response in valid_responses:
            response_is_valid = True
        else:
            print("Please enter a valid response:" + ", ".join(valid_responses))
    return response


def open_account():

    account_type = get_valid_input("Enter account type", valid_accounts)

    if account_type == "roth":
        select = Select(driver.find_element_by_id("regTypeAH"))
        select.select_by_value("ROTH")

    elif account_type == "ira":
        select = Select(driver.find_element_by_id("regTypeAH"))
        select.select_by_value("IRA")

    elif account_type == "brokerage":
        select = Select(driver.find_element_by_id("regTypeAH"))
        select.select_by_value("I")

    elif account_type == "rollover":
        select = Select(driver.find_element_by_id("regTypeAH"))
        select.select_by_value("IRRL")

    else:
        select = Select(driver.find_element_by_id("regTypeAH"))
        select.select_by_value("Joint Registration")

    toa_value = get_valid_input("Is there a TOA?", ["yes", "no"])

    if account_type == "brokerage" and toa_value == "yes":
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("TOA")

    elif account_type == "brokerage" and toa_value == "no":
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("AOONLY")

    elif account_type == "joint" and toa_value == "yes":
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("TOA")
        select = Select(driver.find_element_by_xpath
                        ("/html/body/div[2]/div[2]/form/div/div/div[2]/div/div[5]/div[2]/div[4]/div[2]/select"))
        select.select_by_value("J")

    elif account_type == "joint" and toa_value == "no":
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("AOONLY")
        select = Select(driver.find_element_by_xpath
                        ("/html/body/div[2]/div[2]/form/div/div/div[2]/div/div[5]/div[2]/div[4]/div[2]/select"))
        select.select_by_value("J")

    elif toa_value == "yes":
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("TOAIR")
    else:
        select = Select(driver.find_element_by_id("fundMethodAHSelect"))
        select.select_by_value("ACCTFUNDLATER")

    move_money = get_valid_input("Would you like to move money?", ["yes", "no"])

    if move_money == "yes":
        driver.find_element_by_id("featureFormsAccPick").click()
        time.sleep(1)
        driver.find_element_by_id("BNKINSTR").click()
        driver.find_element_by_id("doneaccFeaturebut").click()
        driver.find_element_by_id("submitMain").click()

    else:
        driver.find_element_by_id("submitMain").click()

    WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((By.ID, "goNext"))
    )

    driver.find_element_by_id("goNext").click()

    time.sleep(2)

    if account_type != "joint" and toa_value == "yes":
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[2]/div/h2").click()
        driver.find_element_by_xpath("//div/div[5]/div[2]/div[2]/label/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[4]/div/h2").click()
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[6]/div/h2").click()

    elif account_type == "joint":
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[2]/div/h2").click()
        driver.find_element_by_xpath("//div/div[5]/div[2]/div[2]/label/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[3]/div/h2").click()

    else:
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[2]/div/h2").click()
        driver.find_element_by_xpath("//div/div[5]/div[2]/div[2]/label/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/form/div/div[4]/div/h2").click()

    if account_type == "joint":
        emp_select = Select(driver.find_element_by_id("EmploymentCd_O0"))
        emp_select.select_by_value("E")
        spouse_select = Select(driver.find_element_by_id("EmploymentCd_O1"))
        spouse_select.select_by_value("E")
        driver.find_element_by_xpath \
            ("/html/body/div[2]/form/div/div[2]/div/div[2]/div/div[2]/div[5]/div[2]/div[2]/label/input").click()
    else:
        emp_select = Select(driver.find_element_by_id("EmploymentCd_O0"))
        emp_select.select_by_value("E")

    ama = Select(driver.find_element_by_id("AdvMoneyMvmt"))
    ama.select_by_value("1")

    core = Select(driver.find_element_by_id("CoreSymbol"))
    core.select_by_value("FDRXX")


def push_data():
    if primary == "joint":
        driver.find_element_by_id("Street1_AL").send_keys(street)
        driver.find_element_by_id("Street2_AL").send_keys(street2)
        driver.find_element_by_id("City_AL").send_keys(city)
        driver.find_element_by_id("Zip_AL").send_keys(zip_code)
        driver.find_element_by_id("FirstName_O0").send_keys(first_name)
        driver.find_element_by_id("LastName_O0").send_keys(last_name)
        driver.find_element_by_id("TaxRptgNbr_O0").send_keys(ssn)
        # driver.find_element_by_id("BirthDt0").send_keys(dob) - not working
        driver.find_element_by_id("TelNbr_D_O0").send_keys(cell_phone)
        driver.find_element_by_id("Email1_O0").send_keys(email)
        driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div[2]/div/div[2]/div/div/div[6]/div[3]/div/div[4]/input") \
            .send_keys(emp_name)
        driver.find_element_by_id("Street1_CE").send_keys(emp_add1)
        driver.find_element_by_id("City_CE").send_keys(emp_city)
        driver.find_element_by_id("Zip_CE").send_keys(emp_zip)
        driver.find_element_by_id("Occupation_O0").send_keys(emp_title)
        driver.find_element_by_id("FirstName_O1").send_keys(spouse_name)
        driver.find_element_by_id("LastName_O1").send_keys(spouse_last)
        driver.find_element_by_id("TaxRptgNbr_O1").send_keys(spouse_ssn)
        driver.find_element_by_id("TelNbr_D_O1").send_keys(spouse_cell_phone)
        driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div[2]/div/div[2]/div/div[2]/div[6]/div[3]/div/div[4]/input") \
            .send_keys(spouse_emp_name)
        driver.find_element_by_id("Occupation_O1").send_keys(spouse_emp_title)
        driver.find_element_by_xpath \
            ("/html/body/div[2]/form/div/div[2]/div/div[2]/div/div[2]/div[6]/div[4]/div[2]/div/div/div[4]/div[2]/input") \
            .send_keys(spouse_emp_add1)
        driver.find_element_by_xpath \
            ("/html/body/div[2]/form/div/div[2]/div/div[2]/div/div[2]/div[6]/div[4]/div[2]/div/div/div[6]/div[2]/input") \
            .send_keys(spouse_emp_city)
        driver.find_element_by_xpath \
            ("/html/body/div[2]/form/div/div[2]/div/div[2]/div/div[2]/div[6]/div[4]/div[2]/div/div/div[6]/div[7]/input") \
            .send_keys(spouse_emp_zip)

        # max and min solve an inconsistent quirk in fidelity window that doesn't show entered text
        driver.minimize_window()
        driver.maximize_window()
        driver.find_element_by_id("AccountShortName").clear()
        driver.find_element_by_id("AccountShortName").send_keys(household)
        driver.find_element_by_id("validateForm").click()

    else:
        driver.find_element_by_id("Street1_AL").send_keys(street)
        driver.find_element_by_id("Street2_AL").send_keys(street2)
        driver.find_element_by_id("City_AL").send_keys(city)
        driver.find_element_by_id("Zip_AL").send_keys(zip_code)
        driver.find_element_by_id("FirstName_O0").send_keys(first_name)
        driver.find_element_by_id("LastName_O0").send_keys(last_name)
        driver.find_element_by_id("TaxRptgNbr_O0").send_keys(ssn)
        driver.find_element_by_id("TelNbr_D_O0").send_keys(cell_phone)
        driver.find_element_by_id("Email1_O0").send_keys(email)
        driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div[2]/div/div[2]/div/div/div[6]/div[3]/div/div[4]/input") \
            .send_keys(emp_name)
        driver.find_element_by_id("Street1_CE").send_keys(emp_add1)
        driver.find_element_by_id("City_CE").send_keys(emp_city)
        driver.find_element_by_id("Zip_CE").send_keys(emp_zip)
        driver.find_element_by_id("Occupation_O0").send_keys(emp_title)
        # max and min solve a quirk in fidelity window that doesn't show entered text
        driver.minimize_window()
        driver.maximize_window()
        driver.find_element_by_id("AccountShortName").clear()
        driver.find_element_by_id("AccountShortName").send_keys(household)
        driver.find_element_by_id("validateForm").click()


# code below opens Facet window to gather client data
# uses global/implicit wait

print("Please enter household ID")
household = input()
print("Please enter Facet email")
facet_email = input().lower()
print("Please enter Facet password")
facet_pass_login = input()

facet_driver = webdriver.Chrome()
facet_driver.get("https://app.facetwealth.com/administrator/household/landing?householdId=" + household)
facet_driver.implicitly_wait(60)
facet_driver.maximize_window()

facet_user = facet_driver.find_element_by_id("email")
facet_user.send_keys(facet_email)

facet_password = facet_driver.find_element_by_id("password")
facet_password.send_keys(facet_pass_login)

facet_driver.find_element_by_class_name("square-button").click()
time.sleep(2)
facet_driver.refresh()

# grabs client email before moving to next screen
email = facet_driver.find_element_by_xpath \
    ("//div[2]/div[2]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div[2]/div[1]").get_attribute("innerHTML")

edit_record = facet_driver.find_element_by_partial_link_text("Edit Record")
facet_driver.execute_script("arguments[0].click();", edit_record)

primary = get_valid_input("Is account for primary, spouse, or joint?", valid_data)

# code below pulls client data from form

if primary == "primary":
    first_name = facet_driver.find_element_by_id("firstName").get_attribute("value")
    last_name = facet_driver.find_element_by_id("lastName").get_attribute("value")
    ssn = facet_driver.find_element_by_xpath \
        ("//div[2]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[5]/div/label/input") \
        .get_attribute("value")
    dob = facet_driver.find_element_by_xpath("//div/input").get_attribute("value")
    street = facet_driver.find_element_by_id("address1").get_attribute("value")
    street2 = facet_driver.find_element_by_id("address2").get_attribute("value")
    city = facet_driver.find_element_by_id("city").get_attribute("value")
    zip_code = facet_driver.find_element_by_id("zip").get_attribute("value")
    cell_phone = facet_driver.find_element_by_xpath \
        ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[6]/div/label/input") \
        .get_attribute("value")
    if cell_phone == "":  # checks if 'cell phone' form field has value, if not, pulls number from 'other phone' form field
        cell_phone = facet_driver.find_element_by_xpath \
            ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[8]/div/label/input") \
            .get_attribute("value")
    else:
        pass
    emp_name = facet_driver.find_element_by_id("employer").get_attribute("value")
    emp_title = facet_driver.find_element_by_id("jobTitle").get_attribute("value")
    emp_add1 = facet_driver.find_element_by_id("employerAddress1").get_attribute("value")
    emp_city = facet_driver.find_element_by_id("employerCity").get_attribute("value")
    emp_zip = facet_driver.find_element_by_id("employerZip").get_attribute("value")


elif primary == "spouse":
    first_name = facet_driver.find_element_by_id("significantOtherFirstName").get_attribute("value")
    last_name = facet_driver.find_element_by_id("significantOtherLastName").get_attribute("value")
    ssn = facet_driver.find_element_by_xpath \
        ("//div[2]/div[2]/div/div/div[3]/div/div[4]/div[2]/div/div/div[1]/div[5]/div/label/input") \
        .get_attribute("value")
    street = facet_driver.find_element_by_id("address1").get_attribute("value")
    street2 = facet_driver.find_element_by_id("address2").get_attribute("value")
    city = facet_driver.find_element_by_id("city").get_attribute("value")
    zip_code = facet_driver.find_element_by_id("zip").get_attribute("value")
    cell_phone = facet_driver.find_element_by_xpath \
        ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div/div[1]/div[1]/div/label/input") \
        .get_attribute("value")
    if cell_phone == "":
        cell_phone = facet_driver.find_element_by_xpath \
            ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div/div[1]/div[3]/div/label/input") \
            .get_attribute("value")
    else:
        pass
    emp_name = facet_driver.find_element_by_id("significantOtherEmployerName").get_attribute("value")
    emp_title = facet_driver.find_element_by_id("significantOtherJobTitle").get_attribute("value")
    emp_add1 = facet_driver.find_element_by_id("significantOtherEmployerAddress1").get_attribute("value")
    emp_city = facet_driver.find_element_by_id("significantOtherEmployerCity").get_attribute("value")
    emp_zip = facet_driver.find_element_by_id("significantOtherEmployerZip").get_attribute("value")

else:
    first_name = facet_driver.find_element_by_id("firstName").get_attribute("value")
    last_name = facet_driver.find_element_by_id("lastName").get_attribute("value")
    ssn = facet_driver.find_element_by_xpath \
        ("//div[2]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div[5]/div/label/input") \
        .get_attribute("value")
    dob = facet_driver.find_element_by_xpath("//div/input").get_attribute("value")
    street = facet_driver.find_element_by_id("address1").get_attribute("value")
    street2 = facet_driver.find_element_by_id("address2").get_attribute("value")
    city = facet_driver.find_element_by_id("city").get_attribute("value")
    zip_code = facet_driver.find_element_by_id("zip").get_attribute("value")
    cell_phone = facet_driver.find_element_by_xpath \
        ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[6]/div/label/input") \
        .get_attribute("value")
    if cell_phone == "":  # checks if 'cell phone' form field has value, if not, pulls number from 'other phone' form field
        cell_phone = facet_driver.find_element_by_xpath \
            ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[8]/div/label/input") \
            .get_attribute("value")
    else:
        pass
    emp_name = facet_driver.find_element_by_id("employer").get_attribute("value")
    emp_title = facet_driver.find_element_by_id("jobTitle").get_attribute("value")
    emp_add1 = facet_driver.find_element_by_id("employerAddress1").get_attribute("value")
    emp_city = facet_driver.find_element_by_id("employerCity").get_attribute("value")
    emp_zip = facet_driver.find_element_by_id("employerZip").get_attribute("value")
    spouse_name = facet_driver.find_element_by_id("significantOtherFirstName").get_attribute("value")
    spouse_last = facet_driver.find_element_by_id("significantOtherLastName").get_attribute("value")
    spouse_ssn = facet_driver.find_element_by_xpath \
        ("//div[2]/div[2]/div/div/div[3]/div/div[4]/div[2]/div/div/div[1]/div[5]/div/label/input") \
        .get_attribute("value")
    spouse_cell_phone = facet_driver.find_element_by_xpath \
        ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div/div[1]/div[1]/div/label/input") \
        .get_attribute("value")
    if spouse_cell_phone == "":
        spouse_cell_phone = facet_driver.find_element_by_xpath \
            ("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div/div[1]/div[3]/div/label/input") \
            .get_attribute("value")
    else:
        pass
    spouse_emp_name = facet_driver.find_element_by_id("significantOtherEmployerName").get_attribute("value")
    spouse_emp_title = facet_driver.find_element_by_id("significantOtherJobTitle").get_attribute("value")
    spouse_emp_add1 = facet_driver.find_element_by_id("significantOtherEmployerAddress1").get_attribute("value")
    spouse_emp_city = facet_driver.find_element_by_id("significantOtherEmployerCity").get_attribute("value")
    spouse_emp_zip = facet_driver.find_element_by_id("significantOtherEmployerZip").get_attribute("value")


driver = webdriver.Chrome()
driver.get("https://www.wealthscape.com/")
driver.maximize_window()
main_window = driver.window_handles[0]

print("Please enter Fidelity username")
fido_user = input()
print("Please enter Fidelity password")
fido_pass = input()

user_name = driver.find_element_by_id("userInput")
user_name.send_keys(fido_user)

driver.find_element_by_class_name("group-h__item-spaced").click()

password = WebDriverWait(driver, 45).until(
    EC.presence_of_element_located((By.ID, "password"))
)

password.send_keys(fido_pass)
driver.find_element_by_id("fs-login-button").click()

WebDriverWait(driver, 45).until(
    EC.presence_of_element_located((By.ID, "menu-bar__mega-menu"))
)
driver.find_element_by_id("menu-bar__mega-menu").click()

WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "item_4ba5e56fa9d6f527c44d37e133679b90"))
)

driver.find_element_by_id("item_4ba5e56fa9d6f527c44d37e133679b90").click()
time.sleep(5)

# code below begins to manipulate new window - account open screen

new_window = driver.window_handles[1]
driver.switch_to_window(new_window)
driver.maximize_window()

time.sleep(5)

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

while True:
    open_account()
    push_data()
    print("Would you like to open an additional account?")
    additional_acc = input().lower()
    if additional_acc == "no":
        break
    else:
        driver.find_element_by_id("addAnotherAccountKit").click()


print("Complete. Please verify information.")