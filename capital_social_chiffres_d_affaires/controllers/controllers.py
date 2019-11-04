# -*- coding: utf-8 -*-
from odoo import http

# class CapitalSocialChiffresDAffaires(http.Controller):
#     @http.route('/capital_social_chiffres_d_affaires/capital_social_chiffres_d_affaires/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capital_social_chiffres_d_affaires/capital_social_chiffres_d_affaires/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('capital_social_chiffres_d_affaires.listing', {
#             'root': '/capital_social_chiffres_d_affaires/capital_social_chiffres_d_affaires',
#             'objects': http.request.env['capital_social_chiffres_d_affaires.capital_social_chiffres_d_affaires'].search([]),
#         })

#     @http.route('/capital_social_chiffres_d_affaires/capital_social_chiffres_d_affaires/objects/<model("capital_social_chiffres_d_affaires.capital_social_chiffres_d_affaires"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capital_social_chiffres_d_affaires.object', {
#             'object': obj
#         })