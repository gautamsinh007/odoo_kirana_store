# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api


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

    @api.depends('product_price','product_quntity')
    def _value_pc(self):
        for rec in self:
            ctc = 0
            if rec.product_price:
                ctc += rec.product_price 
            if rec.product_quntity:
                ctc *= rec.product_quntity 
                    
            rec.totel = ctc
  