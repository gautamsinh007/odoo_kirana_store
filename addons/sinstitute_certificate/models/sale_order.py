from odoo import fields , models , api,_
from odoo.exceptions import ValidationError, UserError
# import  datetime 
from datetime import date, datetime




class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    test = fields.Char(string='test field')
    staff_id  = fields.Many2one('res.country', string='country')
    
    