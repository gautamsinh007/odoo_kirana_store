# -*- coding: utf-8 -*-
{
    'name': "Kirana_Store",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        
        Grocery store   
        A grocery store (AE), grocery shop (BE) or simply grocery is a retail store that primarily retails a general range of food products, which may be fresh or packaged 
    """,

    'author': "Gautamsinh Makwana",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
   

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml'
    ],  
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images':['static/description/a.jpeg']
}
