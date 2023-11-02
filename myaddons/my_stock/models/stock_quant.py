from odoo import api, fields, models


class StockQuantInherit(models.Model):
    _inherit = 'stock.quant'

    country_id = fields.Many2one('res.country', string='国家', related='location_id.warehouse_id.country_id')
    warehouse_id = fields.Many2one(store=True)
    product_categ_id = fields.Many2one(store=True)

