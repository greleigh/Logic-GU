---
layout: page
title: Publications
permalink: publications
published: true
---

Publications by the logic group of the [Department of Philosophy, Linguistics and Theory of Science](https://www.gu.se/flov) at the University of Gothenburg.

## Publications

{% assign sorted_pubs = site.data.publications | sort:'pubyear' | reverse %}
{% for pub in sorted_pubs %}
{% assign person = site.data.people[member] %}
 - {% for author in pub.authors %}{% if forloop.last %}{% unless forloop.first %}and {% endunless %}{% endif %}{{ author.first_name }} {{ author.last_name }}{% if forloop.last %}.{% else %},{% endif %} {% endfor %} [{{ pub.title }}](https://gup.ub.gu.se/publication/{{ pub.id }}) {{ pub.sourcetitle }}, {{ pub.pubyear}}.
{% endfor %}
