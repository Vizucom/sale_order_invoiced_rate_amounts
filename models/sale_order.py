# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp


class SaleOrder(osv.Model):

    _inherit = 'sale.order'

    def _get_invoiced_amounts(self, cursor, user, ids, name, arg, context=None):
        ''' Modify the core method so that exact amounts are also calculated '''
        print "calculus"
        res = {}
        for sale in self.browse(cursor, user, ids, context=context):
            # Loop through SO's open/paid invoices and get their total sum
            invoiced_total = 0.00
            for invoice in sale.invoice_ids:
                if invoice.state not in ('draft', 'cancel'):
                    invoiced_total += invoice.amount_untaxed

            if invoiced_total == 0.00:
                # If nothing's been invoiced yet
                res[sale.id] = {
                    'invoiced_rate': 0.00,
                    'invoiced_amount': invoiced_total,
                    'to_be_invoiced_amount': sale.amount_untaxed,
                }
            else:
                res[sale.id] = {
                    'invoiced_rate': min(100.0, invoiced_total * 100.0 / (sale.amount_untaxed or 1.00)),
                    'invoiced_amount': invoiced_total,
                    'to_be_invoiced_amount': sale.amount_untaxed - invoiced_total,
                }

        return res

    _columns = {
        'invoiced_rate': fields.function(_get_invoiced_amounts, string='Invoiced Ratio', type='float', digits_compute=dp.get_precision('Account'), multi='invoice_amounts'),
        'invoiced_amount': fields.function(_get_invoiced_amounts, string='Invoiced Amount (untaxed)', type='float', digits_compute=dp.get_precision('Account'), multi='invoice_amounts'),
        'to_be_invoiced_amount': fields.function(_get_invoiced_amounts, string='To Be Invoiced (untaxed)', type='float', digits_compute=dp.get_precision('Account'), multi='invoice_amounts'),
    }
