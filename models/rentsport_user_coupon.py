import re, uuid, datetime                           # ← IMPORTS Python 

from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportUserCoupon(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.user.coupon'                   # ← NOMBRE TECNICO DEL MODELO
    _description = 'Codigos de altas de usuarios'     # ← NOMBRE LEGIBLE DEL MODELO

                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB

    codigo = fields.Char(string="Código",  size=12, required=True ) 
    codigo_usado =   fields.Boolean(string='¿Se ha usado?', default=False )
    fecha_validez =   fields.Date(string='Fecha de validez', required=True, default=fields.Date.context_today()+datetime.timedelta(days=+20))
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario')   