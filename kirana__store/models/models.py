# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api
import smtplib
import csv
import base64, io


class Products(models.Model):
    _name = 'products.data'
    _description = 'products detailes'
    _order  =  'name'

    name  = fields.Char(string='name')


class Saledata(models.Model):
    _name = 'sale.data'
    _order  =  'name'
    
    name = fields.Char(string='name')
    productqty = fields.One2many('product.quality', 'saledata' , string='productqty')
    mail_send = fields.Char(string='your mail', default=lambda self: self.env.user.login)
    user = fields.Many2one('res.users', string='seller mail')
    date  = fields.Datetime(string='Need product')
    type = fields.Selection([('sale', 'Sale'),('purchase','Purchase')],string='Type')
    
    def check_orm(self):
        templates_id = self.env.ref('kirana__store.send_products_email_template').id
        tem = self.env['mail.template'].browse(templates_id)
        tem.send_mail(self.id, force_send=True)  
        
                        
class ProductQuality(models.Model):
    
    _name = 'product.quality'        
    
    product_id = fields.Many2one('products.data') 
    price = fields.Char(string='price')   
    qty  = fields.Char(string='qty')    
    saledata = fields.Many2one('sale.data', string='saledata')    
    type = fields.Selection([('sale', 'Sale'),('purchase','Purchase')],string='Type',related='saledata.type')
    
    
    
    
    
    
    
    
    
    
    
    