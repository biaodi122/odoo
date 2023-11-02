from  odoo import  api ,fields,models


class Test(models.Model):
    _name = 'test'
    _description = '测试'
    _auto = False


    name = fields.Char(string='姓名')


