# -*- encoding: utf-8 -*-
{
    'name': 'Website contact',
    'summary': 'Website contact : display contact on website',
    'version': '15.0.1.0.0',
    'category': 'Website',
    'author': 'RAVALISON A. Tsiorimampionina',
    'license': 'AGPL-3',
    'depends': ['website'],
    'data': [
        'views/partner_snippets.xml',
        'views/partner_template.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_contact/static/src/scss/style.scss',
        ]
    },
    'installable': True,
    'application': False,
}
