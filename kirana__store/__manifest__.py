# -*- coding: utf-8 -*-
{
    'name': "Grocery Store With Whatsapp",
    'sequence': 3,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "Kirana stores are shops that serve daily needs products and commonly used grocery items",
   'summary': 'Grocery Store are shops that serve daily needs products and commonly used grocery items',     
        
    'author': "Gautamsinh Makwana",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
   
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml', 
        'views/products.xml',
        'views/sale_data.xml',
        'views/mail_product.xml',
        'views/product_quantity.xml',
    ],  
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'images':['static/description/h.gif'],
    'icon':['static/description/icon.png','static/description/rr.png'],
      
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3'
    
}
