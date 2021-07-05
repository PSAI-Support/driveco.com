# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    order_line_ids = fields.One2many('crm.lead.order.line', 'crm_lead_id')

    @api.onchange('order_line_ids')
    def _onchange_order_line_ids(self):
        for rec in self:
            price_total = 0
            if rec.order_line_ids:
                for line in rec.order_line_ids:
                    price_total += line.price_total
            # rec.expected_revenue = price_total

    def print_document(self):
        for rec in self:
            rec.message_post(body='Did print document', notify_by_email=False)
        action = self.env.ref('crm_lead_add_products.action_report_crm_lead').report_action(self)
        return action


class CrmOrderLines(models.Model):
    _name = 'crm.lead.order.line'

    crm_lead_id = fields.Many2one('crm.lead')
    product_template_id = fields.Many2one('product.template')
    quantity = fields.Float(digits=(10, 2), default=1)
    # price = fields.Float(related='product_template_id.list_price')
    price_unit = fields.Float()
    price_total = fields.Float(compute='_get_price_total', store=True)

    @api.onchange('quantity')
    def _onchange_quantity(self):
        for rec in self:
            if rec.quantity == 0:
                raise UserError('Quantity cannot be 0')


    @api.onchange('product_template_id')
    def _onchange_product_template_id(self):
        for rec in self:
            if rec.product_template_id:
                rec.price_unit = rec.product_template_id.list_price

    @api.depends('price_unit', 'quantity')
    def _get_price_total(self):
        #self.ensure_one() If we want only 1 Record explicitly 
        for rec in self:
            rec.price_total = 0
            if rec.price_unit and rec.quantity:
                rec.price_total = rec.price_unit * rec.quantity
