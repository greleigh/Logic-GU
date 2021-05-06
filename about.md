---
layout: page
title: About
permalink: about
---

The logic group is part of the [Department of Philosophy, Linguistics and Theory of Science](https://www.gu.se/flov) at the University of Gothenburg.

We organise [bi-weekly research seminar]({% link seminars.md %}), the annual Lindström Lectures plus various other [logic-themed events]({% link events.md %}).
Plus the [Master in Logic]({% link _pages/MiL.md %}).

### Current members

<ul>
{% for member in site.data.members %}
<li> <strong>{% if member.homepage %} <a href="{{ member.homepage }}">{% endif %}{{ member.name }}{% if member.homepage %}</a>{% endif %} – {{ member.position }}</strong> {{ member.description | markdownify }} </li>
{% endfor %}
</ul>

### Previous and associate members
