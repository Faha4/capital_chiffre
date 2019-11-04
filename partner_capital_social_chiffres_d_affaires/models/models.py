# -*- coding: utf-8 -*-

from odoo import models, fields, api

class partner_capital_social_chiffres_d_affaires(models.Model):
	_inherit = 'res.partner'
	
	company_id = fields.Many2one('res.company', string ='Company')
	company_currency_id = fields.Many2one('res.currency', string="Devise", default=105)
	capital_share 	= fields.Monetary()
	capital_amount 	= fields.Monetary()

class DataTransferCompanyCapital(models.Model):
	_inherit = 'crm.lead'

	@api.multi
	def _lead_create_contact(self, name, is_company, parent_id=False):


		values = {
			'capital_share'	:  self.contact_capital_share,
			'capital_amount':  self.contact_capital_amount 	
		}

		insert_partner = super(DataTransferCompanyCapital,self)._lead_create_contact(name, is_company, parent_id)
		insert_partner.update(values)

		return insert_partner
