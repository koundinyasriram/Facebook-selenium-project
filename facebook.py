from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from random import randint



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

email_id=raw_input("Enter your email or phone.no:\n")
password_input=getpass('Enter your Password:\n')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.facebook.com')

email=browser.find_element_by_id("email")
email.send_keys(email_id)

password=browser.find_element_by_id("pass")
password.send_keys(password_input)

password.send_keys(Keys.RETURN)

wishes = [
    'Happy Birthday !!',
    'Happy Birthday! Have a blast.',
    'Many more happy returns of the day',
    'I wish you all the happiness in the world! Happy Birthday.',
    'Just live it out to the fullest and have fun! Happy Birthday',
    'I hope you have the best day ever. Happy Birthday!',
    'Happy Birthday!! May all of your birthday wishes come true.',
    'Happy Birthday! Welcome to the new age.'
    'Best wishes on your birthday .May you have many, many more.'
    'Wishing you the happiest of birthdays.'
    'Happy Birthday! Today is a good day to spend some time with family, and some money on yourself.'
    'I hope you treat yourself to something special on your birthday , you deserve it!'
    'Happy Birthday to one of my favorite people on the planet.'
    'Getting older sucks, but you make it look easy.'
    'You make life more fun for everyone you meet. Thanks for being you.'
    'Congratulations on another year well lived.'
    'You do so much for others, I hope you find time to do something for yourself on your birthday.'
]

current_url=browser.current_url

if current_url!='https://www.facebook.com/login.php?login_attempt=1&lwv=110' :
    suffix='events/birthdays/'
    url=current_url+suffix
    home = current_url

    wishing_page=browser.get(url)
    count = 0
    #count=len(browser.find_elements_by_name("message"))
    #Points to the first section of birthdays division in "birthdays" page and it will be Today's birthday
    go_div=browser.find_elements_by_xpath('//*[@id="birthdays_content"]/div[1]/div[2]/ul/li')
    count=len(go_div)
    #list = []
    #i=0
    try :
        go_today_bday=browser.find_element_by_xpath('//*[@id="birthdays_today_card"]/span[1]')
        if(go_today_bday.text != "Today's Birthdays") :
            count = 0
        if count!=0 :
            print('These friends of yours have their birthdays today')
            i=0
            while(i<count) :
                name=go_div[i].find_element_by_tag_name('a')
                print(name.text)
                i=i+1    
            sleep(1)
            reply=raw_input('Do you want to wish them all ? "yes"?\n')
            if(reply=='yes') :
                i=0
                while(i<count) :
                    wish=""
                    wish=wishes[randint(0,len(wishes)-1)]
                    wishing=go_div[i].find_element_by_name("message")
                    wishing.click()
                    wishing.send_keys(wish)
                    wishing.send_keys(Keys.RETURN)
                    i = i+1
                    sleep(5)
                    wishing_page=browser.get(url)
                    sleep(2)
                    go_div=browser.find_elements_by_xpath('//*[@id="birthdays_content"]/div[1]/div[2]/ul/li')
                return_home=browser.get(current_url)
                print 'Wished every bday buddies. Relax and chill !!'
            else :
                print 'Ok Done! Thy will be done, Wish them on your own. Always here for your service! <3'
        else :
            print 'There are no birthdays today I feel jobless :(' 
    except :
        print 'There are no birthdays today I feel jobless :('
else :
    print 'You are high af. Run program again with correct credentials'

browser.quit()
