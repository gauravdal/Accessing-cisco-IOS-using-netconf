from device_info import ios_xe1
from ncclient import manager
from pprint import pprint
import xmltodict

netconf_filter = open('filter-ietf-interfaces.xml','r').read()

with manager.connect(host= ios_xe1['address'],
                     port= ios_xe1['port'],
                     username= ios_xe1['username'],
                     password= ios_xe1['password'],
                     hostkey_verify= False) as m:

    netconf_reply = m.get(netconf_filter)

    #print(netconf_reply)

    #processing the xml and store in useful dictionaries

    intf_details = xmltodict.parse(netconf_reply.xml)['rpc-reply']['data']

    #print(intf_details)

    intf_config = intf_details['interfaces']['interface']

    #pprint(intf_config)

    pprint('')
    pprint('Interface details')
    print(' Name: {}'.format(intf_config['name']['#text']))