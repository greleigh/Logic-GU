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
<div class="seminar" id="{{ talk.speaker | append: '-' | append: talk.title | slugify }}">
    <span class="seminar-speaker">{{ talk.speaker }}</span> (<span class="seminar-affil">{{ talk.affil }}</span>) – <span class="seminar-title">{{ talk.title }}</span>
    <div class="seminar-date">{{ talk.date | date: "%A, %d %B %Y at %H:%M (%Z)" }}</div>
    <div class="abstract">
      {{ talk.content }}
    </div>
  </div>
{% endfor %}

{% endunless %}
{% endfor %}

Research seminars prior to 2021 are in a [separate archive]({% link _pages/archive/seminar-2014-2019.md %}).
