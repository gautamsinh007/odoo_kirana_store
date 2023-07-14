# -*- coding: utf-8 -*-
{
    'name': "Kirana_Store",
    'sequence': 5,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/products.xml',
        'views/csvdata.xml'
        
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3',
}
