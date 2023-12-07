from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.firefox.options import Options

# akun email PENS
email = "jhiven@it.student.pens.ac.id" # bukan akun asli
password = "jhivenelek123"

def isi_kuesioner(tipe_kuisioner, driver):
    wait = WebDriverWait(driver, 60)
    print(f"Mengisi Kuisioner {tipe_kuisioner}...")

    try:
        print("menunggu button 'Non Akademik'")
        wait.until(EC.element_to_be_clickable((by.XPATH, "/html/body/div/div[2]/ul/li[3]/a"))).click()
        print("button 'Non Akademik' ditemukan")
    except NoSuchElementException:
        print("button 'Non Akademik' tidak ditemukan")
        driver.quit()

    try:
        print(f"menunggu button Kuisioner {tipe_kuisioner}...")
        wait.until(EC.element_to_be_clickable((by.LINK_TEXT, "Kuisioner " + tipe_kuisioner.capitalize()))).click()
        print(f"button Kuisioner {tipe_kuisioner.capitalize()} ditemukan")
    except NoSuchElementException:
        print(f"button Kuisioner {tipe_kuisioner.capitalize()} tidak ditemukan")
        driver.quit()

    try:
        print("menunggu button 'Klik disini untuk melanjutkan'...")
        wait.until(EC.element_to_be_clickable((by.LINK_TEXT, "Klik disini untuk melanjutkan"))).click()
        print("button 'Klik disini untuk melanjutkan' ditemukan")
    except NoSuchElementException:
        print("button 'Klik disini untuk melanjutkan' tidak ditemukan")
        driver.quit()

    try:
        print("menunggu select cbMatakuliah...")
        wait.until(EC.presence_of_element_located((by.XPATH, "/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/table[3]/tbody/tr/td/h3")))
        btn_select = driver.find_element(by.ID, "cbMatakuliah")
        select_matakuliah = Select(btn_select)
        print("select cbMatakuliah telah ditemukan")
    except NoSuchElementException:
        print("cbMatakuliah tidak ditemukan")
        driver.quit()

    for i in range(1, len(select_matakuliah.options)):
        try:
            matkul = select_matakuliah.options[i].text
        except StaleElementReferenceException:
            select_matakuliah = Select(driver.find_element(by.ID, "cbMatakuliah"))
            matkul = select_matakuliah.options[i].text

        select_matakuliah.select_by_index(i)
        print(f"kuisioner matakuliah {matkul}")
        
        try:
            print(f"menunggu status kuisioner matakuliah {matkul}...")
            wait.until(EC.presence_of_element_located((by.XPATH, "/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/table[3]/tbody/tr/td/h3")))
            btn_submit = driver.find_element(by.XPATH, "//*[@id='Simpan']")
            print(f"status kuisioner matakuliah {matkul} telah ditemukan")
        except NoSuchElementException:
            print(f"kuisioner matakuliah {matkul} telah diisi")
            print(f"mengganti matakuliah...")
            continue;

        print(f"mengisi kuisioner matakuliah {matkul}")
        for radio in driver.find_elements(by.XPATH, "//input[@value='3']"):
            print("melakukan spam kuisioner...")
            radio.click()
        
        btn_submit.click()
        wait.until(EC.visibility_of_element_located((by.XPATH, "//*[@id='tdData']/span")))

    print(f"Kuisioner {tipe_kuisioner} done.")
    driver.get('https://online.mis.pens.ac.id')

def run():
    options = Options()
    options.add_argument('--log-level=OFF')
    options.add_argument('--user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"')
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Firefox(options=options)

    driver.get('https://online.mis.pens.ac.id')

    driver.find_element(by.XPATH, "//a[@title='login']").click()
    driver.find_element(by.XPATH, "//a[@title='login mahasiswa/dosen/staff']").click()

    try:
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((by.NAME, "username")))

        input_email = driver.find_element(by.NAME, "username")
        input_password = driver.find_element(by.NAME, "password")

        input_email.send_keys(email)
        input_password.send_keys(password)
        input_password.send_keys(Keys.RETURN)

        isi_kuesioner("teori", driver)
        isi_kuesioner("praktikum", driver)

    finally:
        driver.implicitly_wait(30)
        driver.quit()

if __name__ == "__main__":
    run()