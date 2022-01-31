# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2019-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Employee Icard',
    'summary': 'Print Standard ID Card for your employee from system',
    'version': '12.0.0.1.0',
    'category': 'extra',
    'author':'Jupical Technologies Pvt. Ltd.',
    'maintainer': 'Jupical Technologies Pvt. Ltd.',
    'website': 'http://www.jupical.com',
    'depends': ['hr','jt_employee_sequence'],
    'data': [
        'reports/light_icard_report_front.xml',
        'reports/light_icard_report_back.xml',
        'reports/stylish_icard_report_front.xml',
        'reports/stylish_icard_report_back.xml',
    ],
    "price": 15.00,
    "currency": "EUR",
    'license': 'AGPL-3',
    'images': ['static/description/poster_image.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}