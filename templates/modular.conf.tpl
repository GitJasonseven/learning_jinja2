{% for port in ports -%}
    {% with port=port -%}
        {% include "port_conf.sub.conf.tpl" -%}
    {% endwith -%}
{% endfor -%}