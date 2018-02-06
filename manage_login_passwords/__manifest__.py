# -*- coding: utf-8 -*-

{
    'name': 'Password Credentials Management',
    'category': 'Extra',
    'summary': 'Module to manage login passwords',
    'version': '1.0',
    'description': """This module helps to manage password & login details compnay. eg. A webiste development company, can store all sites username and passwords in single place. Access & visiblity rule added based on department""",
    'author': 'Navabrind IT Solutions',
    'website': 'https://www.navabrinditsolutions.com',
    'depends': ['base','hr','project'],
    'data': [
        'security/password_security.xml',
        'security/ir.model.access.csv',
    	'login_password_view.xml',
    	'data/sites_data.xml',
    	#'data/sites_type_data.xml',
    	'login_data_template_view.xml',
	],
    'installable': True,
    'auto_install': False,
}

