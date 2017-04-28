# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "CargoNext",
			"color": "grey",
			"icon": "fa fa-truck",
			"type": "module",
			"label": _("CargoNext")
		},
                {
                        "module_name": "Forwarding",	
                        "color": "green",
                        "icon": "fa fa-ship",
                        "type": "module",
                        "label": _("Forwarding")
                },
                {
                        "module_name": "Haulage",
                        "color": "blue",
                        "icon": "fa fa-truck",
                        "type": "module", 
                        "label": _("Haulage")
                },
                {
                        "module_name": "Customs",
                        "color": "red",
                        "icon": "fa fa-certificate",
                        "type": "module",
                        "label": _("Customs")
                },
                {
                        "module_name": "Warehousing",
                        "color": "brown",
                        "icon": "fa fa-qrcode",
                        "type": "module",
                        "label": _("Warehousing")
                },
                {
                        "module_name": "Organizations",
                        "color": "orange",
                        "icon": "fa fa-address-card-o",
                        "type": "module",
                        "label": _("Organizations")
                }                                                                                                           
                                                                                                                            
                ] 
