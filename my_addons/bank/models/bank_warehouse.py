# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BankWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    storehouse_country_id = fields.Many2one('res.country',
                                            string='仓库所在地',
                                            compute='sync_partner_id',
                                            store=True)

    @api.depends('partner_id', 'partner_id.country_id')
    def sync_partner_id(self):
        for warehouse in self:
            country = warehouse.partner_id.country_id
            if country:
                warehouse.storehouse_country_id = country.id
            else:
                warehouse.storehouse_country_id = self.env.ref('base.us').id


