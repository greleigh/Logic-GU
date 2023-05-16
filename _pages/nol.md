---
layout: page
title: Nordic Online Logic Seminars
permalink: seminars/nol
contact: graham
---
{%- assign nol = site.data.nol -%}
The Nordic Online Logic Seminar (NOL Seminar) is organised monthly over Zoom, with expository talks on topics of interest for the broader logic community.
The seminar is open for professional or aspiring logicians and logic aficionados worldwide.

The tentative time slot is Monday, 16.00-17.30 (Sweden).
If you wish to receive the Zoom ID and password for it, as well as further announcements, please subscribe to the [NOL Seminar mailing list]({{ nol.mailing_list }}).

NOL seminar organisers\
Valentin Goranko and Graham Leigh

{% comment %}
  Moving on to seminars ...
  First set the seminar period of interest
{% endcomment %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "item.tags contains 'NOL'" %}

## Talks in the Nordic Online Logic Seminar

{% for nol-seminar in seminars %}
  {% include seminar-entry.html talk=nol-seminar LL_tag=true %}
{% endfor %}