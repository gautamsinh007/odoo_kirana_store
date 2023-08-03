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

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/products.xml',
        'views/csvdata.xml',
        'views/buyproducts.xml',
        'views/mail_templates.xml',
        'views/product_stock.xml',
        'views/purchase_data.xml',
        'views/products_quantity.xml',
        'views/mail_product.xml',
        'views/product_view.xml'
     
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3',
}



