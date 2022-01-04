# Lo scopo di questo script è quello di testare diverse funzionalità del sito demo http://tutorialsninja.com/demo/
# Tra gli step di verifica possiamo elencare i seguenti passi :
# 1 ) Aprire sito http://tutorialsninja.com/demo/
# 2 ) Selezionare 2 Iphone
# 3 ) Eseguire screenshot in pagina
# 4 ) Select 1 Laptop or Tablet
# 5 ) Select delivery date 31-12-2022
# 6) Creare un account
#
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#initilize webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

#Open website URL

OpenBrowser = driver.get("http://tutorialsninja.com/demo/")
sleep(3)



#Click sulla voce menù Phones & PDAs

phones = driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[6]/a')
phones.click()

#Selezionare iphone

iphonePhoneSelect = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/h4/a')
iphonePhoneSelect.click()
sleep(2)

#Click su immagine iphone

first_pic = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/ul[1]/li[1]/a/img')
first_pic.click()
sleep(2)

click_Avanti = driver.find_element(By.XPATH,'/html/body/div[2]/div/button[2]')
for i in range(0,5):
    click_Avanti.click()
    sleep(4)

driver.save_screenshot('screenshot#'+str(random.randint(0,101)) + '.png')


#save screenshot
xbutton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/button')
xbutton.click()


#selezionare quantità

quantità = driver.find_element(By.ID,'input-quantity')
quantità.click()
sleep(2)

cancellaQtn = driver.find_element(By.ID,'input-quantity')
cancellaQtn.clear()
sleep(1)

quantità.send_keys(2)


#Aggiungi al Carrello

addToCart = driver.find_element(By.ID,'button-cart')
addToCart.click()

#Selezionare un TABLET

voceMenùTablet  = driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[4]/a')
voceMenùTablet.click()


#AGGIUNGERE al carrello dall'icona

addTabletCart = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[1]')
addTabletCart.click()


# click menù Laptop

laptops = driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[2]/a')
action = ActionChains(driver)
action.move_to_element(laptops).perform()

check = driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[2]/div/a')
check.click()

sleep(5)
#SELEZIONARE LAPTOP e scroll

HP = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div[1]/div/div[2]/div[1]/h4/a')
HP.click()

#Selezionare Delivery Date ( Calendario )


clickToCartLaptop = driver.find_element(By.ID,'button-cart')
clickToCartLaptop.location_once_scrolled_into_view
sleep(5)


#input calendario
calendario = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div/span/button/i')
calendario.click()
sleep(2)

#Mese e Anno
prossimoClick_calendario = avanti = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[3]')
meseDaSelezionare = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[2]')
while meseDaSelezionare.text != 'December 2022' :
    prossimoClick_calendario.click()
sleep(3)

#day 31
DayCalendar = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/table/tbody/tr[5]/td[6]')
DayCalendar.click()

sleep(10)
driver.save_screenshot('screenshotLaptop#'+str(random.randint(0,101)) + '.png')


clickToCartLaptop.click()


#CheckOUT e Visualizza dettagli carrello

dettagliCarrello = driver.find_element(By.ID,'cart-total')
dettagliCarrello.click()
sleep(5)

checkout = driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/p/a[2]')
checkout.click()

#Rimuovere prodotti non presenti in stock

rimuoviIphone = driver.find_element(By.XPATH,'//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/span/button[2]')
rimuoviIphone.click()
sleep(2)
rimuoviSamsung= driver.find_element(By.XPATH,'//*[@id="content"]/form/div/table/tbody/tr[2]/td[4]/div/span/button[2]')
rimuoviSamsung.click()
sleep(2)

checkout2 = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')
checkout2.click()


guest = driver.find_element(By.XPATH,'//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
guest.click()

continuebtn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input')
continuebtn.click()
sleep(2)

#Compilazione FORM

#details = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/h4/a')
#details.click()


firstName = driver.find_element(By.ID,"input-payment-firstname")
firstName.send_keys('Luca')
sleep(1)

lastName = driver.find_element(By.ID,"input-payment-lastname")
lastName.send_keys('Pitzalis')
sleep(1)

e_Mail = driver.find_element(By.ID,"input-payment-email")
e_Mail.send_keys('luca.test@tim.it')
sleep(1)

telephone = driver.find_element(By.ID,"input-payment-telephone")
telephone.send_keys('351-0000000')
sleep(1)

company = driver.find_element(By.ID, "input-payment-company")
company.send_keys('ALTEN')
sleep(1)

address1 = driver.find_element(By.ID, "input-payment-address-1")
address1.send_keys('Via Test automatico,5')
sleep(1)

city = driver.find_element(By.ID, "input-payment-city")
city.send_keys('ISILI')
sleep(1)

postCode = driver.find_element(By.ID,'input-payment-postcode')
postCode.send_keys('09056')
sleep(1)

country = driver.find_element(By.ID,'input-payment-country')
dropdown = Select(country)
dropdown.select_by_index(56)
sleep(1)

region_state = driver.find_element(By.ID,'input-payment-zone')
dropdown1 = Select(region_state)
dropdown1.select_by_index(2)
sleep(2)

continueForm = driver.find_element(By.ID,'button-guest')
continueForm.click()



#Aggiungere commento al tuo ordine

Commento = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/div[2]/div/p[4]/textarea')
Commento.send_keys('Gli annunci pubblicitari e i contenuti non personalizzati che ti vengono mostrati potrebbero essere influenzati, ad esempio, dai contenuti che stai guardando e sulla tua posizione (la pubblicazione di annunci pubblicitari è basata sulla posizione generica). Gli annunci pubblicitari e i contenuti personalizzati possono essere basati sugli stessi elementi sopra citati e sulle tue attività, ad esempio le ricerche eseguite su Google e i video guardati su YouTube. Gli annunci e i contenuti personalizzati includono, ad esempio, consigli e risultati più pertinenti, una home page di YouTube personalizzata e annunci pubblicitari in linea con i tuoi interessi.')

ContinuaCom = driver.find_element(By.ID,'button-shipping-method')
ContinuaCom.click()

checkTerms = driver.find_element(By.XPATH,'//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]')
checkTerms.click()

ContinuaTerms = driver.find_element(By.ID,'button-payment-method')
ContinuaTerms.click()

confirmOrder = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[2]/div/div[2]/div/input')
confirmOrder.click()

#VERIFICA ORDINE PAGINA FINALE

#verifySuccessText = driver.find_element(By.XPATH,'')


#Close Browser

#CloseBrowser = driver.quit()




