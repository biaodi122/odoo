from odoo import  api,fields,models


class Test1(models.Model):
    _name = 'test1'
    _description = '测试'


    name=fields.Char(string='nihao')