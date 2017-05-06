# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)



from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportRent(models.Model):                   # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.sport.rent'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Alquiler'                        # ← NOMBRE LEGIBLE DEL MODELO
    _order='fecha_fin_alquiler'
                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    fecha_inicio_alquiler = fields.Datetime(string="Fecha de inicio")
    fecha_fin_alquiler = fields.Datetime(string="Fecha de fin")
    instalacion = fields.Many2one('rentsport.sport.installation', string="Instalacion")
    usuario = fields.Many2one('res.partner', string="Arrendatario")