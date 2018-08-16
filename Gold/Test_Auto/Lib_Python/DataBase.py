import os
import cx_Oracle
import random
os.environ['NLS_LANG']='FRENCH_FRANCE.UTF8'
class DataBase(object):
    
    valRequete=''
    """
        Cette fonction permet de faire une requete sql et recuperer un element au hasard. Elle est utilisee par :
            - Bacara
    """
    def RequeteSQLOracleElementRandom(self,user,password,url_serveur,port,nomBase,requeteSQL):
        #Requete SQL 
        #SQL="SELECT BW_COM.com_refprd FROM BW_COM, BW_ETP WHERE BW_COM.com_numprd=BW_ETP.com_numprd AND etp_metetpedt='ET_GENERATIONOT2_0' AND ETP_ETAETP='A REALISER' AND (etp_psccal='O' OR etp_psccal='FP')"

        #Parametre de connexion de la base de donnee oracle cx_Oracle.connect('user/password@url_serveur:port/nomdelabase')
        #connection = cx_Oracle.connect('PPRBACWB_MNGR/PPRBACWB_MNGR@obux109-tf.prod.ren.globalone.net:1521/PPRBACWB.WORLD')
        connectionBase = user + "/" + password + "@" + url_serveur + ":" + port +"/" + nomBase
        connection = cx_Oracle.connect(connectionBase)
        cursor = connection.cursor()
        #cursor.execute(SQL)
        cursor.execute(requeteSQL)

        #on recupere un element au hasard de la requete sql en utilisant la fonction random 
        test=random.randint(1,20)
        print str(test)
        i=0
        for row in cursor:
            i=i+1
            if (i is int(test)):
                print row
                valRequete= row
                """Formatage du resultat de la requete sql
                    avt le formatage le resultat : ('CD08TNYM21',)
                    apres formatage le resultat : CD08TNYM21"""
                valRequete = str(valRequete)
                valRequete = valRequete[2:]
                valRequete = valRequete[:-3]
                print valRequete
        cursor.close()
        connection.close()
                
        return valRequete
    """
        Cette fonction permet de faire une requete sql et recuperer le premier element. Elle est utilisee par :
            - Bacara
    """   
    def RequeteSQLOracle(self,user,password,url_serveur,port,nomBase,requeteSQL):
        #Requete SQL 
        #SQL="SELECT BW_COM.com_refprd FROM BW_COM, BW_ETP WHERE BW_COM.com_numprd=BW_ETP.com_numprd AND etp_metetpedt='ET_GENERATIONOT2_0' AND ETP_ETAETP='A REALISER' AND (etp_psccal='O' OR etp_psccal='FP')"

        #Parametre de connexion de la base de donnee oracle cx_Oracle.connect('user/password@url_serveur:port/nomdelabase')
        #connection = cx_Oracle.connect('PPRBACWB_MNGR/PPRBACWB_MNGR@obux109-tf.prod.ren.globalone.net:1521/PPRBACWB.WORLD')
        connectionBase = user + "/" + password + "@" + url_serveur + ":" + port +"/" + nomBase
        connection = cx_Oracle.connect(connectionBase)
        cursor = connection.cursor()
        #cursor.execute(SQL)
        cursor.execute(requeteSQL)
        row = cursor.fetchone()
        #on recupere un element au hasard de la requete sql en utilisant la fonction random 
        valRequete= row
        """Formatage du resultat de la requete sql
                avt le formatage le resultat : ('CD08TNYM21',)
                apres formatage le resultat : CD08TNYM21"""
        valRequete = str(valRequete)
        valRequete = valRequete[2:]
        valRequete = valRequete[:-3]

        cursor.close()
        connection.close()
                
        return valRequete
    def testPushGit(self,path_push_git, pathGit, branche, nameFile):
##        os.system("D:/git/AIS_RM_France/Test_Auto/Lib_Python/testGitPush.bat " + pathGit + " " + branche)
        os.system(path_push_git + "/testGitPush.bat " + pathGit + " " + branche + " " + nameFile)
