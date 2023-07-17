# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api
import smtplib
import csv

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
    _description = 'products detailes '
    
    product_name  = fields.Char()
    product_price = fields.Integer()
    product_quntity = fields.Integer()
    abc = fields.Integer()
    totel = fields.Integer(compute="_value_pc", store=True)
    groceries = fields.Many2many('csvfile.load', string='groceries')
    
    
    @api.depends('product_price','product_quntity')
    def _value_pc(self):
        for rec in self:
            ctc = 0
            if rec.product_price:
                ctc += rec.product_price 
            if rec.product_quntity:
                ctc *= rec.product_quntity 
                    
            rec.totel = ctc
    
    def send_email(self):
        
        search_var  = {"Product Name":self.product_name, "Product Price":self.product_price, "Product Quntity":self.product_quntity, "Totle":self.totel}
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("gautamsinh987@gmail.com", "mqznejfvpkkulgho")
        # product_name = search_var["Product Name"]
        # product_price = search_var['Product Price']
        # product_qu = search_var["Product Quntity"]
        
        # x = self.id
        # search_var = self.env['products.data'].browse(x)
        # for i in search_var:
        #     print(i.product_name)
        
        message = f"Product Name {self.product_name} \n Product price {self.product_price} \n Product quntity {self.product_quntity}\n Product totel {self.totel}" 
        s.sendmail("gautamsinh987@gmail.com", 'makwanagautam199@gmail.com',message)
        s.quit()
        print(search_var)
            
            
            
            
class Csvload(models.Model):
    _name = 'csvfile.load'            
    
    name = fields.Char(string='Name')
    price = fields.Char(string='price')
    
    
    def check_orm(self):
        csv_path = '/Users/yudiz/Desktop/backup/odoo_work/odoo_pro/odoo/g.csv'
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = row['itemDescription']
                y = row['price']
                print(x,y)
                
    @api.model
    def create(self,values):
        # Specify the path to your CSV file
        print("csv fiel call")
        
        csv_path = '/Users/yudiz/Desktop/backup/odoo_work/odoo_pro/odoo/g.csv'
        # Read the CSV file and create records in Odoo
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = row['itemDescription']
                y = row['price']
                print(x)
                # val = [
                #     {
                values['name']= x
                values['price'] = y
                #     }
                # ]

                print(values,'-==-')
                datas = super(Csvload, self).create(values)
                print(datas)     
            return datas