from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

inds = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div[4]/div/table[1]/tbody/tr/td[1]/a')
names = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div[4]/div/table[1]/tbody/tr/td[2]/a')
for l in range(len(inds)):
    with open("comapnies.csv", "a") as f:
        f.write(inds[l].text + ":" +names[l].text +"\n")
driver.close()