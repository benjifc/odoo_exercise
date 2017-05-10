# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


from odoo import models, fields, api, exceptions    # ← IMPORTS


class ResPartner(models.Model):                     # ← DEFINICION DE LA CLASE PYTHON
    _inherit =  'res.partner'                       # ← NOMBRE TECNICO DEL MODELO QUE HEREDA

                                                    # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    es_usuario = fields.Boolean(string='¿es usuario?')
    cupones_ids = fields.One2many(comodel_name='rentsport.user.coupon', inverse_name='usuario_id', string='Cupones')
    #sport_rent_ids = fields.One2many(comodel_name='rentsport.sport.rent', inverse_name='usuario_id', string='Reservas')
    total_user_coupons = fields.Integer(string='Total cupones', compute='_get_total_user_coupons')
    total_user_rents = fields.Integer(string='pistas alquiladas', compute='_get_total_user_rents')
    total_user_rents_reservations = fields.Integer(string='Reservas', compute='_get_total_user_rents_reservations')

    @api.one
    def _get_total_user_coupons(self):
        self.total_user_coupons = len(self.env['rentsport.user.coupon'].search([('usuario_id', '=', self.id)]))

    @api.one
    def _get_total_user_rents(self):
        self.total_user_rents = len(self.env['rentsport.sport.rent'].search([('usuario', '=', self.id)]))

    @api.one
    def _get_total_user_rents_reservations(self):
            self.total_user_rents_reservations = len(self.env['rentsport.sport.rent'].search([('usuario', '=', self.id),('fecha_inicio_alquiler', '>=', fields.Datetime.now())]))


    @api.multi
    def open_user_coupons(self):
        for obj in self:
            return {
                'name': 'Cupones de usuario',
                'view_type': 'tree',
                'view_mode': 'calendar',
                'res_model': 'rentsport.user.coupon',
                'domain': [('usuario_id','=', obj.id)],
                'type': 'ir.actions.act_window',
            }
    @api.multi
    def open_user_new_coupons(self):
        for obj in self:
            return {
                'name': 'Nuevo cupon',
                'view_type': 'tree',
                'view_mode': 'form',
                'res_model': 'rentsport.new.user.coupon.wizard',
                'context': {'parent_obj': obj.id},
                'type': 'ir.actions.act_window',
                'target': 'new'
            }

    @api.multi
    def open_user_new_rent(self):
        for obj in self:
            return {
                'name': 'Nuevo Alquiler',
                'view_type': 'tree',
                'view_mode': 'form',
                'res_model': 'rentsport.sport.rent.wizard',
                'context': {'rentsport_sport_rent_wizard_user_context': obj.id},
                'type': 'ir.actions.act_window',
                'target': 'new'
            }






    