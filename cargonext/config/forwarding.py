from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {                
                        "label": _("Shipment"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Shipment"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Groupage"
                                },
								{
								        "type": "doctype",
                                        "name": "Container"
								}
                        ]
                },
				{
                        "label": _("Schedules"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Sailing Schedule"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Flight Schedule"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Rail Schedule"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Road Schedule",
                                },
                        ]
                },
				{
                        "label": _("Forwarding Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "INCO Term"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Network"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Nominations"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Job Type",
                                },
                        ]
                },
                {
                        "label": _("Carriers"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Vessel"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Airline"
                                },
								{
                                        "type": "doctype",
                                        "name": "Vessel Consortium"
                                },
								{
                                        "type": "doctype",
                                        "name": "Land Transport"
                                }
                        ]
                },
                {
                        "label": _("Locations"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "UNLOCO"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Special Economic Zone"
                                },
                                {
                                        "type": "doctype",
                                        "name": "International Zone"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Time Zone"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Trade Lane"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Country"
                                }
                        ]
                },
                {
                        "label": _("Container Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Container Class"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Container Mode"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Container Type"
                                },
                        ]
                },
                {
                        "label": _("Commodity Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Commodity"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Dangerous Good"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Classification"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Unit Conversion"
                                },
                        ]
                },
                {
                        "label": _("Organizations"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Shipper"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Consignee"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Consolidator"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Carrier"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Agent"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Warehouse Provider"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Broker"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Service Provider"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Network"
                                },
								]
                },
                {
                        "label": _("Agreements"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Service Level"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Agency Agreement"
                                },
								]
                },
				]
