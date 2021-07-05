# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmLeadSaleOrder(models.TransientModel):
    _name = 'crm.lead.sale.order'

    def _get_current_products(self):
        lead_id = self.env.context.get('active_id', 0)
        if not lead_id:
            return []
        lead = self.env['crm.lead'].browse(int(lead_id))
        if not lead:
            return []
        ids = []
        for line in lead.order_line_ids:
            n_line = self.env['crm.lead.sale.order.line'].create({
                'wizard_id': self.id,
                'product_template_id': line.product_template_id.id,
                'qty': line.quantity,
                'unit_price': line.price_unit,
            })
            ids.append(n_line.id)
        return ids

    product_line_ids = fields.One2many('crm.lead.sale.order.line', 'wizard_id', default=_get_current_products)

    def create_quotation(self):
        lead_id = self.env.context.get('active_id', 0)
        if not lead_id:
            return True
        lead = self.env['crm.lead'].browse(int(lead_id))
        if not lead:
            return True
        vals = {
            'partner_id': lead.partner_id.id,
            'company_id': self.env.company.id,
            'opportunity_id': lead.id
        }

        order = self.env['sale.order'].create(vals)
        for line in self.product_line_ids:
            self.env['sale.order.line'].create({
                'order_id': order.id,
                'product_id': line.product_template_id.product_variant_id.id,
                'price_unit': line.unit_price,
                'product_uom_qty': line.qty
            })
        return True


class CrmLeadSaleOrderLine(models.TransientModel):
    _name = 'crm.lead.sale.order.line'

    product_template_id = fields.Many2one('product.template')
    qty = fields.Float()
    unit_price = fields.Float()
    wizard_id = fields.Many2one('crm.lead.sale.order')
