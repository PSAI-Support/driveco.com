# © 2014-2016 Camptocamp SA
# @author: Nicolas Bessi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """Add third field in address"""
    _inherit = "res.partner"

    street3 = fields.Char('BP')

    @api.model
    def _address_fields(self):
        fields = super(ResPartner, self)._address_fields()
        fields.append('street3')
        return fields

    def _display_address(self, without_company=False):
        """Remove empty lines which can happen when street3 field is empty."""
        res = super(ResPartner, self)._display_address(
            without_company=without_company)
        while '\n\n' in res:
            res = res.replace('\n\n', '\n')
        return res
