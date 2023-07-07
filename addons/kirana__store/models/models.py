# -*- coding: utf-8 -*- thsis si si snew add 

from odoo import models, fields, api


class kirana__store(models.Model):
    _name = 'kirana__store.kirana__store'
    _description = 'kirana__store.kirana__store'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
