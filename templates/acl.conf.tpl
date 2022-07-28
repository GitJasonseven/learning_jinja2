{% for host in disallowed -%}
    access-list 20 deny host {{ host }}
{% endfor -%}

{% for host in allowed -%}
    access-list 20 permit host {{ host }}
{% endfor -%}