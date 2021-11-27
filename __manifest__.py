{
    'name': 'Open Academy',
    'version': '1.0.0',
    'category': 'Management',
    'sequence': 1,
    'summary': 'Open Academy for Odoo v13',
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author': 'Md. Haisbul Hasan Shovo',
    'company': 'Md. Haisbul Hasan Shovo',
    'maintainer': 'Md. Haisbul Hasan Shovo',
    'website': 'https://www.linkedin.com/in/iam-hasibul/',
    'depends': ['base', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_views.xml',
        'views/res_partner_views.xml',
        'views/openacademy_session_report.xml',
        'wizard/wizard_views.xml',
        'views/dashboard.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
