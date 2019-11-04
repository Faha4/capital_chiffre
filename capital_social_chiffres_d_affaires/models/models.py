# -*- coding: utf-8 -*-

from odoo import models, fields, api

class capital_social_chiffres_d_affaires(models.Model):
	_inherit = 'crm.lead'
	
	currency_id = fields.Many2one("res.currency", string="Devise", default=105)
	contact_capital_share 		= fields.Monetary()
	contact_capital_amount 		= fields.Monetary()


