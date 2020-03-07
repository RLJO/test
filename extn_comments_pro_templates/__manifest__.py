# -*- coding: utf-8 -*-
{
    'name': "Professional Report Templates + Sale Comments",
    'support': "support@optima.co.ke",
    'license': 'AGPL-3',
    'summary': """
        Use this plugin to add sales and invoice comments before and after the product lines""",
    'description': """
Insert Sales Order & Invoice comments to Professional Reports Templates' Documents
==================================================================================
* If you have already purchased: https://apps.odoo.com/apps/modules/12.0/professional_templates
  then you can use  this plugin to add sales and invoice comments before and after the product lines

* This module also depends on: https://www.odoo.com/apps/modules/12.0/sale_comment_template
""",
    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'images': ['static/description/main.png'],
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_comment_template'],

    # always loaded
    'data': [
        'views/report_saleorder.xml',
        'views/report_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
