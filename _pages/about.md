---
layout: page
title: The Group
permalink: about
published: true
---

The logic group is part of the [Department of Philosophy, Linguistics and Theory of Science](https://www.gu.se/flov) at the University of Gothenburg.

Our group has a broad expertise in mathematical, philosophical and computational logic.
We organise a [bi-weekly research seminar]({% link _pages/seminars.md %}), the annual [Lindström Lectures]({% link _pages/lindstrom-lectures.md %}) and various other [logic-themed events]({% link _pages/activities.md %}).
Group members also teach in the [Master in Logic programme]({% link _pages/MiL.md %}).

We are one of the member groups of the [Scandinavian Logic Society]({{ site.data.links['sls'].url }}) which organises a number of events promoting logic in the Nordic regions, for instance the [Nordic Online Logic Seminar]({% link _pages/nol.md %}).

## Current members

{% for member in site.data.members %}
{% assign person = site.data.people[member] %}
 - **{% if person.homepage %}[{{ person.full-name }}]({{ person.homepage }} "{{ person.full-name }}"){% else %}{{ person.full-name }}{% endif %}** – _{{ person.position }}_
    {{ person.description | markdownify }}
    {% endfor %}

## Past and affiliate members

{% for member in site.data.members-past-affiliate %}
{% assign person = site.data.people[member] %}
 - **{% if person.homepage %}[{{ person.full-name }}]({{ person.homepage }} "{{ person.full-name }}"){% else %}{{ person.full-name }}{% endif %}** – _{{ person.position }}_
    {{ person.description | markdownify }}
    {% endfor %}
