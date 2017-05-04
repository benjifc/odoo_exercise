# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import  uuid, datetime, re
from odoo import models, fields, api, exceptions    # ← IMPORTS


class RentSportNewUserWizard(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.new.user.wizard'                       # ← NOMBRE TECNICO DEL MODELO
    _description = 'Alta de nuevos usuarios'        # ← NOMBRE LEGIBLE DEL MODELO

                                                    # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB

 
    nombre = fields.Char(
        string='Nombre',
        required=True,
        help="introduzca su nombre de usuario, porfavor"
    )


    telefono  = fields.Char (
        string='Telefono',
        required=True,
        help="introduzca su telefono, porfavor"
    ) 


    email  = fields.Char (
        string='Correo electronico',
        required=True,
        help="introduzca su direccion de correo electronico, porfavor"
    ) 


   



                                                    # ↓ DEFINICION DE LOS METODOS

    # Restrinciones

    ###########################################################################################################################################
    @api.one
    @api.constrains('email')
    def  _check_email(self):
        pattern = re.compile("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$")

        if pattern.match(str(self.email)):
            return True
        else:
            raise  exceptions.ValidationError("Correo Electronico No Valido,Porfavor introduzca una direccion de correo electronico valida")
    ###########################################################################################################################################

    def crear_usuario(self):
        for wizard in self:
            usuario_vals = {
                'name': wizard.nombre,
                'display_name': wizard.nombre,
                'phone': wizard.telefono,
                'email': wizard.email,
                'es_usuario':True
            }

            nuevo_usuario_id = self.env['res.partner'].create(usuario_vals)

            cupon_vals = {
               'codigo': str(uuid.uuid4().hex)[:12], # generamos un UUID de 12 cifras
               'codigo_usado' : False,
               'fecha_validez' : datetime.date.today() + datetime.timedelta(days=+20), # Creamos el cupon con vente días más de la fecha de creación
               'usuario_id': nuevo_usuario_id.ids[0]
            }
            nuevo_cupon_id = self.env['rentsport.user.coupon'].create(cupon_vals)

