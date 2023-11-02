from odoo import api, models, fields


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    country_id = fields.Many2one('res.country', string='国家', compute='_compute_country_id',store=True)

    @api.depends('partner_id','partner_id.country_id')
    def _compute_country_id(self):
        # 根据地址字段自动识别和设置国家字段
        # ：对于每个仓库记录实例进行循环
        for warehouse in self:
            # 判断仓库的合作伙伴是否有关联的国家
            if warehouse.partner_id.country_id:
                # 如果仓库的合作伙伴有关联的国家，则将仓库的国家字段设置为关联国家的ID。
                warehouse.country_id = warehouse.partner_id.country_id.id
            else:
                #将仓库的国家字段设置为默认国家的ID（这里使用了base.vn作为默认国家的标识符，表示越南）
                warehouse.country_id = self.env.ref('base.vn').id
