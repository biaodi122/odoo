from odoo import api, fields, models


class LibraryRecord(models.Model):
    _name = 'library.record'

    name = fields.Char(string='姓名')
    notes = fields.Text(string='笔记')
    flag = fields.Boolean(string='是否接种', default=True)
    nums = fields.Integer(string='零售价', size=20)
    money = fields.Float(string='总价', compute='_compute_rate')
    now = fields.Date(string='时间')
    time = fields.Datetime(string='具体日期')
    any = fields.Binary(string='上传文件', store=False)
    page = fields.Html('代码')
    gender = fields.Selection([('1', '男性'), ('2', '女性'), ('3', '其他')], default=1)

    @api.depends('nums')
    def _compute_rate(self):
        self.money = self.nums * 20
