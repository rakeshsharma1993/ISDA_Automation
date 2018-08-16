from selenium import webdriver
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
from datetime import date
import unittest

class utils(object):

    """
        Pogen functions
    """

    #select Detail in table Commande
    def select_detail(self, indexTable):
        #get browser already opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        #get Table commande
        tableCommande = driver.find_element_by_id('TableauCommandes')
        rows = tableCommande.find_elements_by_tag_name("tr")
        i = int(indexTable)
        nextLine = True
        while nextLine == True :
            if i < len(rows):
                try:
                    imgDetail = tableCommande.find_element_by_xpath("//tbody/tr["+str(i)+"]/td[2]/a[img/@src='/imgpogen/icone_loupe.gif']")
                    imgDetail.click()
                    nextLine = False
                except:
                    i = i + 1
            else:
                nextLine = False

    #check that last commande is in history
    def verif_commande(self, dateCommande):
        #get browser already opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        time.sleep(5)
        #get table history
        tableHistory = driver.find_element_by_id('TableauHistorique')
        nbRows = len(tableHistory.find_elements_by_tag_name("tr"))
        if nbRows > 3 :
            linkHead = tableHistory.find_element_by_xpath("//tbody/tr[1]/th[1]/a[text()='Date de passage']")
            linkHead.click()
            time.sleep(5)
            tableHistory = driver.find_element_by_id('TableauHistorique')
            #correspond at the first line
            cmdEmis = tableHistory.find_elements_by_tag_name("tr")[1]
            #correspond at the last line
            cmdEnvoie = tableHistory.find_elements_by_tag_name("tr")[2]
            #convert dateCommande in datetime
            date_object = datetime.datetime.strptime(dateCommande, '%Y-%m-%d %H:%M:%S')

            #convert dateEmis in datetime and convert dateEnvoie in datetime
            dateEmis = date.min
            dateEnvoie = date.min

            if cmdEmis.find_elements_by_tag_name("td")[1].text == 'Emis' :
                if cmdEmis.find_elements_by_tag_name("td")[2].text == 'Test, ne pas produire':
                    dateEmis = datetime.datetime.strptime(cmdEmis.find_elements_by_tag_name("td")[0].text, '%d/%m/%Y %H:%M:%S')
            if cmdEnvoie.find_elements_by_tag_name("td")[1].text == 'Envoi':
                dateEnvoie = datetime.datetime.strptime(cmdEnvoie.find_elements_by_tag_name("td")[0].text, '%d/%m/%Y %H:%M:%S')

            sameDate = True
            timeCmd = True
            #check date between dateEmis, dateEnvoie and dateCommande
            sameDate = self.check_date(date_object.date(), dateEmis.date())
            if sameDate :
                if date_object.time() < dateEmis.time() :
                    sameDate = self.check_date(dateEmis, dateEnvoie)
                    print "date emis : " + str(dateEmis)
                    print "date envoie : " + str(dateEnvoie)
                    print "date object : " + str(date_object)
                else:
                    timeCmd = False
            #if it's the right commande, click on file excel to dowload it
            if sameDate and timeCmd :
                col = cmdEnvoie.find_elements_by_tag_name("td")[4]
                imgXl = col.find_elements_by_tag_name("a")
                imgXl[0].click()
            else:
                print 'samedate : ' + str(sameDate)
                print 'timeCmd : ' + str(timeCmd)
                assert (sameDate == True)
                assert (timeCmd == True)
        else:
            print 'nbrows : ' + str(nbRows)
            assert (nbRows > 3)


    def get_num_liasse(self):
        #get browser already opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        nLiasse = driver.find_element_by_id('ref_cmd_four_ora')
        return nLiasse.text

    #check 2 dates
    def check_date(self, dt, dtCompare):
        if dt == dtCompare :
            return True
        else:
            return False

    """
        Core functions
    """

    #click on menu Core
    def navigation_menu(self, idMenu, idSubMenu):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        menu = driver.find_element_by_id(idMenu)
        hidden_submenu = driver.find_element_by_id(idSubMenu)
        ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()


    #click on link of customer name
    def tableResultCustomer(self, idTable, nameCustomer, indexTable) :
        #get browser already opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        try:
            table = driver.find_element_by_id(idTable)
            rows = table.find_elements_by_tag_name("tr")
            nbRows = len(rows)
            i = 1
            n = int(indexTable)
            while i < nbRows :
                label = rows[i].find_elements_by_tag_name("td")[n]
                if label.text == nameCustomer:
                    label.click()
                    i = nbRows
                    time.sleep(5)
                else:
                    i = i + 1
        except:
            print 'no table'

    #Use for test Access throught Core links			
    def change_page(self, url):
        #get browser already opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        #change page
        driver.get(url)

    #select customer line
    def ClickCheckboxCore(self,texte):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        element=driver.find_element_by_xpath("//td[contains(text(), '"+texte+"')]")
        print element.text
        test1= element.find_element_by_xpath("../td[1]")
        test1.click()

    """
        Refco functions
    """

    def change_onglet(self, name_onglet, href_link):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        #onglet = driver.find_element_by_xpath("//div[@id='PSTAB']/table/tbody/tr/td/a/span[text()='" + name_onglet + "']")
        #onglet.click
        #lnkOnglet = driver.find_element_by_xpath("//div[@id='PSTAB']/table/tbody/tr/td/a[@href = '"+ href_link + "']")
        #lnkOnglet.click()
        script_link = href_link[11 :]
        print script_link
        driver.execute_script(script_link)
        
    #wait that div loading disappear
    def wait_div_loading(self, id_element):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        waitLoading = True
        while waitLoading:
            time.sleep(3)
            div = driver.find_element_by_id(id_element)
            attr = div.get_attribute('style')
            if 'DISPLAY' in attr.upper() and 'none' in attr:
                waitLoading = False
    
    """
        Satin functions
    """

    #select EDS_Gestionnaire to duplicate a service
    def select_EDS_Getionnaire(self, EDS_name):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        getNextPage = True
        found = False
        while getNextPage :
            found = self.parcours_Table(EDS_name, driver)
            if found == False:
                getNextPage = self.next_page(driver)
            else:
                getNextPage = False
        

    def parcours_Table(self, EDS_name, driver):
        found = False
        table = driver.find_element_by_id('helpSearchControl_LST')
        lines = table.find_elements_by_tag_name('tr')
        i = 1
        #index = 0
        while i < len(lines):
            name = lines[i].find_elements_by_tag_name('td')[1].text
            if EDS_name in name :
                found = True
                cell = lines[i].find_elements_by_tag_name('td')[0]
                img = cell.find_elements_by_tag_name('input')[0]
                img.click()
                break
            i = i + 1
        #if found:
        #    print index
        #    print lines[index].find_elements_by_tag_name('td')[1].text
            #cell = lines[index].find_elements_by_tag_name('td')[0]
        #    img = table.find_element_by_xpath("//tbody/tr["+str(index + 1)+"]/td[0]/input")
        #    img.click()
        return found

    def next_page(self, driver):
        try:
            img = driver.fid_element_by_xpath("//input[@src='/imgSatinCommande/Next.gif']")
            img.click()
            return True
        except:
            return False

    """
        SA2RA functions
    """

    # check if ICT are created
    def check_One_ICT(self):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        i = 0
        stopWaiting = False
        while i < 10:
            if stopWaiting == False:
                stopWaiting = self.load_search(driver)
                i = i + 1
            else:
                i = 10

    # if ICT contracts are not created, reload page 
    def load_search(self, driver):
        if "ICT" not in driver.title:
            nbElement = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/div/div/div[1]/div[4]/table/tbody[2]/tr/td[2]/div/div/span")
            if '0' in nbElement.text:
                driver.find_element_by_xpath("//html/body/div/div/div/div[1]/div/div[4]/div/table/tbody/tr/td[2]/a/table/tbody/tr/td[2]/div/button").click()
                time.sleep(5)
                driver.find_element_by_xpath("//html/body/div/div/div/div[2]/div/div/table[2]/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td[1]/button").click()
                time.sleep(5)
                return False
            else:
                driver.find_element_by_xpath("//html/body/div/div/div/div[2]/div/div/div[1]/div[3]/table/tbody[2]/tr[1]").click()
                return True
        else:
            return True
