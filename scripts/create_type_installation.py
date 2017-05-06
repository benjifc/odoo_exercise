#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, uuid, datetime, codecs
from random import randint
from random import choice
import sys

reload(sys)
sys.setdefaultencoding('utf8') # para la codificacion de caracteres con tildes y ñ
os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo

print(" Generar tipo instalaciones ...")
dxt = ['Futbol','Futbol sala', 'Baloncesto','Balonmano','Padel','Tenis','Fronton','Voleibol','Natacion','Atletismo','Tiro al plato','Tiro olimpico','Tiro con arco','Rocodromo']
file = codecs.open("../demo/installationType.xml", "w", "utf-8")
# file.write(codecs.BOM_UTF8)
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
file.write("<odoo>\n")
file.write("\t<data>\n")
vcb = 1
for obj in dxt:
        file.write("\t\t<record id=\"rentsport_installation_type_" + str(vcb) + "\" model=\"rentsport.installation.type\">\n\t\t\t<field name=\"nombre\">" + obj + "</field>\n\t\t</record>\n")
        print("Registro: " + str(vcb) + " instalacion: " + obj)
        vcb += 1
file.write("\t</data>\n</odoo>\n")

file.close()