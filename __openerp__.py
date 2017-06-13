# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Show Sale Order Invoiced Amounts',
    'category': 'Sales',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'depends': ['sale'],
    'description': """
Show Sale Order Invoiced Amounts
================================
* Modifies the Invoiced Ratio calculation so that it also calculates the exact amounts, not just the percentage
""",
    'data': [
        'views/sale_order.xml',
    ],
}
