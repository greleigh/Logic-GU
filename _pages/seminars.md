---
layout: page
title: Seminars
permalink: seminars
contact: graham
---
See below for a list of all previous and upcoming seminars.

Up-to-date information, including location of talks, is distributed via the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic).

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
{% include seminar-entry.html speaker=talk.speaker affil=talk.affil title=talk.title date=talk.date abstract=talk.content tags=talk.tags %}
{% endfor %}

{% endunless %}
{% endfor %}

Research seminars prior to 2021 are in a [separate archive]({% link _pages/archive/seminar-2014-2019.md %}).
