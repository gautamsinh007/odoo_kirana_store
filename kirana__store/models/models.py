# -*- coding: utf-8 -*- thsis si si snew add 
from odoo import models, fields, api


class Products(models.Model):
    _name = 'products.data'
    _description = 'products detailes '
    _order  =  'product_name'
    
    product_name  = fields.Char(string='product_name')
    quantity = fields.Char(string='quantity', null=True) 
    
    
class Buyproducts(models.Model):
    _name = 'products.buy'
    _description = 'products buy detailes '      
    _order  =  'groceries'
            
    groceries = fields.Many2many('products.data', string='groceries')      
    user = fields.Many2one('res.users', string='user')
    mail_send = fields.Char(string='mail_send', default=lambda self: self.env.user.login)
    
    def check_orm(self):
        templates_id = self.env.ref('kirana__store.products_send_email_template').id
        tem = self.env['mail.template'].browse(templates_id)
        tem.send_mail(self.id, force_send=True)   