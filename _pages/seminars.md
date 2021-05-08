---
layout: page
title: Seminars
permalink: seminars
published: true
---
Up to date information, including location of talks, is distributed via the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic).

{% assign sorted = site.seminars | reverse %}
{% for talk in sorted %}
  <div class="seminar" id="{{ talk.title | slugify }}">
    <span class="seminar-speaker">{{ talk.speaker }}</span> (<span class="seminar-affil">{{ talk.affil }}</span>) – <span class="seminar-title">{{ talk.title }}</span>
    <div class="seminar-date">{{ talk.date | date: "%A, %d %B %Y at %H:%M (%Z)" }}</div>
    <div class="abstract">
      {{ talk.content }}
    </div>
  </div>
{% endfor %}

Research seminars prior to 2021 are in a [separate archive]({% link _pages/archive/seminar-archive.md %}).
