from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def generate_xml_attachment(self):
        res = super().generate_xml_attachment()
        if self._context.get('l10n_mx_edi_invoice_type') == 'out':
            self.l10n_mx_edi_pac_status = 'signed'
        return res

    @api.multi
    def _l10n_mx_edi_retry(self):
        """avoid generate cfdi when the cfdi was attached"""
        to_retry_invoices = self.filtered(
            lambda inv: inv.l10n_mx_edi_pac_status != 'signed')
        return super(AccountInvoice, to_retry_invoices)._l10n_mx_edi_retry()

    @api.multi
    def invoice_validate(self):
        attach_invoices = self.filtered(
            lambda inv:
            inv.state == 'draft' and inv.l10n_mx_edi_pac_status == 'signed')
        attachs = []
        for inv in attach_invoices:
            attachs.append((inv, inv.l10n_mx_edi_retrieve_last_attachment()))
        res = super().invoice_validate()
        for inv, att in attachs:
            att.name = inv.l10n_mx_edi_cfdi_name
        return res
