from odoo import fields, models, api


class DrivecoMarque(models.Model):
    _name = 'driveco.marque'
    _description = 'Liste des marques'

    name = fields.Char('Code Marque', required=True)

