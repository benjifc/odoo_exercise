# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import datetime

from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportRent(models.Model):                   # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.sport.rent'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Alquiler'                        # ← NOMBRE LEGIBLE DEL MODELO
    _order='fecha_fin_alquiler desc'

                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    fecha_inicio_alquiler = fields.Datetime(string="Fecha de inicio")
    fecha_fin_alquiler = fields.Datetime(string="Fecha de fin")
    instalacion = fields.Many2one('rentsport.sport.installation', string="Instalacion")
    usuario = fields.Many2one('res.partner', string="Arrendatario")
    minutos = fields.Integer(string='Duracion min.', compute='_get_duration_in_minutes')

    @api.one
    def _get_duration_in_minutes(self):
        diff = fields.Datetime.from_string(self.fecha_fin_alquiler) - fields.Datetime.from_string(self.fecha_inicio_alquiler)
        self.minutos = (diff.seconds) / 60


