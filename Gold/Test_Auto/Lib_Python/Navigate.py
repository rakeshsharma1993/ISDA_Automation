# -*- coding: cp1252 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date, time
import time
import logging
import urllib2,json,urllib
import os
import calendar
import random
import datetime as dt
import re

"""
    Navigate on different portail or application with problem on popup, alert, ...
"""
class Navigate(object):
    
    log_error = False
    
    currentHandles = None
    
    #get browser opened by RIDE to dismiss alert displayed
    """
        Cette fonction est utilisee par :
           - standard.txt
        Elle permet de creer l'url de l'appli en passant pas guardian sans la popup
    """
    def encode_url(self, urlApp, urlGuardian):
        return "https://"+ urlGuardian + "/logingassifaible.jsp?TARGET=$SM$HTTPS%3a%2f%2f" + urlGuardian + "%2fAuthForm%2fredirect.jsp%3fRETURN%3d" + urllib.quote(urlApp, safe='')

    def create_profile_firefox(self):
        from selenium import webdriver
        fp = webdriver.FirefoxProfile()
        #resolve popup firefox when the test stop 
        fp.set_preference("browser.tabs.remote.autostart", False)
        fp.set_preference("browser.tabs.remote.autostart.1", False)
        fp.set_preference("browser.tabs.remote.autostart.2", False)
        fp.set_preference("browser.tabs.remote.force-enable", False)
        
        #download auto the file pdf, txt, docx, xls, xlsx
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir", "C:\SeleniumGrid\Downloads")
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,text/plain;")
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("pdfjs.disabled", True)
        
        #disable auto update firefox
        fp.set_preference("app.update.auto", False)
        fp.set_preference("app.update.enabled", False)
        fp.set_preference("app.update.silent", False)
        fp.set_preference("profile.accept_untrusted_certs", True)
        
        #disable contextual warning https
        fp.set_preference("security.insecure_field_warning.contextual.enabled", False)
        
        fp.update_preferences()
        
        return fp.profile_dir
    
    """
        Cette fonction est utilisee par :
           - Core/page_object/connexion_throught_links.txt
        Elle permet d'annuler une pop-up
    """
    def dismiss_poppup(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        status = True
        try:
            EC.alert_is_present()
            driver.switch_to.alert.dismiss()
        except:
            print "No alert exists"
    """
        Cette fonction est utilisee par :
           - Pogen/Page_Object/acces_NAS.txt
           - Opera_Pilot/Page_object/Requete_recherche_DDP.txt
           - Satin/Page_object/recherche_deplacement_interrogation.txt
           - Satin/Page_object/base_des_sites.txt
           - Prisme/Page_Object/RemoteWebServices.txt
           - Prisme/Page_Object/CreationRegle.txt
           - Prisme/Page_Object/TestDeRegle.txt
           - Prisme/Function/function_association_usage.txt
           - SIG/Page_object/Modification_Compte_Satin.txt
           - Polaris/Stand-Alone.txt
        Elle permet d'accepter une pop-up
    """
    def ok_poppup(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        try:
            EC.alert_is_present()
            alert = driver.switch_to.alert.accept()
            #alert.accept()
        except :
            print "No alert message"
    """
        Cette fonction est utilisee par :
           - Polaris/Stand-Alone.txt
           - Polaris/Function/function_connexion_polaris.txt
           - Synapse/page_object/navigationSynapse.txt
           - Synapse/function/function_connexion_synapse.txt
        Elle permet de s'authentifier lorsqu'une pop-up arrive (fonctionne seulement sur ie)
    """
    def login_poppup(self, login, password):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        try :
            EC.alert_is_present()
            driver.switch_to.alert.authenticate(login, password)
        except :
            print "No alert message"

    """
        Cette fonction est utilisee par :
            - Core_Eqt/Stand-Alone.txt
            - Cedre/page_object/page_control_action.txt
    """
    def fillin_popup(self, url, login, pwd):
        theurl = url
        username = login
        password = pwd

        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, login, pwd)

        authhandler = urllib2.HTTPBasicAuthHandler(passman)

        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

        pagehandle = urllib2.urlopen(url)
        strpage=pagehandle.read()

        if pagehandle.getcode() == 200:
            if "result" in strpage:
                if "id" in strpage:
                    logging.info("WebService run with success")
                else:
                    if "doesn't exist" in strpage:
                        logging.warning("WebService run with success but request parameters are no result")
        else:
            loggin.error("No return of WebService")

        logging.info(strpage)
        assert (pagehandle.getcode() == 200)

        
    """
        Cette fonction est utilisee par :
            - Cedre/page_object/page_control_action.txt
            - EAI/Page_object/VerificationEAIFlux.txt
    """
    def getElementValue(self, ElementaVerifier, flow):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        table = driver.find_elements_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td[9]")
        #tableIMG = driver.find_elements_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td[3]")
        nbrows = len(table)-1
        i=0
        for element in table:
            i=i+1 
            if element.text != "" and element.text != "Parameters":
                ValParametreEAI = element.text
                print "contenue ligne : %s" % ValParametreEAI
                elementNonvide="xpath=/html/body/table/tbody/tr/td/table/tbody/tr["+str(i+2)+"]/td[1]/a/img"
                if (ElementaVerifier in element.text):
                    print ValParametreEAI.split('\n')
##                    i= driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[@class='tableView']/tbody/tr["+str(i+2)+"]/td[1]/img")
                    i= element.find_element_by_xpath("./../td[1]/img")
                    print i.get_attribute("title")
                    if (i.get_attribute("title") != "Info log"):
                        logging.error("Probleme flux: "+ flow +" Parametre du flux : "+ValParametreEAI)
                        time.sleep(5)
                        driver.save_screenshot('Screenshot_'+flow+'.png')
                        assert (Navigate.log_error == True)
                        return elementNonvide
                    else :
                        assert (Navigate.log_error == False)
                        return elementNonvide
                    print i.get_attribute("title")
                    #return elementNonvide
    """
        Cette fonction est utilisee par :
            - EAI
        Elle permet de donner une heure ac le format : HH:MM.
        Le param isEnd permet de savoir si nous devons majoré les minutes et secondes du time
    """
    def getTime(self, isEnd = False):
        m = time.strftime('%M',time.localtime())
        h = time.strftime('%H',time.localtime())
        s = ":00"
        if(isEnd):
            s = ":59"
        else:    
            m=int(m)-20
            if (m < 0) :
                m=m+60
                h=int(h)-1
        return time.strftime('%m/%d/%y',time.localtime()) + " " + str(h) + ":" + str(m)+ str(s)

    """
        Cette fonction est utilisee par :
            - Sacre/function/function_verification.txt
            - Core_Eqt/function/function_version_Install.txt
            - Bacara/Page_object/Navigation.txt
    """
    def verificationVersion(self, valPage, valaVerifier, serveur):
        if("MR" in valaVerifier.upper()):
            valaVerifier= re.sub('[A-Z]{2}[.*-/_]?', '', valaVerifier.upper())
            
        valaChecker = re.sub('[.*-/_]', '-', valaVerifier)
        valinPage = re.sub('[.*-/_]', '-', valPage)    
        
        if (valaChecker in valinPage) :
            assert (Navigate.log_error == False)
        else :
            logging.error("Probleme de version sur le serveur : "+ serveur +"\nValeur attendue : "+ valaChecker +"\nValeur trouvee : "+ valinPage) 
            assert (Navigate.log_error == True)

    """
        Cette fonction est utilisee par :
            - Satin/Page_object/Creation_commande_intrannuaire.txt
            - SIG/Function/function_Feuillet_ZVAD.txt
    """
    def splitText(self,textsplit, caractere,concatener, nbelement):
        test=textsplit.split(caractere)
        result=""
        if (concatener == "oui"):
            i=0
            while i < int(nbelement):
                result = result + test[i]
                i=i+1
                print result
                print i
        return result
    
    """
        Cette fonction est utilisee par :
            - SIG/Function/function_Feuillet_ZVAD.txt
            - OQT/Page_object/LogToOQT.txt
            - Iotaweb/Page_object/OngletCreer.txt
    """
    def VerificationByXpath(self,XpathElement,attributaVerifier,messageaVerifier):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        i= driver.find_element(By.XPATH,XpathElement)
        if (i.get_attribute(attributaVerifier) == messageaVerifier):
            print i.get_attribute(attributaVerifier)
            assert (Navigate.log_error == False)
        else :
            print i.get_attribute(attributaVerifier)
            logging.error("Valeur trouvee :" + i.get_attribute(attributaVerifier))
            assert (Navigate.log_error == True)

    """
        Cette fonction est utilisee par :
            - Bacara/Function/function_numerodeproduction.txt
    """ 
    def WriteInFile(self, cheminFichier, variableAchercher1, nouvelleValeurVariable):
        # Ouverture du fichier source
        #source = open("D:/Users/tremous/Documents/Test_Faisabilite/argfile_bacara1.txt", "r")
        source = open(cheminFichier, "r")
        test=""        
        for ligne in source:
            #test=test+ligne
            if (variableAchercher1 in ligne):
                variableAchercher1 = variableAchercher1 +":"
                #archive = ligne.split(variableAchercher1)
                print ligne
                test=test+variableAchercher1+ nouvelleValeurVariable + "\n"
            else :
                test=test+ligne
        source.close()
        print test
        source = open(cheminFichier, "w")
        source.write(test)
        print 'fichier mis a jour'
        
    """
        Cette fonction est utilisee par :
            - SIG/Function/function_Feuillet_ZVAD.txt
    """
    def getWeekSig(self):
        ic = datetime.now().isocalendar()
        print ic
        Year=str(ic[0])
        Week=ic[1]
        NextWeek= Week + 1
        if(NextWeek > 52):
            NextWeek = "01"
        YearWeek=str(Year) + str(NextWeek)
        YearWeekSig = YearWeek[2:6]
        return YearWeekSig

    """
        Cette fonction est utilisee par :
            - Whatoo/Page_object/Creation_User.txt
            - Whatoo/function/function_Creation_User.txt
            - Isig/Page_Object/Consultation_des_feuillets.txt
    """    
    def ClickByText(self,texte):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        #elements=driver.find_elements_by_partial_link_text(texte)
        try :
            element=driver.find_element_by_partial_link_text(texte)
            print element.text
            element.click()
        except :
            return "false"

    """
        A utiliser avant d'effectuer un selectNewWindow
        Enregistre la liste des fenetres courantes dans l'instance.
    """
    def saveWindowsList(self):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        self.currentHandles = driver.window_handles
        
    """
        Methode maison pour contourner les bugs present en utilisant "select windows | new" sous ride
        Necessite d'utiliser precement la methode saveWindowsList ci dessous avant de generer la nouvelle fenetre
    """  
    def selectNewWindow(self):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        for handle in driver.window_handles:
            if not handle in self.currentHandles:
                  driver.switch_to.window(handle)
                  logging.info("switching to "+driver.title)
    """
        Cette fonction est utilisee par :
            - Prisme 
    """         
    def upPrisme(self,path):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            print 'alerte'         
            newLib = BuiltIn().get_library_instance('Selenium2Library')
            driver = newLib._current_browser()
            time.sleep(2)
            actions= ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            #shell.SendKeys("%{F4}",0)
        else :
            print "No alert exists"

    """
        Cette fonction est utilisee par :
           - Refco 2a2 satin
           - Opera scope !recherche
    """    
    def simulate_keys_Enter(self):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()      
        time.sleep(2)
        actions= ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        
    """    
        Cette fonction est utilisee par :
           - opera_Pilot
    """   
    def save_poppup(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            print 'alerte'         
            newLib = BuiltIn().get_library_instance('Selenium2Library')
            driver = newLib._current_browser()
            time.sleep(2)
            actions= ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            print "fin test"
            #shell.SendKeys("%{F4}",0)
        else :
            print "No alert exists"
    """
        Cette fonction est utilisee par :
           - Gamin 2t2 isig
    """   
    def compare_val(self,valacomparer):

        if valacomparer  : 
            return "true"
            #shell.SendKeys("%{F4}",0)
        else :
            return "false"

    def push_git(self, pathGit, branche):
        os.system("/var/lib/jenkins/workspace/" + pathGit + "/Test_Auto/test.sh " + pathGit + " " + branche)
    """
        Cette fonction est utilisee par :
            - Octave creation contrat
    """
    def add_months(self):
        #sourcedate = datetime.date.today()
        date=time.strftime('%d/%m/%y',time.localtime())
        sourcedate = dt.date.today()
        month = sourcedate.month - 1 + 1
        year = int(sourcedate.year + month / 12 )
        month = month % 12 + 1
        day = min(sourcedate.day,calendar.monthrange(year,month)[1])
        d= datetime.date(year,month,1)
        d=str(d)
        print d
        d = datetime.datetime.strptime(d, '%Y-%m-%d')
        
        return d.strftime('%d/%m/%Y')
    """
        Cette fonction est utilisee par :
            - Octave creation contrat
    """
    def click_droit(self,xpath_element):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        element=driver.find_element_by_xpath(xpath_element)
        print element.text
        #for element in elements:
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.context_click()
        actions.perform()
        print "ok"
        
    """
        Cette fonction est utilisee par :
            - Octave contrat
    """
    def VerificationNonVide(self,XpathElement,attributaVerifier):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        i= driver.find_element(By.XPATH,XpathElement)
        
        if not i.get_attribute(attributaVerifier):
            print i.get_attribute(attributaVerifier)
            print "ok" 
            assert (Navigate.log_error ==  False)
        else :
            print "ko"
            print i.get_attribute(attributaVerifier)
            logging.error("Valeur trouvee :" + i.get_attribute(attributaVerifier))
            assert (Navigate.log_error == True)
    
    """
        This function allows you to do modify the url of the current browser. It's use by : 
            - !connexionSupervision
    """
    def SwitchUrl(self,new_url):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        driver.get(new_url)
    
    """
        Cette fonction est utilisee par :
            - Octave contrat
        Elle permet de donner un nom de contrat (random) pour le test 
    """
    def RandomName(self,texte):
        print "ici : " + texte
        name = texte + str(random.randint(1,99))
        print "le nom du contrat : " + name
        return name
    
    """
        Cette fonction est utilisee par :
            - Whatoo creation de user 
        Elle permet de commiter l'écriture du fichier 
    """
    def commit_file_git(self,filepath,branch):
        print "file : " + filepath
        os.system('git status ' + filepath)
        os.system('git add ' + filepath)
        os.system('git commit -m \"ecriture dans le fichier ' + filepath + ' \"')
        os.system('git push origin ' + branch)

    """
        Cette fonction est utilisee pour les tests de page de supervision 
        Elle permet de verifier si une url contient un element de la liste de server 
    """
    def check_url_server(self,url,listServer):
        logging.info("url  : " + url)
        logging.info("listServer : " + listServer )
        ListServer = listServer.split(',')
        for server in ListServer :
            if server.upper() in url.upper() :
                logging.info("oui server : " + server)
                return 'true'
            else :
                logging.info("non")
        return 'false'      
        
    def mouseMoveTo(self, el):
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        el = driver.find_element_by_xpath(el)
        actions = ActionChains(driver)
        actions.move_to_element(el)
        actions.perform()