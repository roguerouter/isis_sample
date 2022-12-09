from __future__ import absolute_import, division, print_function

"""
Copyright (c) 2022 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Matt Leuschner <mleuschn@cisco.com>"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

#Import Modules
from genie import testbed
import csv

#Load testbed file, change isis.yaml to the name of your testbed
testbed = testbed.load('isis_testbed.yaml')

#Create CSV file, generate header, and write header to csv file.
csv_filename = "isis_routing_details.csv"
csv_header = ['Management IP','InstanceID','AreaID','SystemID','VRF','ISIS Interface','ISIS IPv4','ISIS Subnet']

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csv_header)

#Loop through hosts in the testbed file
for host in testbed.devices:
    device = testbed.devices[host]
    device.connect()

    #Parse show commands to capture necessary details for report
    show_isis = device.parse('show isis vrf all')
    show_isis_interface = device.parse('show isis interface vrf all')
    show_mgmt_interface = device.parse('show interface mgmt 0')

    #Get Management address
    if str(testbed.devices[host].os) == 'nxos':
        for address in show_mgmt_interface['mgmt0']['ipv4']:
            mgmt_ip = str(show_mgmt_interface['mgmt0']['ipv4'][address]['ip'])


    #Loop through ISIS instances in all VRFs
    for instance in show_isis['instance']:
        for vrf in show_isis['instance'][instance]['vrf']:
            areaid = str(show_isis['instance'][instance]['vrf'][vrf]['area_address'][0])
            systemid = str(show_isis['instance'][instance]['vrf'][vrf]['system_id'])

            #Loop through interfaces associated with ISIS
            for interface in show_isis_interface['instance'][instance]['vrf'][vrf]['interfaces']:
                if 'ipv4' in show_isis_interface['instance'][instance]['vrf'][vrf]['interfaces'][interface].keys():
                    isis_ipv4 = str(show_isis_interface['instance'][instance]['vrf'][vrf]['interfaces'][interface]['ipv4'])
                    isis_subnet = str(show_isis_interface['instance'][instance]['vrf'][vrf]['interfaces'][interface]['ipv4_subnet'])
            
                    row_data = [ mgmt_ip, instance, areaid, systemid, vrf, interface, isis_ipv4, isis_subnet]

                    with open(csv_filename, 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(row_data)
                    
                    row_data = []