---
layout: page
title: Seminars
permalink: seminars
contact: graham
---
{% assign contact = site.data.people[page.contact] %}
{% assign MiL = site.data.links['MiL-canvas'] %}
{% assign logic-ML = site.data.links['gu-mailing-list'].link %}

See below for a list of all previous and upcoming seminars in the _Gothenburg Research Seminar in Logic_ and the _Nordic Online Logic Seminar_. We also run a bi-weekly _Colloquium in Logic_ focused in the Masters in Logic; details and schedules are listed on the [course page of the Masters Programme]({{ MiL.link }}).

The research seminar meets on alternate Fridays at 10.15. Talk locations (i.e., Zoom link) are distributed in the [GU Logic mailing list]({{ logic-ML }}). Alternatively, contact [{{ contact.name }}]({{ contact.homepage }}) directly.

{% comment %}
  Moving on to seminars ...
  First set the seminar period of interest
{% endcomment %}
{% for period in site.data.semesters %}
{% assign semester = period[1] %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "semester.start-date < item.date and item.date < semester.end-date" %}

{% unless seminars == empty %}

## {{ semester.name }}

{% for seminar in seminars %}
  {%- unless seminar.speaker == "Logic Seminar" -%}
  {% include seminar-entry.html talk=seminar nol_tag=true LL_tag=true %}
  {%- endunless -%}
{% endfor %}

{% endunless %}
{% endfor %}

Research seminars prior to 2020 are in a [separate archive]({% link _pages/archive/seminar-2014-2019.md %}).
