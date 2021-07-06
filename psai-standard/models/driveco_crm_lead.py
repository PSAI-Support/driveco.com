# -*- coding: utf-8 -*-
import datetime

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


    @api.model
    def default_get(self, fields):
        ret = super(DrivecoCrmLead, self).default_get(fields)
        ret['x_prix_prise_kw'] = 1000
        ret['x_prix_prise_renforce'] = 200
        ret['x_prix_prise_one'] = 5000
        ret['x_prix_prise_pro'] = 10000
        ret['x_prix_prise_urban'] = 14000
        ret['x_prix_prise_dc'] = 25000
        return ret

    x_nbre_prise_kw = fields.Integer('Nombre prises KW',tracking=True)
    x_prix_prise_kw = fields.Float('Prix prise KW',tracking=True)
    x_nbre_prise_renforce = fields.Integer('Nombre prises renforcées',tracking=True)
    x_prix_prise_renforce = fields.Float('Prix prise renforcée',tracking=True)
    x_nbre_prise_one = fields.Integer('Nombre prises Borne ONE',tracking=True)
    x_prix_prise_one = fields.Float('Prix prise Borne ONE',tracking=True)
    x_nbre_prise_pro = fields.Integer('Nombre prises Borne PRO',tracking=True)
    x_prix_prise_pro = fields.Float('Prix prise Borne PRO',tracking=True)
    x_nbre_prise_urban = fields.Integer('Nombre prises Borne URBAN',tracking=True)
    x_prix_prise_urban = fields.Float('Prix prise Borne URBAN',tracking=True)
    x_nbre_prise_dc = fields.Integer('Nombre prises Borne DC',tracking=True)
    x_prix_prise_dc = fields.Float('Prix prise Borne DC',tracking=True)
    x_ingenieur_affaire = fields.Many2one("res.users","Ingénieur affaire",tracking=True)
    x_date_attribution = fields.Datetime('Date attribution Ingénieur Affaire',tracking=True)
    x_date_initialisation = fields.Datetime('Date initialisation',tracking=True)
    x_date_envoi_devis = fields.Datetime('Date envoi devis',tracking=True)
    x_date_livraison_prevu = fields.Datetime('Date livraison prévue',tracking=True)
    x_segment_marche = fields.Selection(selection=[('0','Auto'),
                                                   ('1','Retail'),
                                                   ('2','Hotelerie'),
                                                   ('3','Entreprise'),
                                                   ('4','Promoteur'),
                                                   ('5','Immobilier'),
                                                   ('6','Home'),
                                                   ('7','Sante')],
                        string='Segment de marché',default='0',tracking=True)
    x_devis_envoye_id = fields.Char('Devis envoyé')
    x_marque_opportunity =  fields.Many2one( related="partner_id.x_marque", string='Marque', store=True)

    @api.onchange('x_ingenieur_affaire')
    def _onchange_x_ingenieur_affaire(self):
        if self.x_ingenieur_affaire:
            self.x_date_attribution = datetime.datetime.today()

    @api.onchange('x_nbre_prise_kw')
    def _onchange_x_nbre_prise_kw(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_prix_prise_kw')
    def _onchange_x_prix_prise_kw(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_nbre_prise_renforce')
    def _onchange_x_nbre_prise_renforce(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_prix_prise_renforce')
    def _onchange_x_prix_prise_renforce(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_nbre_prise_one')
    def _onchange_x_nbre_prise_one(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_prix_prise_one')
    def _onchange_x_prix_prise_one(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_nbre_prise_pro')
    def _onchange_x_nbre_prise_pro(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_prix_prise_pro')
    def _onchange_x_prix_prise_pro(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_nbre_prise_urban')
    def _onchange_nbre_prise_urban(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_prix_prise_urban')
    def _onchange_x_prix_prise_urban(self):
        self.update_expected_revenue_onchange()

    @api.onchange('x_nbre_prise_dc')
    def _onchange_nbre_prise_dc(self):
        self.update_expected_revenue_onchange()


    @api.onchange('x_prix_prise_dc')
    def _onchange_prix_prise_dc(self):
        self.update_expected_revenue_onchange()

    def update_expected_revenue_onchange(self):
        for rec in self:
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_kw * rec.x_prix_prise_kw)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_renforce * rec.x_prix_prise_renforce)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_one * rec.x_prix_prise_one)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_pro * rec.x_prix_prise_pro)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_urban * rec.x_prix_prise_urban)
            rec.expected_revenue = rec.expected_revenue + (rec.x_nbre_prise_dc * rec.x_prix_prise_dc)