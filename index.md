---
layout: default
title: Home
seminarBlock: 21VT
---

Welcome to the webpage of the logic group at the [University of Gothenburg](https://www.gu.se).
Information about our research and activities can be found through the links to the left.
More detailed information is available through the [personal pages]({% link _pages/about.md %}) of group members and our [homepage at the University of Gothenburg]({{ site.data.links['flov-logic-group'].link }}).

## Upcoming seminars

{% comment %}
  Moving on to seminars ...
  1- Find the (published) seminars with a future date.
  2- Reverse the list (most recent first)
  3- display each seminar using the template _include/seminar-entry.html
{% endcomment %}
{% assign build-date = site.time %}
{% assign upcoming-seminars = site.categories['seminars'] | where_exp:"item", "build-date < item.date" | reverse %}
{% if upcoming-seminars == empty %}New seminars will be published shortly.{% endif %}
Past talks can be found on the [seminar page]({% link _pages/seminars.md %}).

{% for seminar in upcoming-seminars %}
  {% include seminar-entry.html talk=seminar excerpt-only=true nol_tag=true LL_tag=true %}
{% endfor %}
