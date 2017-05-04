# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import re, uuid, datetime                           # ← IMPORTS Python

from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportUserCoupon(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.user.coupon'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Codigos de altas de usuarios'     # ← NOMBRE LEGIBLE DEL MODELO

                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB

    codigo = fields.Char(string="Código",  size=12, required=True ) 
    codigo_usado =   fields.Boolean(string='¿Se ha usado?', default=False )
    fecha_validez =   fields.Date(string='Fecha de validez', required=True)
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario', ondelete="cascade", domain=[('es_usuario','=', True)])