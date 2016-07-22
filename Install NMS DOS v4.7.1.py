import sys
import time
import urllib
import urllib2
import tkMessageBox as tkmb

def download():
    confirm = tkmb.askyesno('Install NMS DOS', 'Are you sure you want to install NMS DOS Version 4.7.1?')
    if confirm == True:
        conf2 = tkmb.askokcancel('Install NMS DOS', 'Click continue to install NMS DOS Version 4.7.1')
        if conf2 == True:
            url = 'http://tgt-gaming.weebly.com/uploads/7/5/6/4/75640241/nms_dos_v4.7.1.py'
            connect = False
            try:
                response=urllib2.urlopen('http://example.com',timeout=2)
                connect = True
            except urllib2.URLError as err: pass

            if connect == True:
                print 'URL is ' + str(url)
                print "downloading with urllib"
                urllib.urlretrieve(url, "NMS DOS v4.6.py")
                time.sleep(4)
                tkmb.showinfo('Install NMS DOS', 'The install was succesful. \rClick OK to exit.')
                sys.exit
            else:
                conf3 = tkmb.askretrycancel('Install NMS DOS', 'The installation failed. \rError NO_INTERNET_CONNECTION.')
                if conf3 == True:
                    download()
                else:
                    tkmb.showerror('Install NMS DOS', 'Click OK to exit.')
                    sys.exit
        else:
            tkmb.showerror('Install NMS DOS', 'The installation failed. \rClick OK to exit.')
            sys.exit
    else:
        tkmb.showerror('Install NMS DOS', 'The installation failed. \rClick OK to exit.')
        sys.exit

download()
