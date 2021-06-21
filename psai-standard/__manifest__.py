# -*- coding: utf-8 -*-
{
    'name': "DriveEco",

    'summary': """
        Développement spécifique DRIVECO sur les opportunités, Devis""",

    'description': """
        Développement spécifique DRIVECO
    """,

    'author': "PSAI",
    'website': "http://www.psai.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Driveco',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sale','hr','sale_crm','partner_company_group'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/driveco_opportunity_views.xml',
        'views/driveco_sale_view_order_form.xml',
        'views/driveco_marque_view.xml',
        'views/driveco_advenir_prive_view.xml',
        'views/driveco_advenir_public_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
