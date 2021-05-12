---
layout: page
title: Nordic Online Logic Seminars
permalink: seminars/nol
contact: graham
---
The Nordic Online Logic Seminar (NOL Seminar) is organised monthly over Zoom, with expository talks on topics of interest for the broader logic community.
The seminar is open for professional or aspiring logicians and logic aficionados worldwide.

The tentative time slot is Monday, 16.00-17.30 (Gothenburg). See the announcement for the next talk below.
If you wish to receive the Zoom ID and password for it, as well as further announcements, [please subscribe here](https://listserv.gu.se/sympa/subscribe/nordiclogic).

Valentin Goranko and Graham Leigh\
NOL seminar organisers

{% comment %}
  Moving on to seminars ...
  First set the seminar period of interest
{% endcomment %}
{% assign seminars = site.categories['seminars'] | where_exp:"item", "item.tags contains 'NOL'" %}

## Talks in the Nordic Online Logic Seminar

{% for talk in seminars %}
{% include seminar-entry.html speaker=talk.speaker affil=talk.affil title=talk.title date=talk.date abstract=talk.content %}
{% endfor %}