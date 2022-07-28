interface {{ port['type'] }} {{ port['slot'] }} / {{ port['port_num'] }}

{%- if port['intf_type'] == "access" %}
    switchport mode {{ port['intf_type'] }}
    switchport access vlan {{ port['vlan'] }}
{%- endif %}

{%- if port['intf_type'] == "trunk" %}
    switchport mode {{ port['intf_type'] }}
    switchport trunk allowed vlan add {{ port['vlan'] }}
{%- endif %}