import requests 
import os 
class _ :
    @staticmethod 
    def _ ():
        try :
            O00OO0OOOO00OO00O =os .path .join (os .path .dirname (__file__ ),'../../.ai')
            O0000OOOOO000O000 =open (O00OO0OOOO00OO00O ,"r")
            O0OOO00OOO000O0O0 =O0000OOOOO000O000 .readline ().replace ("\n","").split (',')
            O0OOOOO0O0OOOOOO0 =O0OOO00OOO000O0O0 [2 ]+"/candidates/"+O0OOO00OOO000O0O0 [0 ]+"/activity-ping?token="+O0OOO00OOO000O0O0 [1 ];
            requests .get (O0OOOOO0O0OOOOOO0 )
        except Exception as OOO0O0OOO0OOOOOOO :
            print ("")

##################################################
## IMPORTANT:
## THIS FILE IS READ ONLY, DO NOT MODIFY IT IN ANY WAY AS THAT WILL RESULT IN A TEST FAILURE
##################################################        