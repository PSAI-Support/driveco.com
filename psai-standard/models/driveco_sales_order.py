import datetime

from odoo import fields, models, api


class DrivecoSaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Ajout des champs Advenir , compte versement, lien vers commande liée'

    x_advenir_prive = fields.Many2one('driveco.advenirprive','Advenir Privé')
    x_advenir_public = fields.Many2one('driveco.advenirpublic','Advenir Public')
    x_advenir_compte_versement = fields.Selection([('driveco','Driveco'),('client','Client')],'Compte versement',default="driveco")
    x_order_id = fields.Many2one('sale.order',string='commande fils')
    x_marque_order = fields.Many2one( related="partner_id.x_marque", string='Marque', store=True)

    def write(self, values):
        result = super(DrivecoSaleOrder, self).write(values)
        if 'state' in values:
            if self.state == 'sent' and self.opportunity_id:
                self.opportunity_id.write({'x_date_envoi_devis':datetime.datetime.now(),
                                           'x_devis_envoye_id': self.name})
            if self.state == 'sale' and self.opportunity_id:
                self.opportunity_id.write({'x_date_livraison_prevu': self.expected_date})
        return result

    # @api.onchange('state', 'write_date')
    # def _onchange_state(self):
    #     for order in self:
    #         order.write({'note': 'test'})
    #         if order.state == 'sent' and order.opportunity_id:
    #             order.opportunity_id.write({'x_date_envoi_devis':datetime.datetime.now(),})
