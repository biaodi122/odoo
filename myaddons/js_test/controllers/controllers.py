# -*- coding: utf-8 -*-
# from odoo import http


# class JsTest(http.Controller):
#     @http.route('/js_test/js_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/js_test/js_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('js_test.listing', {
#             'root': '/js_test/js_test',
#             'objects': http.request.env['js_test.js_test'].search([]),
#         })

#     @http.route('/js_test/js_test/objects/<model("js_test.js_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('js_test.object', {
#             'object': obj
#         })
