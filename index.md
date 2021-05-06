---
layout: default
title: Home
---
## The Logic Group at GU

This is a sample page. We can have [seminars](#seminars) listed below and separate pages for [projects]({% link 5projects.md %}), [upcoming events](./events.html) and [us]({% link 8members.md %})! We can even link to the _static_ [GU page](https://www.gu.se/en/flov/our-research/research-areas/research-in-logic-and-mathematical-methodology)!

All this, and more.

Finally, sign up to our [mailing list](https://listserv.gu.se/sympa/subscribe/logic) to stay up to date.

## Upcoming Seminars<a name="seminars"></a>

<ul class="seminar">
  {% for seminar in site.seminars %}
    <li>
      <span class="seminar-speaker">{{ seminar.speaker }}</span> (<span class="seminar-affil">{{ seminar.affil }}</span>) – <span class="seminar-title">{{ seminar.title }}</span>
      <div class="seminar-date">{{ seminar.date | date_to_string }}</div>
      <div class="abstract">{{ seminar.excerpt }}
      {% if seminar.excerpt != seminar.content %}
        <p><a href="{{ seminar.url }}">(&#8230; read full abstract &#8230;)</a></p>
      {% endif %}
      </div>
    </li>
  {% endfor %}
</ul>

Past seminars are in the [archive](./seminars.html).

### Contact

Under construction
