# -*- coding: utf-8 -*-
import os
import sys
import time
import itertools

"""
Raj bi mAy firend

How to identify Twitter user ids without making a request to Twitter?

@ Locard Conference 2017 
"""

def enum(**enums):
    return type('Enum', (), enums)
	
def kaydet(Ad,Top):
	try:
	
		if not os.path.exists("rehber/"):
			os.makedirs("rehber/")
			
		with open("rehber/"+str(Ad), "wb") as mf:
			mf.write("Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,E-mail 1 - Type,E-mail 1 - Value,Phone 1 - Type,Phone 1 - Value\n"+Top)
	except:
		return ""
	
	
"""
Add to your country code area
"""
Ulke 	= enum(TR=90,UK=44,DE=49,PL=48)

def numaraUret(Ulke,OP, SonRakam):
	Uretim 		= itertools.product(xrange(10), repeat=5)
	#MaxUretilen = len(list(itertools.product(xrange(10), repeat=5)))
	Art 		= 0
	Sayfa		= 1
	#Total		= 0
	Top 		= ""
	for Combination in Uretim:
		Art = Art + 1
		#Total = Total  + 1
		Top = Top + str(",,,,,,,,,,,,,,,,,,,,,,,,,,* My Contacts,* Home,,Mobile,+")+ str(Ulke) + str(OP) + ''.join(map(str, Combination)) + str(SonRakam) + "\n"
		if Art == 5000:
			kaydet("rehber-"+str(SonRakam)+"_"+str(Sayfa)+".csv", Top)
			Sayfa = Sayfa + 1
			Top = ""
			Art = 0
		

numaraUret(Ulke.UK,"777","99")


