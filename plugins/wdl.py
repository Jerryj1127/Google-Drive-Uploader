import os
import subprocess
from urllib.parse import unquote

def wget_dl(url):
        try:
            print("Downloading Started")
            # i was facing some problem in filename That's Why i did this ,
            #  i will fix it later :(

            filename = unquote(url.split('/')[-1])
            output = subprocess.check_output("wget '--output-document' '{}' '{}' ".format(filename , url), stderr=subprocess.STDOUT, shell=True)
            
            print("Downloading Complete",filename)
            return filename
        except Exception as e:
            print("DOWNLAOD ERROR :",e)
           
            return "error",filename
        
# wget_dl(url)
