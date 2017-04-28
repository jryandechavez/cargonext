from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {                
                        "label": _("Organizations"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Consignor"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Consignee"
                                },
								{
								        "type": "doctype",
                                        "name": "Supplier"
								},								
								{
								        "type": "doctype",
                                        "name": "Customer"
								},
                        ]
                },
		{
                        "label": _("Carriers"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Airline"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Shipping Line"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Land Transport Company"
                                },							
								{
								        "type": "doctype",
                                        "name": "Consolidator"
								},
								{
								        "type": "doctype",
                                        "name": "Forwarder Agent"
								},
                        ]
                },
				{
                        "label": _("Service Providers"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Container Freight Station"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Container Terminal Operator"
                                },
								{
                                        "type": "doctype",
                                        "name": "Container Yard"
                                },
								{
								        "type": "doctype",
                                        "name": "Warehouse Company"
								},
								{
								        "type": "doctype",
                                        "name": "Fumigation Contractor"
								},
								{
								        "type": "doctype",
                                        "name": "Road Depot"
								},
								{
								        "type": "doctype",
                                        "name": "Distribution Center"
								}
                        ]
                },
                {
                        "label": _("Service Level and Agreements"),
                        "items": [
								{
                                        "type": "doctype",
                                        "name": "Service Level"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Profit Share Agreement"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Agent PSA"
                                },
								{
                                        "type": "doctype",
                                        "name": "Agency Agreement Type"
                                }
                        ]
                },
                {
                        "label": _("Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Exporter Category"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Importer Category"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Agent Network"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Forwarder Category"
                                }
                        ]
                },
                
				]
