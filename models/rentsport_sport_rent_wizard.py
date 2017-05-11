# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, exceptions  # ← IMPORTS Odoo
import datetime
class RentSportRentWizard(models.Model):                # ← DEFINICION DE LA CLASE PYTHON
     _name = 'rentsport.sport.rent.wizard'              # ← NOMBRE TECNICO DEL MODELO
     _description = 'Instalaciones'  # ← NOMBRE LEGIBLE DEL MODELO
     _ids_ins=[]   # ← ARRAY IDS DE INSTALACIONES DISPONIBLES
     _ids_cup=[]   # ← ARRAY IDS DE CUPONES DISPONIBLES
                                                  # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
     fecha_inicio = fields.Date(string="Fecha de inicio")
     duracion = fields.Integer(string="Duracion en minutos", default="60")
     tipo_pista = fields.Many2one('rentsport.installation.type', string="Tipo de pista", onchange="_get_ids_instalaciones")
     cupones_disponibles = fields.Many2many(comodel_name='rentsport.user.coupon',onchange="_get_cupones", string="Cupones")
     pistas_disponibles2 = fields.Many2one(comodel_name='rentsport.sport.installation', string="Instalaciones2")
     pistas_disponibles = fields.Many2many(comodel_name='rentsport.sport.installation',onchange="_get_instalaciones",  string="Instalaciones")




                                                            # ↓ DEFINICION DE LOS METODOS


     @api.multi
     def reservar(self):

         for wizard in self:
             if int(wizard.duracion) < 1440:
               usuario_id = self._context.get('active_id')
               d1 = fields.Datetime.from_string(self.fecha_inicio)
               d2 = fields.Datetime.from_string(str(d1 + relativedelta(days=1)))


               for reserva_id in self._ids_ins:
                    if wizard.fecha_inicio and wizard.tipo_pista and int(wizard.duracion > 0):
                         rents = wizard.env['rentsport.sport.rent']
                         rec= rents.search([
                             ('fecha_inicio_alquiler', '>=', d1.strftime("%Y-%m-%d")),
                             ('fecha_fin_alquiler', '<', d2.strftime("%Y-%m-%d")),
                             ('instalacion', '=',reserva_id)],limit=1)


                         if len(rec)>0:
                             fecha = fields.Datetime.from_string(rec.fecha_fin_alquiler)
                         else:
                             fecha = fields.datetime.now()
                             fecha = fecha.replace(hour=0,minute=0,second=0, microsecond=0)


                         rent_vals = {
                              'fecha_inicio_alquiler': fecha,
                              'fecha_fin_alquiler': fecha + datetime.timedelta(minutes=int(wizard.duracion)),
                              'instalacion': int(reserva_id),
                              'usuario': int(usuario_id)
                         }
                         rent_id = wizard.env['rentsport.sport.rent'].create(rent_vals)
                    else:
                         raise exceptions.ValidationError('Compruebe que ha introducido una fecha o un tipo de pista o que la duracion sea mayor a 0.')

               for cupones_id in self._ids_cup:
                    rent_cupones = self.env['rentsport.user.coupon']
                    cupon = rent_cupones.search([('id','=',int(cupones_id))],limit=1)
                    cupon.write({'codigo_usado': 'usado'})

     @api.one
     @api.constrains('duracion')
     def _check_duration(self):
         if self.duration <= 0:
             raise exceptions.ValidationError('La duracion minimo tiene que ser mayor a 1 minuto.')

     @api.onchange('cupones_disponibles')
     def _get_cupones(self):
         del self._ids_cup[:]
         for id in  self.cupones_disponibles:
             self._ids_cup.append(int(id[0]))

     @api.onchange('pistas_disponibles')
     def _get_instalaciones(self):
         del self._ids_ins[:]
         for id in  self.pistas_disponibles:
             self._ids_ins.append(int(id[0]))

     @api.onchange('tipo_pista','fecha_inicio','duracion')
     def _get_ids_instalaciones(self):



                 if fields.Datetime.from_string(self.fecha_inicio) != None and self.tipo_pista and int(self.duracion>0):

                         d1 = fields.Datetime.from_string(self.fecha_inicio)

                         d2 = fields.Datetime.from_string(str(d1 + relativedelta(days=1)))
                         ids =[]

                         rents = self.env['rentsport.sport.rent']
                         instalaciones = self.env['rentsport.sport.installation']

                         for I in instalaciones.search([('tipo_pista','=',int(self.tipo_pista))]):
                             ids.append(I.id)
                         min = 0
                         for X in rents.search([('fecha_fin_alquiler', '<', d2.strftime("%Y-%m-%d")),('fecha_inicio_alquiler', '>=', d1.strftime("%Y-%m-%d")),('instalacion','in', ids)]):

                              min += (fields.Datetime.from_string(X.fecha_fin_alquiler)-fields.Datetime.from_string(X.fecha_inicio_alquiler)).seconds / 60

                              if min + int(self.duracion) >= 1440:
                                 ids.remove(int(X.instalacion))

                         if  int(self.duracion) < 1440:
                            self.pistas_disponibles = ids
                            self.pistas_disponibles2 = ids
                         else:
                             del ids[:]
                             self.pistas_disponibles = []



                         cids=[]
                         cupones = self.env['rentsport.user.coupon'].search([('fecha_validez', '>=', fields.Date.today()),('codigo_usado','=','activo'),('usuario_id','=',int(self._context.get('active_id')))],limit=4)
                         for C in cupones:
                                cids.append(C.id)
                         self.cupones_disponibles = cids

