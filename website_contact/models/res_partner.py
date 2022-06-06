# -*- encoding: utf-8 -*-

from odoo import api, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = [
        'res.partner',
        'website.searchable.mixin',
    ]

    @api.model
    def _search_get_detail(self, website, order, options):
        with_image = options['displayImage']
        with_description = options['displayDescription']
        fetch_fields = ['id', 'name', 'website_url']
        search_fields = ['name']
        mapping = {
            'name': {'name': 'name', 'type': 'text', 'match': True},
            'website_url': {'name': 'website_url', 'type': 'text'},
        }
        if with_image:
            mapping['image_url'] = {'name': 'image_url', 'type': 'html'}
        if with_description:
            fetch_fields.append('function')
            search_fields.append('function')
            mapping['description'] = {'name': 'function', 'type': 'text', 'match': True}
        return {
            'model': 'res.partner',
            'search_fields': search_fields,
            'base_domain': [],
            'fetch_fields': fetch_fields,
            'mapping': mapping,
            'icon': 'fa-user'
        }

    def _search_render_results(self, fetch_fields, mapping, icon, limit):
        with_image = 'image_url' in mapping
        results_data = super()._search_render_results(fetch_fields, mapping, icon, limit)
        for partner, data in zip(self, results_data):
            data['website_url'] = partner.website_url
            if with_image:
                data['image_url'] = '/web/image/res.partner/%s/avatar_512' % data['id']
        return results_data
