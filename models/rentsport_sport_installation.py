# -*- coding: utf-8 -*-
# Copyright 2017 Benjamín Fernández Carrasco
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)



from odoo import models, fields, api, exceptions    # ← IMPORTS Odoo


class RentSportInstallation(models.Model):                  # ← DEFINICION DE LA CLASE PYTHON
    _name = 'rentsport.sport.installation'                  # ← NOMBRE TECNICO DEL MODELO
    _description = 'Instalaciones'                          # ← NOMBRE LEGIBLE DEL MODELO
    _rec_name = 'nombre'
    _order = 'nombre'
                                                      # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    nombre = fields.Char(string="Nombre instalación")
    ubicacion = fields.Char(string="Ubicación")
    tipo_pista = fields.Many2one('rentsport.installation.type',string="Tipo de pista")