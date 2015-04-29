# -*- coding: utf-8 -*-

{
    'name': "Mailing Server",
    'version': '1.1',
    'category': 'Mail',
    'image': 'logo.png',
    'summary': 'Mass mailing and personalized mail server',
    'description': """Mailing server""",
    'author': 'Igor Sjeverac',
    'license': 'AGPL-3',
    'website': "www.netjunky.net",
    "depends" : ['mail','mass_mailing'],
    'data': [
        'mailing_server_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
