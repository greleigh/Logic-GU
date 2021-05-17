---
layout: default
title: Home
seminarBlock: 21VT
---
**NB. This website is under construction.**
## The Logic Group at the University of Gothenburg

Welcome to the webpage of the logic group at the [University of Gothenburg](https://www.gu.se).
Information about our research and activities can be found through the links to the left.
More detailed information is available through the [personal pages]({% link _pages/about.md %}) of group members and our university-hosted [webpage]({{ site.data.links['flov-logic-group'].link }}).

## Upcoming seminars

The list of past seminars is available [here]({% link _pages/seminars.md %}).

{% comment %}
  Moving on to seminars ...
  1- Find the (published) seminars with a future date.
  2- Reverse the list (most recent first)
  3- display each seminar using the template _include/seminar-entry.html
{% endcomment %}
{% assign build-date = site.time %}
{% assign upcoming-seminars = site.categories['seminars'] | where_exp:"item", "build-date < item.date" | reverse %}

{% for seminar in upcoming-seminars %}
{% comment %}
  Check if seminar is in NOL.
  Then determine whether to print whole abstract or excerpt.
{% endcomment %}
{% if seminar.tags contains "NOL" %}
  {% assign is-nol = true %}
{% else %}
  {% assign is-nol = false %}
{% endif %}
{% if seminar.excerpt == seminar.content %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt nol=is-nol %}
{% else %}
{% capture forward %}{% link _pages/seminars.md %}#{{ seminar.speaker | append: '-' | append: seminar.title | slugify}}{% endcapture %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt forward=forward nol=is-nol %}
{% endif %}
{% endfor %}

{% comment %}
[comment]: # (Display all seminars in the semester block {{ page.seminarBlock }} )

{% assign semester = site.data.semesters[page.seminarBlock] %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "semester.start-date < item.date and item.date < semester.end-date" %}

## Research seminars in {{ site.data.semesters[page.seminarBlock].name }}

For up to date information, including location of talks, sign up to the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic).
Details of past seminars can be found in the [archive]({% link _pages/seminars.md %}).

{% for seminar in seminars %}
{% comment %}
  Check if seminar is in NOL.
  Then determine whether to print whole abstract or excerpt.
{% endcomment %}
{% if seminar.tags contains "NOL" %}
  {% assign is-nol = true %}
{% else %}
  {% assign is-nol = false %}
{% endif %}
{% if seminar.excerpt == seminar.content %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt nol=is-nol %}
{% else %}
{% capture forward %}{% link _pages/seminars.md %}#{{ seminar.speaker | append: '-' | append: seminar.title | slugify}}{% endcapture %}
{% include seminar-entry.html speaker=seminar.speaker affil=seminar.affil title=seminar.title date=seminar.date abstract=seminar.excerpt forward=forward nol=is-nol %}
{% endif %}
{% endfor %}

{% endcomment %}