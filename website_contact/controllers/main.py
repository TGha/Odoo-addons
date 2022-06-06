# -*- encoding: utf-8 -*-

from odoo import http
from odoo.http import request


class Partner(http.Controller):

    def _prepare_contact_values(self, search, page, order):
        step = 10
        options = {
            'displayDescription': False,
            'displayDetail': False,
            'displayExtraDetail': False,
            'displayExtraLink': False,
            'displayImage': False
        }
        offset = (page - 1) * step
        pages_count, details, fuzzy_search_term = request.website._search_with_fuzzy(
            "contact", search, limit=page * step, order=order, options=options)
        pager = request.website.pager(
            url='/website/contact',
            total=pages_count,
            page=page,
            step=step,
        )
        return {
            "pager": pager,
            "contacts": details[0]['results'][offset:offset + step]
        }

    @http.route([
        '/website/contact',
        '/website/contact/page/<int:page>'
    ], type='http', auth='user', website=True, multilang=True)
    def index_contact(self, page=1, search='', order='name asc', **kwargs):
        values = self._prepare_contact_values(search, page, order)
        return request.render('website_contact.index', {
            'contacts': values['contacts'],
            'pager': values['pager'],
            'search': search
        })
