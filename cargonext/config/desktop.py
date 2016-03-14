# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "CargoNext",
			"color": "grey",
			"icon": "icon-truck",
			"type": "module",
			"label": _("CargoNext")
		},
                {
                        "module_name": "Forwarding",	
                        "color": "green",
                        "icon": "icon-suitcase",
                        "type": "module",
                        "label": _("Forwarding")
                },
                {
                        "module_name": "Haulage",
                        "color": "blue",
                        "icon": "icon-truck",
                        "type": "module", 
                        "label": _("Haulage")
                },
                {
                        "module_name": "Customs",
                        "color": "red",
                        "icon": "icon-file-text",
                        "type": "module",
                        "label": _("Customs")
                },
                {
                        "module_name": "Warehousing",
                        "color": "brown",
                        "icon": "icon-qrcode",
                        "type": "module",
                        "label": _("Warehousing")
                }                                                                                                           
                                                                                                                            
                ] 
