import sys
import os
import ftplib

verbose = 1
ip = “xx.xx.xx.xx”
tags = [“tag1”,”tag2”]

def openFtp(ip):
    try:
        if verbose >=1:
            print “openFtp function”
        ftp = ftplib.FTP(ip)
        if verbose >=2:
            ftp.set_debuglevel(2)
        ftp.login("anonymous")
        openPath(ftp)
    except:
        print "Error server connection”    

def openPath(ftp):    
    
    files = []
         
    try:
        if verbose>=2:
            print "Provo ad elencare: " + ftp.pwd()
        files = ftp.nlst() #Error with empty dir
    except ftplib.error_perm, resp:
        if str(resp) == "550 No files found":
            print "No files in this directory"
        else:
            raise

    for f in files:
        try:
            if verbose>=2:
                print “Try to open: " + f
            ftp.cwd(str(f))
            if verbose >= 1:
            #print str(f) + " is a dir”
                print "DIR - " + ftp.pwd()
            openPath(ftp)
        except:
            if verbose >= 1:
                print "FILE - " + ftp.pwd() +"/" + f
            for tag in tags:
            
                if tag in str(f):
                    print “Found file with tag " + tag + " --> " + f
                    log = open("log_tag_" +ip+".txt", "a")
                    log.write(“Found file with tag " + tag + " --> " + ftp.pwd() +"/"+ f + "\n")
                    log.close
            #print f + " isn’t a dir”  
    ftp.cwd("../")             
        
def main():
    openFtp(ip)
    
if __name__ == "__main__":
    main()	
            