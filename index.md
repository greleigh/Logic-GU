---
layout: default
title: Home
listPeriod: 21VT
---
**NB. This website is under construction.**

## The Logic Group at GU

Welcome to the webpage of the logic group at the [University of Gothenburg](https://www.gu.se).
Information about our research and activities can be found through the links to the left.
More detailed information is available through the [personal pages]({% link _pages/about.md %}) of group members and our university-hosted [webpage](https://www.gu.se/en/flov/our-research/research-areas/research-in-logic-and-mathematical-methodology).

## Research seminars in Spring 2021

For up to date information, including location of talks, sign up to the [GU Logic mailing list](https://listserv.gu.se/sympa/subscribe/logic).

<ul class="seminar">
  {% for seminar in site.seminars %}
  {% if seminar.tags contains page.listPeriod %}
    <li>
      <span class="seminar-speaker">{{ seminar.speaker }}</span> (<span class="seminar-affil">{{ seminar.affil }}</span>) – <span class="seminar-title">{{ seminar.title }}</span>
      <div class="seminar-date">{{ seminar.date | date: "%A, %d %B %Y at %H:%M (%Z)" }}</div>
      <div class="abstract">{{ seminar.excerpt }}
      {% if seminar.excerpt != seminar.content %}
        {% assign link = seminar.title | slugify %}
        <p><a href="{% link _pages/seminars.md %}#{{ link }}">(&#8230; read full abstract &#8230;)</a></p>
      {% endif %}
      </div>
    </li>
    {% endif %}
  {% endfor %}
</ul>

Details of past seminars can be found in the [archive]({% link _pages/seminars.md %}).
