---
layout: page
title: The Group
permalink: about
published: true
---

The logic group is part of the [Department of Philosophy, Linguistics and Theory of Science](https://www.gu.se/flov) at the University of Gothenburg.

We organise [bi-weekly research seminar]({% link _pages/seminars.md %}), the annual Lindström Lectures plus various other [logic-themed events]({% link _pages/activities.md %}).
Plus the [Master in Logic]({% link _pages/MiL.md %}).

## Current members

{% for member in site.data.members %}
{% assign person = site.data.people[member] %}
 - **{% if person.homepage %}[{{ person.name }}]({{ person.homepage }} "{{ person.name }}"){% else %}{{ person.name }}{% endif %}** – _{{ person.position }}_
    {{ person.description | markdownify }}
{% endfor %}
