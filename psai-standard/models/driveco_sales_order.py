from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'driveco.sale.order'
    _description = 'Ajout des champs Advenir , compte versement, lien vers commande liée'
    _inherit = 'sale.order'

    x_advenir_prive = fields.Char()
    x_advenir_public = fields.Char()
    x_advenir_compte_versement = fields.Selection([('driveco','Driveco'),('client','Client')],'Compte versement',default="driveco")
    x_order_id = fields.Many2one('sale.order',string='commande fils')
    x_order_ids = fields.One2many('sale.order','x_order_id', 'Commandes père')

