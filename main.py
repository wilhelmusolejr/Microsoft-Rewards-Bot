from datetime import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# convert time string to datetime
start = time.time()



# class Bot:
#     def __init__(self):
#         self.firstBrowser = webdriver.Chrome(executable_path='driver\chromedriver.exe')
#         self.secondBrowser = webdriver.Chrome(executable_path='driver\chromedriver.exe')

#     def gotopage(self):
#         self.firstBrowser.get("https://www.google.com/")
#         self.secondBrowser.get("https://stackoverflow.com/")


# bot = Bot()
# bot.gotopage()


# email = "geraldine.grant4@gmail.com"
# password = "qw09058222"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='driver\chromedriver.exe', chrome_options= chrome_options)
#---------------------------------------------------
waiting_time = 20;

email = "tawana.harvey42@poqueqo.store"
password = "T.wana.harvey42!"



def login():
    loginWaitingTime = 3
    print("************************"+email+"*************************")
    current_process = "[LOGIN]"
    
    # Goes to website
    driver.get("https://rewards.bing.com/")
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i0116")))
    print(current_process + " Logging in as " + email)

    # input username
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i0116")))
    driver.find_element_by_css_selector('#i0116').send_keys(email)
    # clicks submit
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#idSIButton9")))
    WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9")))
    time.sleep(loginWaitingTime)
    driver.find_element_by_css_selector('#idSIButton9').click()
    # input password
    driver.find_element_by_css_selector('#i0118').send_keys(password)
    # clicks sign in
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#idSIButton9")))
    WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9")))
    time.sleep(loginWaitingTime)
    driver.find_element_by_css_selector('#idSIButton9').click()

    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lightbox > div:nth-child(2) > img")))
    print(current_process + " Logged in")    

def getCurrentPoints():
    current_process = "[POINTS]"
    goMsHome()
    for i in range(2):
        time.sleep(1)
    first_points = driver.find_element(By.CSS_SELECTOR, "#balanceToolTipDiv > p > mee-rewards-counter-animation > span").text
    # print(current_process + " Current points: " + str(first_points))
    return first_points
    
def goMsHome():
    driver.get("https://rewards.bing.com/")
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#rewards-header > div > div.l_header_left")))        

def getPointsBreakdown(): 
    driver.get("https://rewards.bing.com/status/pointsbreakdown")
    WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button")))

    targetSearchPc = driver.find_element(By.CSS_SELECTOR, "#userPointsBreakdown > div > div:nth-child(2) > div > div:nth-child(1) > div > div.pointsDetail > mee-rewards-user-points-details > div > div > div > div > p.pointsDetail.c-subheading-3.ng-binding").text.split()
    targetSearchMobile = driver.find_element(By.CSS_SELECTOR, "#userPointsBreakdown > div > div:nth-child(2) > div > div:nth-child(2) > div > div.pointsDetail > mee-rewards-user-points-details > div > div > div > div > p.pointsDetail.c-subheading-3.ng-binding").text.split()
    targetSearchEdge = driver.find_element(By.CSS_SELECTOR, "#userPointsBreakdown > div > div:nth-child(2) > div > div:nth-child(3) > div > div.pointsDetail > mee-rewards-user-points-details > div > div > div > div > p.pointsDetail.c-subheading-3.ng-binding").text.split()    

    return [targetSearchPc, targetSearchMobile, targetSearchEdge]

def searchFunction():
    searchKey = ""
    
    randomWords = [
		"abandoned","able","absolute","adorable","adventurous","academic","acceptable","acclaimed","accomplished",
		"accurate","aching","acidic","acrobatic","active","actual","adept","admirable","admired","adolescent",
		"adorable","adored","advanced","afraid","affectionate","aged","aggravating","aggressive","agile","agitated",
		"agonizing","agreeable","ajar","alarmed","alarming","alert","alienated","alive","all","altruistic","amazing",
		"ambitious","ample","amused","amusing","anchored","ancient","angelic","angry","anguished","animated","annual",
		"another","antique","anxious","any","apprehensive","appropriate","apt","arctic","arid","aromatic","artistic",
		"ashamed","assured","astonishing","athletic","attached","attentive","attractive","austere","authentic",
		"authorized","automatic","avaricious","average","aware","awesome","awful","awkward","babyish","bad","back",
		"baggy","bare","barren","basic","beautiful","belated","beloved","beneficial","better","best","bewitched","big",
		"bighearted","biodegradable","bitesized","bitter","black"
	     ]

    fNames = ["Harry","Angel","Bruce","Cook","Carolyn","Andrea","Albert","Joshua","Randy","Althea","Larry","Barnes","Nathalie","Wilson","Jesse","Samantha","Ernest","Princess","Sophia","Javier","Henry","Simmons","Michelle","David","Manalo","Shaina","Aguilar"];
    lNames = ["Flores","Bautista","Villanueva","Reyes","Gerald","Fernandez","Raymond","Carter","Jacqueline","Castro","Garcia","Nelson","Santos","Cruz","Castillo","Clark","Lopez","Alexander","Tolentino","Valdez","Eric","Long","Amanda","Diaz","Soriano","Diaz","Wanda","Santiago"];
    toKnow = ["biography", "facebook profile", "instagram profile", "pornhub profile", "social media", "twitter profile", "news paper", "events in life"]
    
    typeSearch = random.randrange(1,5)
    
    if typeSearch == 1:
        searchKey += fNames[random.randrange(0, len(fNames))] + " " + lNames[random.randrange(0, len(lNames))] + " " + toKnow[random.randrange(0, len(toKnow))]
    elif typeSearch == 2:
        searchKey += "Who is " + fNames[random.randrange(0, len(fNames))] + " " + lNames[random.randrange(0, len(lNames))]
    elif typeSearch == 3:
        searchKey += "What is the meaning of " + randomWords[random.randrange(0, len(randomWords))]
    elif typeSearch == 4:
        searchKey += str(random.randrange(10, 100)) + " examples of " + randomWords[random.randrange(0, len(randomWords))]
    else:
        searchKey += "Wilhelmus Ole " + toKnow[random.randrange(0, len(toKnow))] + " and " + toKnow[random.randrange(0, len(toKnow))]

    driver.get("https://www.bing.com/search?q=" + searchKey)
    time.sleep(5)


login()

driver.get("https://www.msn.com/en-us/shopping")
time.sleep(10)

script_to_user_pref_container = 'document.getElementsByTagName("shopping-page-base")[0]\
                .shadowRoot.children[0].children[1].children[0]\
                .shadowRoot.children[0].shadowRoot.children[0]\
                .getElementsByClassName("user-pref-container")[0]'
WebDriverWait(driver, 60).until(EC.visibility_of(driver.execute_script(f'return {script_to_user_pref_container}')))
button = WebDriverWait(driver, 60).until(EC.visibility_of(driver.execute_script(f'return {script_to_user_pref_container}.\
                        children[0].children[0].shadowRoot.children[0].\
                        getElementsByClassName("me-control")[0]'
                    )
                )
            )

button.click()


# email
WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i0116")))
driver.find_element(By.CSS_SELECTOR, "#i0116").send_keys(email)
# next
WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9")))
driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()

time.sleep(10)
# driver.execute_script('(function () {\
#     var msnShoppingGamePane = document\
#     .querySelector("shopping-page-base")\
#     ?.shadowRoot.querySelector("shopping-homepage")\
#     ?.shadowRoot.querySelector("msft-feed-layout")\
#     ?.shadowRoot.querySelector("msn-shopping-game-pane");\
#     if (msnShoppingGamePane != null) {\
#     msnShoppingGamePane.scrollIntoView();\
#     msnShoppingGamePane.style.setProperty("grid-area", "slot1");\
#     msnShoppingGamePane.setAttribute("gamestate", "active");\
#     msnShoppingGamePane.cardsPerGame = 1;\
#     msnShoppingGamePane.resetGame();\
#     } else alert("Unable to locate the shopping game!");\
#     })();')

# elemental = driver.execute_script('return document\
#     .querySelector("shopping-page-base")\
#     ?.shadowRoot.querySelector("shopping-homepage")\
#     ?.shadowRoot.querySelector("msft-feed-layout")\
#     ?.shadowRoot.querySelector("msn-shopping-game-pane")\
#     ?.shadowRoot.querySelectorAll(".shopping-game-card-outline")')

# quering products
products = driver.execute_script('return document\
    .querySelector("shopping-page-base")\
    ?.shadowRoot.querySelector("shopping-homepage")\
    ?.shadowRoot.querySelector("msft-feed-layout")\
    ?.shadowRoot.querySelector("msn-shopping-game-pane")\
    ?.shadowRoot.querySelectorAll(".shopping-game-card-outline")\
    ')


targetClick = random.randrange(0, len(products))
driver.execute_script('document\
  .querySelector("shopping-page-base")\
  ?.shadowRoot.querySelector("shopping-homepage")\
  ?.shadowRoot.querySelector("msft-feed-layout")\
  ?.shadowRoot.querySelector("msn-shopping-game-pane")\
  .shadowRoot.querySelectorAll(".shopping-game-card-outline")['+str(targetClick)+']\
  .querySelector(".shopping-select-overlay-button")\
  .click();')
print("pressed product successfully")

numbuh = 0
for iterate in products:
    title = driver.execute_script('return document\
  .querySelector("shopping-page-base")\
  ?.shadowRoot.querySelector("shopping-homepage")\
  ?.shadowRoot.querySelector("msft-feed-layout")\
  ?.shadowRoot.querySelector("msn-shopping-game-pane")\
  ?.shadowRoot.querySelectorAll(".shopping-game-card-outline")['+str(numbuh)+']\
  ?.querySelector(".shopping-game-card")?.children[0].shadowRoot.children[0].children[0].children[1].querySelector("a").getAttribute("title");')
    
    price = driver.execute_script('return document\
  .querySelector("shopping-page-base")\
  ?.shadowRoot.querySelector("shopping-homepage")\
  ?.shadowRoot.querySelector("msft-feed-layout")\
  ?.shadowRoot.querySelector("msn-shopping-game-pane")\
  .shadowRoot.querySelectorAll(".shopping-game-card-outline")['+str(numbuh)+']\
  .children[0].children[0].shadowRoot.querySelector(\
    ".shopping-price-span-text"\
  ).textContent;')
    
    print(title)
    print(price)
    numbuh += 1



def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

exit()


pointsBreakdown = getPointsBreakdown()
targetSearchPc = pointsBreakdown[0]
targetSearchMobile = pointsBreakdown[1]
targetSearchEdge = pointsBreakdown[2]






# ------------------------------------------
# searches
# ------------------------------------------
isSignedIn = False

# PC SEARCH
currentPoints = int(getCurrentPoints().replace(",", ""))
pointsToBeAdded = int((int(targetSearchPc[-1]) - int(targetSearchPc[0])) + int(currentPoints))

numbuh = 0
while currentPoints != pointsToBeAdded:
    if not isSignedIn:
        current_process = "[CHECKING]"
        print(current_process + " Signing in")
        driver.get("https://www.bing.com/")
        WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#id_s")))
        driver.find_element(By.CSS_SELECTOR, "#id_s").click()
        time.sleep(5)
        isSignedIn = True
    
    searchFunction()
    
    if numbuh % 5 == 0:
        WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_l")))
        currentPoints = int(driver.find_element(By.CSS_SELECTOR, "#id_rc").text)
        current_process = "[PC SEARCH]"
        print(current_process + " " + str(currentPoints) + " of " + str(pointsToBeAdded))
        
    numbuh += 1
    
# MOBILE SEARCH and MICROSOFT BONUS
isSignedIn = False
currentPoints = int(getCurrentPoints().replace(",", ""))
pointsToBeAdded = int(((int(targetSearchMobile[-1]) + int(targetSearchEdge[-1])) - (int(targetSearchMobile[0]) + int(targetSearchEdge[0]))) + int(currentPoints))

numbuh = 0
while currentPoints != pointsToBeAdded:
    if not isSignedIn:
        driver.quit()
        chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
        driver = webdriver.Chrome(executable_path='driver\chromedriver.exe', chrome_options= chrome_options)
        
        login()
        
        driver.get("https://www.bing.com/")
        WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mHamburger")))
        driver.find_element(By.CSS_SELECTOR, "#mHamburger").click()
        WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hb_s")))
        driver.find_element(By.CSS_SELECTOR, "#hb_s").click()
        time.sleep(3)
        
        isSignedIn = True

    searchFunction()
    
    if numbuh % 5 == 0:
        currentPoints = int(getCurrentPoints().replace(",", ""))
        current_process = "[MOBILE SEARCH]"
        print(current_process + " " + str(currentPoints) + " of " + str(pointsToBeAdded))
        
    numbuh += 1

done = time.time()
elapsed = done - start

print(elapsed)

# daily push cards
# activities = driver.find_elements(By.TAG_NAME, "mee-rewards-more-activities-card mee-card")

# i = 1
# for act in activities:
#     cssText = "#more-activities > div > mee-card:nth-child("+ str(i) +") > div > card-content > mee-rewards-more-activities-card-item > div > a > mee-rewards-points > div > div > span"    
#     isHaving = driver.find_elements(By.CSS_SELECTOR, cssText)
    
#     if isHaving:
#         classes = driver.find_element(By.CSS_SELECTOR, cssText).get_attribute("class")
#         classes = classes.split()
#         classes = classes[len(classes) - 1]
#         print(classes)
        
#         if classes == "mee-icon-AddMedium":
#             act.click()

#     i += 1