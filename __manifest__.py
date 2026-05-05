{
    'name': 'Riders Backend Theme',
    'version': '18.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Modern backend theme with Riders orange brand identity',
    'description': 'Customizes the Odoo 18 backend interface with Riders brand colors, modern typography, refined spacing, and polished UI components.',
    'author': 'Riders Workshop',
    'website': 'https://www.intres.com',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'riders_backend_theme/static/src/scss/backend_theme.scss',
            'riders_backend_theme/static/src/js/backend_theme.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
