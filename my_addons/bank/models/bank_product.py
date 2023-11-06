# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BankProduct(models.Model):
    _inherit = 'product.template'

    major_supplier_ids = fields.Char(string='主要供应商', default='your company')

    supplierinfo_id = fields.Many2many('product.supplierinfo')

    china_inventory = fields.Float(string='中国库存数量', compute="_compute_china_inventory")
    america_inventory = fields.Float(string='美国库存数量', compute='_compute_america_quantity')
    test1 = fields.Many2many('stock.quant', 'product_quant_rel',
                             'template_id', 'quant_id')
    test2 = fields.Many2one('stock.quant')

    @api.depends('test1.quantity')
    def _compute_china_inventory(self):
        for prod in self:
            stockquant = self.env['stock.quant'].search([
                ('location_id.warehouse_id.storehouse_country_id.code', '=', 'CN'),
                ('product_id.product_tmpl_id', '=', prod.id),
            ])
            prod.china_inventory = sum(stockquant.mapped('quantity'))

    @api.depends('test2.quantity', 'test2.location_id.warehouse_id.storehouse_country_id.code')
    def _compute_america_quantity(self):
        stockquant = self.env['stock.quant']
        for prod in self:
            defaultwarehouseid = self.env['stock.warehouse'].search([('storehouse_country_id.code', '=', 'US')])._ids
            defaultwarehouseid = list(defaultwarehouseid)
            num = 0.0
            quantres = stockquant.search([('product_id.product_tmpl_id', '=', prod.id),
                                          ('warehouse_id', 'in', defaultwarehouseid)])
            for line in quantres:
                num = num + line.quantity
            prod.america_inventory = num
