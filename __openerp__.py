# -*- coding: utf-8 -*-
{
    'name': "Sistema de Ventas",

    'summary': """
        It is used to manage the transactions""",

    'description': """
        You can manage transactions as pagos, compras, clientes etc.
    """,

    'author': "@wzuniga",
    'website': "http://www.facebook.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/main.xml',
        'views/cliente.xml',
        'views/producto.xml',
        'views/temporada.xml',
        'views/precio.xml',
        'views/venta.xml',
        'views/pago.xml',
        'views/relacion.xml',
        'reports/ventas_report.xml',
        'reports/temporadas_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}