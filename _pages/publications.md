---
layout: page
title: Publications
permalink: publications
published: true
---

Below is the list of publications by the logic group of the [Department of Philosophy, Linguistics and Theory of Science](https://www.gu.se/flov) at the University of Gothenburg as archived by the [Gothenburg
University Library Publication Database](https://www.ub.gu.se/en).
More information can be found at group [members' pages]({% link _pages/about.md %}).

## List of publications by members of the Logic Group

<div class="publist" markdown=1>
{% assign sorted_pubs = site.data.publications | sort:'pubyear' | reverse %}
{% for pub in sorted_pubs %}
{% assign person = site.data.people[member] %}
 - {% for author in pub.authors %}{% if forloop.last %}{% unless forloop.first %}and {% endunless %}{% endif %}{{ author.first_name }} {{ author.last_name }}, {% endfor %} {{ pub.pubyear}}. [{{ pub.title }}](https://gup.ub.gu.se/publication/{{ pub.id }}), <sourcetitle>{{ pub.sourcetitle }}</sourcetitle>.
{% endfor %}
</div>
