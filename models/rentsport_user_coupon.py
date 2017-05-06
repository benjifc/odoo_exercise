# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import re, uuid, datetime                           # ← IMPORTS Python

from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportUserCoupon(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.user.coupon'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Codigos de altas de usuarios'     # ← NOMBRE LEGIBLE DEL MODELO
    _order = 'fecha_validez'
                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB

    codigo = fields.Char(string="Código",  size=12, required=True ) 
    codigo_usado =  fields.Selection(selection=[('usado','Usado'),('activo','Activo')],string='Estado', default='activo')

    fecha_validez =   fields.Date(string='Fecha de validez', required=True)
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario', ondelete="cascade", domain=[('es_usuario','=', True)])
    total_coupons_without_use = fields.Integer(string='Total cupones sin uso', compute='_get_total_coupons_without_use')
    total_coupons_with_use = fields.Integer(string='Total cupones sin uso', compute='_get_total_coupons_with_use')


    @api.one
    def _get_total_coupons_without_use(self):
        self.total_coupons_without_use = len(self.search([('fecha_validez', '&gt;=', (datetime.date.today()).strftime('%%Y-%%m-%%d 00:00:00')),('codigo_usado','=','activo')]))

    @api.one
    def _get_total_coupons_with_use(self):
        self.total_coupons_with_use = len(self.search([('codigo_usado', '=', 'usado')]))


