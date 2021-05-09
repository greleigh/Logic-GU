---
layout: default
title: Home
seminarBlock: 21VT
---
**NB. This website is under construction.**
## The Logic Group at the University of Gothenburg

Welcome to the webpage of the logic group at the [University of Gothenburg](https://www.gu.se).
Information about our research and activities can be found through the links to the left.
More detailed information is available through the [personal pages]({% link _pages/about.md %}) of group members and our university-hosted [webpage](https://www.gu.se/en/flov/our-research/research-areas/research-in-logic-and-mathematical-methodology).

{% comment %}
  Moving on to seminars ...
  First set the seminar period of interest
{% endcomment %}
{% assign semester = site.data.semesters[page.seminarBlock] %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "semester.start-date < item.date and item.date < semester.end-date" %}


## Research seminars in {{ site.data.semesters[page.seminarBlock].name }}

For up to date information, including location of talks, sign up to the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic).
Details of past seminars can be found in the [archive]({% link _pages/seminars.md %}).

{% for seminar in seminars %}
{% if seminar.excerpt == seminar.content %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt tags=seminar.tags %}
{% else %}
{% capture forward %}{% link _pages/seminars.md %}#{{ seminar.speaker | append: '-' | append: seminar.title | slugify}}{% endcapture %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt forward=forward tags=seminar.tags %}
{% endif %}
{% endfor %}

