# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api
import smtplib
import csv
import base64, io
from odoo.exceptions import ValidationError
import urllib.parse

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
    phone =  fields.Char(string='Enter Your Number',required = True)
    images = fields.Binary(string="images") 
    totle = fields.Float(string='totle' ,compute = 'calc_ctc')
     
    @api.depends("productqty")
    def calc_ctc(self):
        dd = []
        for record in self:
            x = record.productqty
            for ii in x:
                d = ii.price 
                qty = ii.qty
                x = int(qty)*d 
                dd.append(x)               
        ctc = sum(dd)
        record.totle = ctc
                    

    def check_orm(self):
        templates_id = self.env.ref('kirana__store.send_products_email_template').id
        tem = self.env['mail.template'].browse(templates_id)
        tem.send_mail(self.id, force_send=True)  
    
    
    
    def share_whatsapp(self):
        if not self.phone:
            return ValidationError('Missign Phone Number')
        
        phone = urllib.parse.quote(self.phone)
        msg = urllib.parse.quote("hi how are you....")

        return {
            'type': 'ir.actions.act_url',
            'url' : f'https://api.whatsapp.com/send?phone={phone}&text={msg}'
        }
        
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamic_domain', False):
            domain = self._get_dynamic_domain()
            args = domain
        return super(Saledata, self).search(args, offset=offset, limit=limit, order=order, count=count)


    @api.model
    def _get_dynamic_domain(self):
        domain = [('mail_send', '=', self.env.user.login)]
        return domain      
        
                 
class ProductQuality(models.Model):
    
    _name = 'product.quality'        
    
    product_id = fields.Many2one('products.data') 
    price = fields.Integer(string='price')   
    qty  = fields.Char(string='Quality' , required = True)    
    saledata = fields.Many2one('sale.data', string='saledata')    
    login_user = fields.Char(string='login_user', default=lambda self: self.env.user.login )
    type = fields.Selection([('sale', 'Sale'),('purchase','Purchase')],string='Type',related='saledata.type')
    totle = fields.Float(string='totle' , compute = 'calc_ctcs')
       
       
    @api.depends('qty', 'price')
    def calc_ctcs(self):
        # dd = []
        for ii in self:
            # if int(qty):
            d = ii.price 
            qty = ii.qty
            # if qty  and d:
            x = int(qty) * d 
            ii.totle = x   
           
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamic_domains', False):
            domain = self._get_dynamic_domains()
            args = domain
        return super(ProductQuality, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def _get_dynamic_domains(self):
        domain = [('login_user', '=', self.env.user.login)]
        return domain     
    