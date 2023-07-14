from odoo import fields , models , api,_
from odoo.exceptions import ValidationError, UserError
# import  datetime 
from datetime import date, datetime

class StudentCertificate(models.Model):
    _name = "certificate.student"
    _rec_name = 'email'
    _order  =  'name asc' # 'name desc'
    _description = "this is scholl management model"
   
   
    name = fields.Char(string="name")
    place = fields.Char(string="palce")
    email = fields.Char(string="email")
    states = fields.Char(string="states")
    language = fields.Char(string="language")
    country_id = fields.Many2one('res.country', string='Country')
    images = fields.Binary(string="images")
    datetime  = fields.Date(string='defult date', default=lambda self: date.today())
    defult_datetime  = fields.Date(string='defultsdate',default=lambda self: datetime.now())
    login_user  = fields.Many2one('res.users',string='User',default=lambda self: self.env.user.id)
    user_company = fields.Many2one('res.company', string='company',default=lambda self: self.env.company.id)
    activate  = fields.Boolean(string='Active', default=True)
    
     
    def call_by_menu(self):
        print("call python fucntion  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
    #  if  name is existing  in db  
    @api.constrains('name')
    def _check_unique_name(self):
        product = self.search([('id', '!=', self.id) , ('name', '=ilike', self.name)])
        print(product,"product_______")
        if product:
            raise ValidationError(_('name already exists!'))
      



# class Salesadddtaa(models.Model):
#     _inherit = "sale.order"            
    
    
#     place = fields.Char(string="palce")

            

# class Salesorderline(models.Model):
#     _inherit = "sale.order.line"            
    
    
#     newthigs = fields.Char(string="newthigs")