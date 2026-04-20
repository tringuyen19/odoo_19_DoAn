# from odoo import http


# class DuplicateGuard(http.Controller):
#     @http.route('/duplicate_guard/duplicate_guard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/duplicate_guard/duplicate_guard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('duplicate_guard.listing', {
#             'root': '/duplicate_guard/duplicate_guard',
#             'objects': http.request.env['duplicate_guard.duplicate_guard'].search([]),
#         })

#     @http.route('/duplicate_guard/duplicate_guard/objects/<model("duplicate_guard.duplicate_guard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duplicate_guard.object', {
#             'object': obj
#         })

