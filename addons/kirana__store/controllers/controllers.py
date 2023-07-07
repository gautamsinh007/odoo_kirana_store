# -*- coding: utf-8 -*-
from odoo import http


class KiranaStore(http.Controller):
    @http.route('/kirana__store/kirana__store', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/kirana__store/kirana__store/objects', auth='public')
    def list(self, **kw):
        return http.request.render('kirana__store.listing', {
            'root': '/kirana__store/kirana__store',
            'objects': http.request.env['kirana__store.kirana__store'].search([]),
        })

    @http.route('/kirana__store/kirana__store/objects/<model("kirana__store.kirana__store"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('kirana__store.object', {
            'object': obj
        })
