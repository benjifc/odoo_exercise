# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import re, uuid
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


   



                                                    # ↓ DEFINICION DE LOS METODOS PRIVADOS



    def  ValidarEmail(self,email):
        pattern = re.compile("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$")

        if pattern.match(email):
            return True
        else:
            raise exceptions.Warning('Correo Electronico No Valido', 'Porfavor introduzca una direccion de correo electronico valida')

    def crear_usuario(self):
        for wizard in self:
            usuario_vals = {
                'name': wizard.nombre,
                'phone': wizard.telefono,
                'email': wizard.email,
                'es_usuario':True
            }


            nuevo_usuario_id = self.env['rentsport.res.partner'].create(session_vals)
            cupon_vals = {
               'codigo': str(uuid.uuid4().hex)[:12],
               'codigo_usado' : False,
               'usuario_id': nuevo_usuario_id
            }


            nuevo_cupon_id = self.env['rentsport.user.coupon'].create(session_vals)

