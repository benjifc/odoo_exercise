# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import  uuid, datetime, re
from odoo import models, fields, api, exceptions    # ← IMPORTS


class RentSportNewUserCouponWizard(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.new.user.coupon.wizard'                 # ← NOMBRE TECNICO DEL MODELO
    _description = 'Nuevo cupon'                               # ← NOMBRE LEGIBLE DEL MODELO


                                                               # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB

 

    fecha_validez =   fields.Date(string='Fecha de validez', required=True)


   



                                                    # ↓ DEFINICION DE LOS METODOS


    def crear_cupon(self):
        for wizard in self:
            cupon_vals = {
               'codigo': str(uuid.uuid4().hex)[:12], # generamos un UUID de 12 cifras
               'codigo_usado' : 'activo',
               'fecha_validez' : wizard.fecha_validez,
               'usuario_id': self._context['parent_obj']
            }
            nuevo_cupon_id = self.env['rentsport.user.coupon'].create(cupon_vals)

