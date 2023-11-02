from odoo import api, fields, models, tools


class ProductReport(models.Model):
    _name = 'product.report'
    _description = '产品报告'
    _auto = False
    id = fields.Integer(string='ID', readonly=True)
    product_id = fields.Many2one('product.template',string='产品')
    warehouse1 = fields.Float(string='仓库1', readonly=True)
    warehouse2 = fields.Float(string='仓库2', readonly=True)
    warehouse3 = fields.Float(string='仓库3', readonly=True)
    warehouse4= fields.Float(string='仓库4', readonly=True)
    all_quantity = fields.Float(string='合计',readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            create or replace  view %s as(
            
            select 
                 row_number() over () as id,
                 sq.product_id as product_id,
                    SUM(CASE WHEN sw.id = 1 THEN sq.quantity ELSE 0 END)  as warehouse1,                               
                    SUM(CASE WHEN sw.id = 16 THEN sq.quantity ELSE 0 END) as warehouse2,                              
                    SUM(CASE WHEN sw.id = 3 THEN sq.quantity ELSE 0 END)  as warehouse3 ,
                    SUM(CASE WHEN sw.id = 20 THEN sq.quantity ELSE 0 END) as  warehouse4,
                    SUM(CASE WHEN sw.id in (1,16,2,20) THEN sq.quantity ELSE 0 END ) all_quantity
                                      
            from 
                 stock_quant sq
                    join stock_location sl on sq.location_id = sl.id
                    join stock_warehouse sw on sw.lot_stock_id=sl.id
                    group by sq.product_id
            )
        ''' % self._table)
