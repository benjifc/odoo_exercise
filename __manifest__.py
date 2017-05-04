# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Modulo Rent Sport',
    'version': '1.0',
    'description':'Gestión de instalaciones deportivas',
    'author':'Benjamín Fdez. Carrasco',
    'website':'https://www.linkedin.com/in/benjifc/',
    'category' : 'Rent',
    'license' : 'AGPL-3',
    'description': """
                    Permitirá al usuario final realizar la gestión completa de las instalaciones, 
                    así como las reservas a las mismas y los usuarios que pueden reservar pistas.
            """,
    'data' : [ 
        'views/rentsport_new_user_wizard.xml',
        'views/rentsport_users.xml',
        'views/rentsport_menus.xml'  
    ],
    'demo':[
        'demo/rest_partner.xml'
    ],
    'installable': True,
    'active': False

}
