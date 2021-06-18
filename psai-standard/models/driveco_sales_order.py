from odoo import fields, models, api


class ModelName(models.Model):
    _description = 'Ajout des champs Advenir , compte versement, lien vers commande liée'
    _inherit = 'sale.order'

    x_advenir_prive = fields.Many2one('driveco.advenirprive','Advenir Privé')
    x_advenir_public = fields.Many2one('driveco.advenirpublic','Advenir Public')
    x_advenir_compte_versement = fields.Selection([('driveco','Driveco'),('client','Client')],'Compte versement',default="driveco")
    x_order_id = fields.Many2one('sale.order',string='commande fils')


