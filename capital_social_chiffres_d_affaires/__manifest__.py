# -*- coding: utf-8 -*-
{
    'name': "capital_social_chiffres_d_affaires",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Eufonie DEV",
    'website': "https://www.eufonie.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm','donnees_administratives'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        "static/description/icon.png"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}