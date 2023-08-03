# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api
import smtplib
import csv
import base64, io
from odoo.exceptions import ValidationError, UserError

# class kirana__store(models.Model):
#     _name = 'kirana__store.kirana__store'
#     _description = 'kirana__store.kirana__store'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Products(models.Model):
    _name = 'products.data'
    _description = 'products detailes'
    _order  =  'product_name'

    product_name  = fields.Char(string='product_name')
    quantity = fields.Char(string='quantity', null=True)



    # product_price = fields.Integer()
    # abc = fields.Integer()
    # product_quntity = fields.Integer()
    # totel = fields.Integer(compute="_value_pc", store=True)
    # groceries = fields.Many2many('csvfile.load', string='groceries')
    
    
    @api.depends('product_price','product_quntity')
    def _value_pc(self):
        for rec in self:
            ctc = 0
            if rec.product_price:
                ctc += rec.product_price 
            if rec.product_quntity:
                ctc *= rec.product_quntity 
            rec.totel = ctc
    
    
        # def send_email(self):
    #     x =self.groceries
    #     search_var  = {"Product Name":self.product_name, "Product Groceries":self.product_quntity, "Product Quntity":self.product_quntity, "Totle":self.totel}
    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     s.starttls()
    #     s.login("gautamsinh987@gmail.com", "enter your email password")
    #     message = f"Product Name {self.product_name} \n Product price {self.product_quntity} \n Product quntity {self.product_quntity}\n Product totel {self.totel}" 
    #     s.sendmail("gautamsinh987@gmail.com", 'makwanagautam199@gmail.com',message)
    #     s.quit()
    #     print(search_var,'-=-=-=-=-')
    
    
class Productdata(models.Model):    
    _name = 'product.stock'
     
    p_name = fields.Many2many('csvfile.load', string='p_name')
    p_quantity = fields.Many2many('product.qua',string='p_quantity')   
    
    
class Productsqua(models.Model):   
    _name = 'product.qua'
    p_quantity  = fields.Char(string='p_quantity')
    
    
class Buyproducts(models.Model):
    _name = 'products.buy'
    _description = 'products buy detailes'      
    _order  =  'groceries'
    _inherit =['mail.thread', 'mail.activity.mixin']
            
    groceries = fields.Many2many('products.data', string='groceries')      
    user = fields.Many2one('res.users', string='user')
    mail_send = fields.Char(string='mail_send', default=lambda self: self.env.user.login)
    quantity = fields.Char(string='quantity')
    # extdata = fields.Char(string='extdata')
    # extdata2 = fields.Char(string='extdata2')
    
    # @api.model
    # def create(self, values):
        
    #     d = []
    #     for i in self.groceries:
    #         # print(i['product_name'])
    #         # print(i['quantity'])
    #         x = i['product_name']
    #         y = i['quantity']
            
    #         datas  = {
    #             x:y
    #         }
    #         d.append(datas)
            
    #         print(d,'===')    
    #         values['extdata'] = datas
    #         # values['extdata'] = x,y
    #         # values['extdata2'] = y
    #         data =  super(Buyproducts, self).create(values)
    #     # print(d, '-=-=-=')    
    #     return data
            
            
        # print(self.groceries,'-==--=')
    
    # def check_orm(self):
    #     x = self.groceries
    #     user = self.user
    #     xx = user.login
        
    #     p_data = []
    #     for i  in x:
    #         p_data.append(i.product_name)
    #         # p = i.product_name
            
    #     # p = dict(zip( , p_data))  
    #     buyuser products.buy(1,)= self.env.user.email

    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     # s['Subject'] = 'This message was sent with Python'
        
    #     SUBJECT = "This message was sent with Python "   
    #     # TEXT = "Message body"
 
        
    #     s.starttls()
        
    #     s.login("gautamsinh987@gmail.com", "mqznejfvpkkulgho")
    #     message = f"Product Name {p_data}  \nBuy User {buyuser}, \n{SUBJECT}" 
    #     # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #     s.sendmail("gautamsinh987@gmail.com",xx,message)
    #     s.quit()    
    
    
    def check_orm(self):
        templates_id = self.env.ref('kirana__store.products_send_email_template').id
        print(templates_id,'-=-=-=')
        tem = self.env['mail.template'].browse(templates_id)
        tem.send_mail(self.id, force_send=True)
        
        # print(templates,'-===---=---=-=--==-=--=-=-=')
        # for i in self:
        #     x = i.user.login
        #     print(x)
        #     templates.send_mail(i.id)

        # print(p_data)
        
    
    # def send_email(self):
    #     x =self.groceries
    #     search_var  = {"Product Name":self.product_name, "Product Groceries":self.product_quntity, "Product Quntity":self.product_quntity, "Totle":self.totel}
    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     s.starttls()
    #     s.login("gautamsinh987@gmail.com", "enter your email password")
    #     message = f"Product Name {self.product_name} \n Product price {self.product_quntity} \n Product quntity {self.product_quntity}\n Product totel {self.totel}" 
    #     s.sendmail("gautamsinh987@gmail.com", 'makwanagautam199@gmail.com',message)
    #     s.quit()
    #     print(search_var,'-=-=-=-=-')
    
   
class Csvload(models.Model):
    _name = 'csvfile.load'            
    
    name = fields.Char(string='Name')
    price = fields.Char(string='price')
    
    def check_orm(self):
        csv_path = '/Users/yudiz/Desktop/backup/odoo_work/odoo_pro/odoo/g.csv'
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                c = (row.keys())    
                pdata = []
                for i in  c:
                    print(i,'-==--=')
                    print(pdata.append(i), "0--0--00-")
                print(pdata,'---')
                print(pdata)
                for i in pdata:
                    x = row['itemDescription']
                    y = row['price']
                    print(x,y)
                    #  need model dynamic and keys make dynamic 
            # for i in c:   
            #     print(i, '===')
             
    @api.model
    def create(self,values):
        # Specify the path to your CSV file
        print("csv file call")
        
        csv_path = '/Users/yudiz/Desktop/backup/odoo_work/odoo_pro/odoo/g.csv'
        # Read the CSV file and create records in Odoo
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = row['itemDescription']
                y = row['price']
                print(row.keys(),'-===--=-=--=-=-')
                
                values['name']= x
                values['price'] = y

                print(str(values),'-==-')
                datas = super(Csvload, self).create(values)
                print(datas)     
            return datas
        
        
class PurchaseProduct(models.Model):
    _name = 'purchase.data'
    
    name = fields.Char(string='name')
    productqty = fields.One2many('product.quality', 'purchasedata' , string='productqty')
    mail_send = fields.Char(string='your mail', default=lambda self: self.env.user.login)
    user = fields.Many2one('res.users', string='seller mail')
    
    # def check_orm(self):
    #     print(self,'-=-=-==--=')
    #     for i in self.productqty:
    #         print(i['product_id']['name'],'-=-=-=')    
    #         print(i['price'],'-=-=-=')    
    #         print(i['qty'],'-=-=-=')
    
    # @api.constrains('user')     
    # def lencheck(self): 
    #     for  record  in self:
    #         if  record.user == self.env.user.login:
    #             raise  ValidationError('name not allowled')
              
              
    def check_orm(self):
        templates_id = self.env.ref('kirana__store.send_products_email_template').id
        print(templates_id,'-=-=-=')
        tem = self.env['mail.template'].browse(templates_id)
        tem.send_mail(self.id, force_send=True) 
    
    
    def test(self):
        print(self.user.login)
        search_var = self.env['purchase.data'].search([('user','=', self.env.user.login)])  
        print(search_var,'-=-=-=-=')
        
        
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamic_domain', False):
            domain = self._get_dynamic_domain()
            args += domain
        return super(PurchaseProduct, self).search(args, offset=offset, limit=limit, order=order, count=count)

    # Method to get the dynamic domain based on the current user's department
    @api.model
    def _get_dynamic_domain(self):
        # current_user = self.env.user
        # if current_user and current_user.department_id:
        domain = [('mail_send', '=',self.env.user.login )]
        # else:
        #     domain = []
        return domain
    
        
        
        
                  
                  
class ProductQuality(models.Model):
    
    _name = 'product.quality'        
        
    product_id = fields.Many2one('csvfile.load', )   
    quantity  = fields.Char(string='quantity')    
    login_user = fields.Char(string='login_user', default=lambda self: self.env.user.login )
    purchasedata = fields.Many2one('purchase.data', string='purchasedata')    
    
    
    # this is for dynamic domain set 
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamic_domain', False):
            domain = self._get_dynamic_domain()
            args += domain
        return super(ProductQuality, self).search(args, offset=offset, limit=limit, order=order, count=count)

    # Method to get the dynamic domain based on the current user's department
    @api.model
    def _get_dynamic_domain(self):
        # current_user = self.env.user
        # if current_user and current_user.department_id:
        domain = [('login_user', '=',self.env.user.login )]
        # else:
        #     domain = []
        return domain
    
    


