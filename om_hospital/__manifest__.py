{
    'name': 'Hospital Management',
    'version': '13.0.1.0',
    'summary': 'Module for managing the Hospital',
    'description': 'Hospital Management System',
    'category': 'test',
    'author': 'Unisoft',
    'website': 'unisoft.com',
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}