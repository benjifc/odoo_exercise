# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, api, exceptions  # ← IMPORTS Odoo

class RentSportRentWizard(models.Model):                # ← DEFINICION DE LA CLASE PYTHON
     _name = 'rentsport.sport.rent.wizard'              # ← NOMBRE TECNICO DEL MODELO
     _description = 'Instalaciones'                     # ← NOMBRE LEGIBLE DEL MODELO

                                                        # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
     fecha_inicio = fields.Datetime(string="Fecha de inicio")
     duracion = fields.Integer(string="Duracion en minutos")
     tipo_pista = fields.Many2one('rentsport.installation.type', string="Tipo de pista")
     instalaciones = fields.Many2one('rentsport.sport.installation', string="Instalaciones")
     pistas_disponibles = fields.Many2one('rentsport.sport.rent', string="Pistas disponibles")

                                                            # ↓ DEFINICION DE LOS METODOS


     def reservar(self):
          for reserva in self:
               cupon_vals = {
                    'codigo': str(uuid.uuid4().hex)[:12],  # generamos un UUID de 12 cifras
                    'codigo_usado': 'activo',
                    'fecha_validez': wizard.fecha_validez,
                    'usuario_id': self._context['parent_obj']
               }
               #nuevo_cupon_id = self.env['rentsport.user.coupon'].create(cupon_vals)

