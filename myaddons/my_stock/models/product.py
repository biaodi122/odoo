from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    main_supplier = fields.Many2one('res.partner', string='主要供应商', default='中国')
    country_id = fields.Many2one('res.country', string='国家')
    supplierinfo_id = fields.Many2many('product.supplierinfo')
    china_quantity = fields.Float(string='中国库存数量', compute='_compute_china_quantity')
    usa_quantity = fields.Float(string='美国库存数量',compute='_compute_usa_quantity')

    quant_ids = fields.Many2many('stock.quant', 'product_quant_rel',
                                 'template_id', 'quant_id', string='库存记录')
    product_variant_id = fields.Many2one(store = True)

    # 定义一个计算字段，用来存储quantity字段的总和
    test = fields.Float(string='测试', compute='_compute_total_quantity')

    # # 定义一个计算函数，使用sum聚合函数对quantity字段进行求和
    # @api.depends('quant_ids.quantity')
    # def _compute_total_quantity(self):
    #     # 使用search方法获取所有的stock.quant记录
    #     for a in self:
    #         quants = self.env['stock.quant'].search([])
    #         # 使用sum聚合函数对quantity字段进行求和，并赋值给计算字段
    #         a.test = sum(quants.mapped('quantity'))

    @api.depends('quant_ids.quantity')
    def _compute_total_quantity(self):
        for template in self:
            total_quantity = 2.0
            quants = self.env['stock.quant'].search([
                ('product_id.product_tmpl_id', '=', template.id)
            ])
            for quant in quants:
                total_quantity += quant.quantity
            template.test = total_quantity

    # 计算某个产品的中国库存数量
    # 指定了触发计算属性 _compute_china_quantity的依赖关系，即当产品的库存量发生变化时，该计算属性会被重新计算。
    @api.depends('quant_ids.quantity')
    def _compute_china_quantity(self):
        # 遍历所有的产品模板记录
        for template in self:
            # 筛选条件
            # self.env['stock.quant']获取stock.quant模型访问对象
            china_quants = self.env['stock.quant'].search([
                ('location_id.warehouse_id.country_id.code', '=', 'CN'),
                ('product_id.product_tmpl_id', '=', template.id),
            ])
            # 对筛选出来的进行求和
            # mapped()方法返回一个列表，将库存记录中的quantity属性提取出来，并计算它们的和。sum返回列表所有元素之和
            template.china_quantity = sum(china_quants.mapped('quantity'))

    @api.depends('quant_ids.quantity','quant_ids.warehouse_id.country_id.code')
    def _compute_usa_quantity(self):
        # 遍历所有的产品模板记录
        for template in self:
            # 筛选条件
            # self.env['stock.quant']获取stock.quant模型访问对象
            usa_quants = self.env['stock.quant'].search([
                ('location_id.warehouse_id.country_id.code', '=', 'US'),
                ('product_id.product_tmpl_id', '=', template.id),
            ])
            # 对筛选出来的进行求和
            # mapped()方法返回一个列表，将库存记录中的quantity属性提取出来，并计算它们的和。sum返回列表所有元素之和
            template.usa_quantity = sum(usa_quants.mapped('quantity'))
