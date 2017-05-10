#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, uuid, datetime, codecs
from random import randint
from random import choice
import sys

reload(sys)
sys.setdefaultencoding('utf8') # para la codificacion de caracteres con tildes y ñ

os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
print(" Generar Alquileres...")
file = codecs.open("../demo/rents.xml", "w", "utf-8")
# file.write(codecs.BOM_UTF8)
dias =[]

file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
file.write("<odoo>\n")
file.write("\t<data>\n")




def diaparcial(file,vcb,fecha):

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha+ datetime.timedelta(minutes=randint(1,125))) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha+ datetime.timedelta(minutes=randint(126,300)))+"</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100))+"\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4))+"\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha + datetime.timedelta(minutes=randint(360,400)))+"</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=randint(401,700)))+"</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100))+"\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4))+"\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha+datetime.timedelta(minutes=randint(720,900))) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=randint(901,1020))) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha+datetime.timedelta(minutes=randint(1080,1200))) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=randint(1201,1440))) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1
        dias.append(fecha)
        return vcb


def diacompleto (file,vcb,fecha):
        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=360)) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write(
                "\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha + datetime.timedelta(minutes=360)) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=720)) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write(
                "\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha + datetime.timedelta(minutes=720)) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=1080)) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1

        file.write("\t\t<record id=\"sport_rent_test_" + str(vcb) + "\" model=\"rentsport.sport.rent\">\n")

        file.write("\t\t\t<field name=\"fecha_inicio_alquiler\">" + str(fecha + datetime.timedelta(minutes=1080)) + "</field>\n")
        file.write("\t\t\t<field name=\"fecha_fin_alquiler\">" + str(fecha + datetime.timedelta(minutes=1440)) + "</field>\n")
        file.write("\t\t\t<field name=\"instalacion\" ref=\"sport_installation_test_" + str(randint(1, 100)) + "\"/>\n")
        file.write("\t\t\t<field name=\"usuario\" ref=\"base.res_partner_" + str(randint(1, 4)) + "\"/>\n")

        file.write("\t\t</record>\n")
        vcb+=1
        dias.append(fecha)
        return vcb


vcb = 1

for I in range(0,999):
        fecha = datetime.datetime.today() + datetime.timedelta(days=+randint(-525,125))
        fecha = fecha.replace(hour=0,minute=0,second=0, microsecond=0)
        estado =""
        
        if not (fecha in dias):
                if choice([True, False]):
                 vcb=diacompleto(file,vcb,fecha)
                 estado="Completo"
                else:
                 vcb=diaparcial(file,vcb,fecha)
                 estado = "Parcial"
                print("Dia: " + estado + " Fecha de alquiler: "+ str(fecha))
        else:
                print("Fecha de alquiler: " + str(fecha)+" ya usada.")
       

file.write("\t</data>\n</odoo>\n")

file.close()

