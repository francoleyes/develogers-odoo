# -*- coding: utf-8 -*-
{
    'name': "Develogers - Reto",

    'summary': 'Módulo de reto para Develogers',

    'author': "Franco Leyes",
    'website': "https://www.linkedin.com/in/francoleyes/",
    'category': 'Uncategorized',
    'version': '1.0',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'data/ir.module.category.csv',
        'security/res.groups.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/teacher_views.xml',
        'views/menu.xml',
    ],
}





