# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


from odoo import models, fields, api, exceptions    # ← IMPORTS


class ResPartner(models.Model):                     # ← DEFINICION DE LA CLASE PYTHON
    _inherit =  'res.partner'                       # ← NOMBRE TECNICO DEL MODELO QUE HEREDA

                                                    # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    es_usuario = fields.Boolean(string='¿es usuario?')
    cupones_ids = fields.One2many(comodel_name='rentsport.user.coupon', inverse_name='respartner_id', string='Cupones')

    





    