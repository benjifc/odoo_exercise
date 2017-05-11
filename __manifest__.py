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
    'depends':['report'],
    'data' : [
        'demo/users.xml',
        'demo/coupons.xml',
        'demo/installationType.xml',
        'demo/installations.xml',
        'demo/rents.xml',
        'views/rentsport_new_user_wizard.xml',
        'views/rentsport_new_user_coupon_wizard.xml',
        'views/rentsport_coupons.xml',
        'views/rentsport_users.xml',
        'views/rentsport_sport_installations.xml',
        'views/rentsport_sport_rent_wizard.xml',
        'views/rentsport_sport_rents.xml',
        'views/rentsport_menus.xml',
        'reports/coupon.xml',
        'reports/coupon_template.xml'

    ],
    'demo':[

    ],
    'installable': True,
    'active': False

}
