# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

import openerp.addons.decimal_precision as dp

class ManufacturerPrice(models.Model):

	_inherit = 'product.template'

	#_name = 'test_price'

	# 'standard_price': fields.property(type = 'float', digits_compute=dp.get_precision('Product Price'), 
 #                                          help="Cost price of the product template used for standard stock valuation in accounting and used as a base price on purchase orders. "
 #                                               "Expressed in the default unit of measure of the product.",
 #                                          groups="base.group_user", string="Cost Price"),

 	# _columns = {

 	# 	'standard_price' : fields.Float(help="Cost price of the product template used for standard stock valuation \
 	# 							in accounting and used as a base price on purchase orders.Expressed in the default unit of measure of the product.",
 	# 							groups="base.group_user", string="Cost Price",default=0, digits=dp.get_precision('Product Price')),


 	# }

 	standard_price = fields.Float(help="Cost price of the product template used for standard stock valuation \
 								in accounting and used as a base price on purchase orders.Expressed in the default unit of measure of the product.",
 								groups="base.group_user", string="Cost Price",default=0, digits=dp.get_precision('Product Price')),
 	
                                               