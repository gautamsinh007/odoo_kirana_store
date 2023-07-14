{
    
    
     'name' : 'Certificate',
     'summary':"Student Certificate System",
     'sequence': 5,
     'description' : 'This is Institute of Certificate  management sysytem software suport in odoo v31',
     'depends' : ['base', 'sale'],
     'author' : "Gautamsinh Makwana",
    #  'image' : [ ]    add image path hear in thsi use images
    
      'data' : [
          
        "security/ir.model.access.csv",
        "views/certificate_genrate.xml",
        "views/demo.xml",
        "views/website_form.xml",
        "views/democheck.xml",
        "views/demoform.xml",
        "views/sale_order_view.xml"
        # "views/inhertipage.xml"
        
      ],
      
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3',
    
    'assets': {
      
      'web.assets_backend': [
        'sinstitute_certificate/static/src/css/abc.css'
         
      ]
      
     }
}

