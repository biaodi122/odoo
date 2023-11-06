# -*- coding: utf-8 -*-

from odoo import models, fields, tools


class BankReport(models.Model):
    _name = 'bank.report'
    _description = '仓库产品数量'
    _auto = False

    product_id = fields.Many2one('product.template', string='产品名称')
    count = fields.Float("总数")
    warehouse1 = fields.Float("仓库1")
    warehouse2 = fields.Float("仓库2")
    warehouse3 = fields.Float("仓库3")
    warehouse4 = fields.Float("仓库4")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
        CREATE OR REPLACE VIEW %s AS (
        SELECT
            row_number() over () as id,
            sq.product_id AS product_id,
            sum(CASE WHEN sw.id = 1 THEN sq.quantity ELSE 0 END )AS warehouse1,
            sum(CASE WHEN sw.id = 2 THEN sq.quantity ELSE 0 END )AS warehouse2,
            sum(CASE WHEN sw.id = 3 THEN sq.quantity ELSE 0 END )AS warehouse3,
            sum(CASE WHEN sw.id = 4 THEN sq.quantity ELSE 0 END )AS warehouse4,
            sum(CASE WHEN sw.id IN (1,2,3,4)THEN sq.quantity ELSE 0 END) AS count
        FROM
            stock_quant AS sq
            JOIN stock_location AS sl ON sl.id = sq.location_id
            JOIN stock_warehouse AS sw ON sw.lot_stock_id = sl.id
            GROUP BY
                sq.product_id
        )''' % (self._table,)
                            )
