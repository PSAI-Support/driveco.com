# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Contact(models.Model):
    _inherit = "res.partner"

    company_group_id = fields.Many2one(
        "res.partner", "Company group", domain=[("is_company", "=", True)]
    )

    def _commercial_fields(self):
        return super()._commercial_fields() + ["company_group_id"]

    @api.onchange('company_group_id')
    def onchange_company_group_id(self):
        for partner in self:
            if partner.company_group_id:
                group = partner.company_group_id
                if group.property_product_pricelist:
                    partner.property_product_pricelist = group.property_product_pricelist
                if group.property_payment_term_id:
                    partner.property_payment_term_id = group.property_payment_term_id
