# -*- coding: utf-8 -*-
from odoo import http

# class PartnerCapitalSocialChiffresDAffaires(http.Controller):
#     @http.route('/partner_capital_social_chiffres_d_affaires/partner_capital_social_chiffres_d_affaires/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_capital_social_chiffres_d_affaires/partner_capital_social_chiffres_d_affaires/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_capital_social_chiffres_d_affaires.listing', {
#             'root': '/partner_capital_social_chiffres_d_affaires/partner_capital_social_chiffres_d_affaires',
#             'objects': http.request.env['partner_capital_social_chiffres_d_affaires.partner_capital_social_chiffres_d_affaires'].search([]),
#         })

#     @http.route('/partner_capital_social_chiffres_d_affaires/partner_capital_social_chiffres_d_affaires/objects/<model("partner_capital_social_chiffres_d_affaires.partner_capital_social_chiffres_d_affaires"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_capital_social_chiffres_d_affaires.object', {
#             'object': obj
#         })