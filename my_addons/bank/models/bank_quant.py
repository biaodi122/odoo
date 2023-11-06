# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BankQuant(models.Model):
    _inherit = 'stock.quant'

    storehouse_country_id = fields.Many2one('res.country',
                                            string='国家',
                                            related='location_id.warehouse_id.storehouse_country_id')

    warehouse_id = fields.Many2one(store=True)
    product_categ_id = fields.Many2one(store=True)


