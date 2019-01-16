# -*- coding: iso-8859-1 -*-
#! /usr/bin/python

"""BCAdirecto account Balance Display (default account)"""
__author__ = ""
__copyright__ = ""
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Production"

# TODO - Get user account if more than one and work with...

import urllib3
import sys #basics (main...)
import re #regular expression
import mechanize as mec #browser...
import getpass #read password (hidden input)
 
#//BCA Directo Services URL's
BCALoginRoot = 'https://bcadirecto.bca.cv/Login/login.aspx'
BCATransationUrl = "https://bcadirecto.bca.cv/Transaccoes/transaccao.aspx?idc=142&idsc=181&idl=1"

#Cells with Balances
cellStart,cellEnd = '<span style="white-space:nowrap">','</span>'

#function to process login and read balance 
def check(user, passw):
  br = mec.Browser()
  br.set_handle_robots(False) # ignore robots
  br.open(BCALoginRoot) #open login url
  br.select_form(name="aspnetForm") #get login form
  
  #set credentials
  br["ctl00$ctl00$Utilizador"] = user
  br["ctl00$ctl00$Password"] = passw
  
  #login
  res = br.submit()
  
  if(res != False):
    res = br.open(BCATransationUrl) #get transactions
    
    if res != False:
      d = str(res.read()) #read data
      
      #print d
      #regular expression to extract balance cell data
      res = re.findall(cellStart + '(.+?)' + cellEnd, d)
      
      if res:
        print ("Saldo contabilistico\t: " + res[0])
        print ("Saldo Disponivel\t: " + res[1])
	
  print ("Good bye!")
  exit(0)
def header():
  print ("checkbca.py -1.0\n\rRead your BCA online account balance")

#main program
def main(argv):
  user,passw = '',''
  header()  
  user = raw_input("BCA Directo Username: ")
  passw = getpass.getpass()
  
  print ("Reading Balance, please wait...")
  check(user, passw)
  
if __name__ == "__main__":
  main(sys.argv[1:])