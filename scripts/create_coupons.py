#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, uuid, datetime, codecs
from random import randint
from random import choice        
os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
print(" Generar cupones...")
file = codecs.open("coupons.xml", "w", "utf-8")
#file.write(codecs.BOM_UTF8)
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
file.write("<odoo>\n")
file.write("\t<data>\n")
vcb=1
for I in range(1,5):
    for F in range(randint(5,125)):
        file.write("\t\t<record id=\"user_coupon_test_"+str(vcb)+"\" model=\"rentsport.user.coupon\">\n\t\t\t<field name=\"codigo\">"+str(uuid.uuid4().hex)[:12]+"</field>\n\t\t\t<field name=\"codigo_usado\">"+str(choice([True, False]))+"</field>\n\t\t\t<field name=\"fecha_validez\" >"+str(datetime.date.today() + datetime.timedelta(days=+randint(-125,125)))+"</field>\n\t\t\t<field name=\"usuario_id\" ref=\"base.res_partner_"+str(I)+"\"/></record>\n")
        print("Registro: "+str(vcb))
        vcb+=1
        
        
file.write("\t</data>\n</odoo>\n")

     
file.close()