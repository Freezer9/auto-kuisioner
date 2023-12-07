from selenium import webdriver 
from selenium.webdriver.common.by import By
import getpass
from selenium.webdriver.common.keys import Keys as keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.options import Options as options


options = options()
options.add_argument('--log-level=OFF')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"')

browser = webdriver.Firefox(options=options)
browser.get('https://online.mis.pens.ac.id')
browser.implicitly_wait(5)

while(browser.current_url == 'https://online.mis.pens.ac.id/'):
    try:
        login1 = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/ul/li/a")
        login2 = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/ul/li/ul/li[1]/a")
    except NoSuchElementException:
        continue
    else:
        login1.click()
        login2.click()  
        break

uname = browser.find_element(by=By.ID, value="username")
pword = browser.find_element(by=By.ID, value="password")
uname.send_keys("ryanhusni@ce.student.pens.ac.id")

try:
    while(browser.find_element(by=By.ID, value="username")):
        pw = getpass.getpass()
        pword.send_keys(pw + keys.ENTER)
        # pword.send_keys(dpw + keys.ENTER)
except NoSuchElementException:
    pass

browser.implicitly_wait(15)
#browser.get("https://online.mis.pens.ac.id/mKepuasan2_1.php")

inputPilih = input("Kuesioner Praktikum/Teori? (P/T) : ")
if inputPilih.lower() == "p":
    browser.get("https://online.mis.pens.ac.id/mQuiz_Intro_Praktikum.php")
else:
    browser.get("https://online.mis.pens.ac.id/mQuiz_Intro_Teori.php")

#/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/p/a
#tombol start kuesioner teori

btnMulai = browser.find_element(by=By.XPATH, value="/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/p/a")
btnMulai.click()

#a1-7
#b1-8
#c1-2
#d1-7

input("Pilih matakuliah lalu tekan enter")

def klikKuesioner():
    browser.implicitly_wait(10)
    for i in "abcd":
        for j in range(1,15):
            try:
                if(j > 2):
                    browser.implicitly_wait(0)
                if(browser.find_element(by=By.ID, value= i + str(j) + "_3" )):
                    btnKuesioner = browser.find_element(by=By.ID, value= i + str(j) + "_" + str(nilai) )
                    print("clicking "+ i + str(j) + "_" + str(nilai))
                    btnKuesioner.click()
                else:
                    pass
            except NoSuchElementException:
                pass
        print("done\n")
                
def submitKuesioner():
    input("\ntekan enter untuk submit")
    submitBtn = browser.find_element(by=By.ID, value="Simpan")
    submitBtn.click()

nilai = 3

#askPT()
klikKuesioner()
submitKuesioner()

while(True):
    u_input = input("Jalankan ulang? (Y/n)")
    if u_input.lower() == "y":
       # askPT()
        input("Pilih matakuliah")
        klikKuesioner()
        submitKuesioner()
    else:
        browser.quit()
        exit()


countr = 0

# while(browser.find_element(by=By.CSS_SELECTOR, value='[type=button]')):
#     countr = cekKuesioner()
#     klikKuesioner(countr)
#     continue
# else:
#     print("done")
       
# countr = cekKuesioner()
# klikKuesioner(countr)

while(True):
    continue


# browser.implicitly_wait(30)
# nonakademik = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/ul/li[3]/a")
# nonakademik.click()
# kTeori = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/ul/li[3]/ul/li[3]/a")
# kTeori.click()
# kLanjut = browser.find_element(by=By.XPATH, value="/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/p/a")
# kLanjut.click()
# kIsi = browser.find_element(by=By.XPATH, value="/html/body/form/div/div[3]/table/tbody/tr[1]/td/div/a")
# kIsi.click()


# browser.implicitly_wait(30)
# for i in range(1,a+1):
#     print("clicking r"+ str(i) +"a3")
#     cekNilai = browser.find_element(by=By.ID, value="r"+ str(i) +"a3")
#     cekNilai.click()
# submitBtn = browser.find_element(by=By.CSS_SELECTOR, value='[type=button]')
# submitBtn.click()