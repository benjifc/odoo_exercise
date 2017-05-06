# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)



from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportInstallationType(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.installation.type'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Tipos de instalaciones'                 # ← NOMBRE LEGIBLE DEL MODELO
    _rec_name = 'nombre'
    _order = 'nombre'
                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    nombre = fields.Char(string="Tipo instalación")
    instalaciones = fields.Many2one('rentsport.sport.installation', string="Instalaciones")