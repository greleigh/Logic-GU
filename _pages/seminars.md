---
layout: page
title: Seminars
permalink: seminars
contact: graham
---
{% assign contact = site.data.people[page.contact] %}

See below for a list of all previous and upcoming seminars. The research seminar meets on alternate Fridays at 10.15. Talk locations (i.e., Zoom link) are distributed in the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic). Alternatively, contact [{{ contact.name }}]({{ contact.homepage }}) directly.

{% comment %}
  Moving on to seminars ...
  First set the seminar period of interest
{% endcomment %}
{% for period in site.data.semesters %}
{% assign semester = period[1] %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "semester.start-date < item.date and item.date < semester.end-date" %}

{% unless seminars == empty %}

## {{ semester.name }}

{% for talk in seminars %}
{% if talk.tags contains "NOL" %}
  {% assign is-nol = true %}
{% else %}
  {% assign is-nol = false %}
{% endif %}
{% include seminar-entry.html speaker=talk.speaker affil=talk.affil title=talk.title date=talk.date abstract=talk.content nol=is-nol %}
{% endfor %}

{% endunless %}
{% endfor %}

Research seminars prior to 2020 are in a [separate archive]({% link _pages/archive/seminar-2014-2019.md %}).
