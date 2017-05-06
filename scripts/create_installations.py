#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, uuid, datetime, codecs
from random import randint
from random import choice
import sys

reload(sys)
sys.setdefaultencoding('utf8') # para la codificacion de caracteres con tildes y ñ

os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
print(" Generar instalaciones...")
file = codecs.open("../demo/installations.xml", "w", "utf-8")
# file.write(codecs.BOM_UTF8)
instalacion = [  "Et LLC",  "Nulla In Tincidunt Corporation",  "Parturient Montes Nascetur Associates",  "Lectus Ante Dictum PC",  "Euismod Enim Etiam Consulting",  "Fusce Aliquam Institute", "Felis Eget Incorporated",  "Felis Purus Corp.",  "Curae; Donec LLP",  "Velit Foundation",  "Non Consulting",  "Erat Vivamus Inc.",  "Pellentesque Inc.",  "Aliquam Corporation",  "Vitae Erat Vivamus Associates",  "Porttitor Tellus Non Limited",  "Lacus Corporation",  "Mauris Ut Foundation",  "Ligula Inc.",  "Pellentesque Eget LLC",  "Tincidunt Vehicula Risus Consulting",  "Turpis Vitae Purus Industries",  "Cursus Industries",  "Erat Industries",  "Curabitur Company",  "Aliquam Institute",  "Magnis Dis Associates",  "Nibh Inc.",  "Placerat LLP",  "Tortor Industries",  "Ullamcorper Nisl Institute",  "Euismod Est Arcu Industries",  "Tincidunt Pede Ac Consulting",  "Amet Faucibus Ut Industries",  "Vestibulum Limited",  "Scelerisque LLC",  "Ipsum Foundation",  "Non Leo Limited",  "Dolor Dapibus PC",  "Vestibulum Industries",  "Suspendisse Ac Metus Inc.",  "Ornare Fusce PC",  "Cras Dictum LLC",  "Elit Erat Corporation",  "Lorem Tristique Foundation",  "Ante Maecenas Mi Corp.",  "Non Ante Bibendum PC",  "Tellus Faucibus Incorporated",  "Blandit Consulting",  "Vivamus Sit Amet Institute",  "Duis PC",  "Suspendisse Tristique Neque Inc.",  "Sagittis Lobortis Mauris Company",  "Ullamcorper Viverra Industries",  "Suspendisse Eleifend Foundation",  "Consequat Associates",  "Venenatis A Associates",  "Vitae Nibh Donec Ltd",  "Cursus Diam At Ltd",  "Ipsum Company",  "Molestie Arcu Sed Corporation",  "Magna Industries",  "Elit Pede Company",  "Non Enim Associates",  "Diam Proin Company",  "Proin Ultrices Duis Foundation",  "Pede Ac Urna LLC",  "Quisque Libero PC",  "Fringilla Porttitor Vulputate Industries",  "Et Magnis Institute",  "Nec Consulting",  "Nullam Corp.",  "Ante Bibendum Inc.",  "Senectus Et Inc.",  "Vitae Corp.",  "Vitae Institute",  "Aenean Euismod Incorporated",  "Aliquam Eros Limited",  "Aliquet Molestie LLC",  "In Scelerisque Scelerisque Company",  "Est LLC",  "Felis Consulting",  "Quisque Industries",  "Cursus Diam At LLP",  "Aenean Limited",  "Turpis Vitae Purus Corporation",  "Fringilla Cursus Company",  "Ante Vivamus Non LLP",  "Risus Donec Nibh LLC",  "Ante Blandit Viverra Institute",  "Luctus Lobortis PC",  "Parturient Company",  "Nullam LLC",  "Diam Incorporated",  "Eu Ultrices Sit Incorporated",  "Ullamcorper Velit Incorporated",  "Consectetuer PC",  "Ipsum Company",  "Lorem Ipsum Sodales Industries",  "Lacus Cras Interdum Foundation" ]
pueblos = ["Aguadulce","Alanís","Albaida del Aljarafe","Alcalá de Guadaíra","Alcalá del Río","Alcolea del Río","La Algaba","Algámitas","Almadén de la Plata","Almensilla","Arahal","Aznalcázar","Aznalcóllar","Badolatosa","Benacazón","Bollullos de la Mitación","Bormujos","Brenes","Burguillos","Las Cabezas de San Juan","Camas","La Campana","Cantillana","Cañada Rosal","Carmona","Carrión de los Céspedes","Casariche","Castilblanco de los Arroyos","Castilleja de Guzmán","Castilleja de la Cuesta","Castilleja del Campo","El Castillo de las Guardas","Cazalla de la Sierra","Constantina","Coria del Río","Coripe","El Coronil","Los Corrales","El Cuervo de Sevilla","Dos Hermanas","Écija","Espartinas","Estepa","Fuentes de Andalucía","El Garrobo","Gelves","Gerena","Gilena","Gines","Guadalcanal","Guillena","Herrera","Huévar del Aljarafe","Isla Mayor","La Lantejuela","Lebrija","Lora de Estepa","Lora del Río","La Luisiana","El Madroño","Mairena del Alcor","Mairena del Aljarafe","Marchena","Marinaleda","Martín de la Jara","Los Molares","Montellano","Morón de la Frontera","Las Navas de la Concepción","Olivares","Osuna","Los Palacios y Villafranca","Palomares del Río","Paradas","Pedrera","El Pedroso","Peñaflor","Pilas","Pruna","La Puebla de Cazalla","La Puebla de los Infantes","La Puebla del Río","El Real de la Jara","La Rinconada","La Roda de Andalucía","El Ronquillo","El Rubio","Salteras","San Juan de Aznalfarache","San Nicolás del Puerto","Sanlúcar la Mayor","Santiponce","El Saucejo","Sevilla","Tocina","Tomares","Umbrete","Utrera","Valencina de la Concepción","Villamanrique de la Condesa","Villanueva de San Juan","Villanueva del Ariscal","Villanueva del Río y Minas","Villaverde del Río","El Viso del Alcor"]
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
file.write("<odoo>\n")
file.write("\t<data>\n")
vcb = 1
for I in instalacion:
        ubicacion = str(choice(pueblos))
        print("Registro: " + str(vcb) + "\n\tEmpresa: " + I + "\n\tPoblacion: " + ubicacion)
        file.write("\t\t<record id=\"sport_installation_test_" + str(vcb) + "\" model=\"rentsport.sport.installation\">\n\t\t\t<field name=\"nombre\">" + I + "</field>\n\t\t\t<field name=\"ubicacion\">" + ubicacion + "</field>\n\t\t\t<field name=\"tipo_pista\" ref=\"rentsport_installation_type_" + str(randint(1, 12))+"\"/>\n\t\t</record>\n")

        vcb += 1

file.write("\t</data>\n</odoo>\n")

file.close()
