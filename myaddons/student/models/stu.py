from odoo import api , models , fields


class stu(models.Model):
    _name = 'student.stu'
    _description = 'student.stu'

    name = fields.Char(string='姓名')
    age = fields.Integer(string = '年龄')
