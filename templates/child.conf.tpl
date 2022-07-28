{% extends 'base.conf.tpl' -%}
{% block head -%}
{{ super() }}
hello, coming from the inside world
{% endblock -%}
{% block hostname_suffix -%}
router-01
{% endblock %}