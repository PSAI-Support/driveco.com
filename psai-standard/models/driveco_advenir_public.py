from odoo import fields, models, api


class DrivecoAdvenirPublic(models.Model):
    _name = 'driveco.advenirpublic'
    _description = 'Driveco ADVENIR PUBLIC'

    name = fields.Char('Code ADVENIR Public', required=True)
