from odoo import fields, models, api


class DrivecoAdvenirPrive(models.Model):
    _name = 'driveco.advenirprive'
    _description = 'Driveco ADVENIR PRIVE'

    name = fields.Char('Code ADVENIR PRIVE',required=True)
