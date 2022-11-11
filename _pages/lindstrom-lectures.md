---
layout: page
title: The Lindström Lectures
permalink: lindstrom-lectures
---
{% assign logic-ML = site.data.links['gu-mailing-list'].url %}
{% assign contact = site.data.people['graham'].name %}
{% assign contact-email = site.data.people['graham'].email %}

The Department of Philosophy, Linguistics and Theory of Science at the University of Gothenburg launched a lecture series in 2013 to celebrate the singular achievements of Per Lindström, former professor of logic at the department.

Annually, a distinguished logician is invited to deliver a general lecture to the public, and a specialized presentation at the logic seminar.

[About Per (Pelle) Lindström]({% link _pages/lindstrom-lectures/per-lindstrom.md %})

## The Lindström Lectures 2023 edition

The 2023 Lindström Lectures will be given by **Rineke Verbrugge**, Professor of Logic and Cognition at the University of Groningen, Netherlands.

The Public and Research Lectures will take place in **May, 2023**.
Full details will be released in due course.

{% comment %}
The Public Lindström Lecture will take place on **Monday, 20 June 2022, 18--20** at the [Faculty of Humanities](https://www.gu.se/en/humanities) of Gothenburg University and online. Details will be posted on the [GU page about the Lindström Lectures](https://www.gu.se/en/flov/the-lindstrom-lectures).

The Research Lecture will take place on **Wednesday, 22 June 2022, 10--12**. The location of the Research Lecture will be circulated through the [GU Logic mailing list]({{ logic-ML }}) or contact [{{ contact }}](mailto:{{ contact-email }}).

{% assign lectures = site.categories['seminars'] | where_exp:"item", "item.tags contains 'LL22'" %}
{% assign public-lecture = lectures | find:"public", true %}
{% assign research-lecture = lectures | find:"public", nil %}

{% include lindstrom-entry.html talk=public-lecture public=true %}

{% include lindstrom-entry.html talk=research-lecture public=false %}

{% endcomment %}

## Previous Lindström Lectures

{% assign LLs = site.pages | where:"lindstrom-lecture","true" | where_exp:"item","item.year < 2023" | reverse %}
{% for lecture in LLs %}
* [{{ lecture.title }}]({% link {{ lecture.path }} %}): {{ lecture.speaker }}
{%- endfor %}
