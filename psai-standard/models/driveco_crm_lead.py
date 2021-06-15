# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


# class c:\odoo\local-addons\driveco.com\psai-standard(models.Model):
#     _name = 'c:\odoo\local-addons\driveco.com\psai-standard.c:\odoo\local-addons\driveco.com\psai-standard'
#     _description = 'c:\odoo\local-addons\driveco.com\psai-standard.c:\odoo\local-addons\driveco.com\psai-standard'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class DrivecoCrmLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'Ajout divers champs pour valorisation lead selon nombre de prises'

    x_nbre_prise_kw = fields.Integer('Nombre prises KW')
    x_prix_prise_kw = fields.Float('Prix prise KW')
    x_nbre_prise_renforce = fields.Integer('Nombre prises renforcées')
    x_prix_prise_renforce = fields.Float('Prix prise renforcée')
    x_nbre_prise_one = fields.Integer('Nombre prises Borne ONE')
    x_prix_prise_one = fields.Float('Prix prise Borne ONE')
    x_nbre_prise_pro = fields.Integer('Nombre prises Borne PRO')
    x_prix_prise_pro = fields.Float('Prix prise Borne PRO')
    x_nbre_prise_urban = fields.Integer('Nombre prises Borne URBAN')
    x_prix_prise_urban = fields.Float('Prix prise Borne URBAN')
    x_nbre_prise_dc = fields.Integer('Nombre prises Borne DC')
    x_prix_prise_dc = fields.Float('Prix prise Borne DC')
    x_ingenieur_affaire = fields.Many2one("hr.employee","Ingénieur affaire",required=True)
    x_date_attribution = fields.Datetime('Date attribution Ingénieur Affaire')
    x_date_initialisation = fields.Datetime('Date initialisation')
    x_date_envoi_devis = fields.Datetime('Date envoi devis')
    x_date_livraison_prevu = fields.Datetime('Date livraison prévue')
    x_segment_marche = fields.Selection(selection=[('0','Auto'),
                                                   ('1','Retail'),
                                                   ('2','Hotelerie'),
                                                   ('3','Entreprise'),
                                                   ('4','Promoteur'),
                                                   ('5','Immobilier'),
                                                   ('6','Home'),
                                                   ('7','Sante')],
                        string='Segment de marché',default=0)

    @api.onchange('x_nbre_prise_kw')
    def _onchange_x_nbre_prise_kw(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_prix_prise_kw')
    def _onchange_x_prix_prise_kw(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_nbre_prise_renforce')
    def _onchange_x_nbre_prise_renforce(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_prix_prise_renforce')
    def _onchange_x_prix_prise_renforce(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_nbre_prise_one')
    def _onchange_x_nbre_prise_one(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_prix_prise_one')
    def _onchange_x_prix_prise_one(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_nbre_prise_pro')
    def _onchange_x_nbre_prise_pro(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_prix_prise_pro')
    def _onchange_x_prix_prise_pro(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_nbre_prise_urban')
    def _onchange_nbre_prise_urban(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)
    @api.onchange('x_prix_prise_urban')
    def _onchange_x_prix_prise_urban(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_nbre_prise_dc')
    def _onchange_nbre_prise_dc(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

    @api.onchange('x_prix_prise_dc')
    def _onchange_prix_prise_dc(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)

