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

## The 2024 Lindström Lectures

We pleased to announce that the 2024 Lindström Lecture series is **Phokion Kolaitis**, Distinguished Research Professor at UC Santa Cruz and a Principal Research Staff Member at the IBM Almaden Research Center, US.

The Public Lindström Lecture will take place on **Monday, 15 April 2024, 18--20** in the Faculty of Humanities. For room location, see the [homepage of the Lindström Lectures](https://www.gu.se/en/flov/the-lindstrom-lectures).

The Research Lecture will take place on **Wednesday, 17 April 2024, 10**.
The location of the Research Lecture will be circulated through the [GU Logic mailing list]({{ logic-ML }}). Alternatively, contact [{{ contact }}](mailto:{{ contact-email }}).

{% assign lectures = site.categories['seminars'] | where_exp:"item", "item.ll_year == 2024" %}
{% assign public-lecture = lectures | find:"ll_kind", "public" %}
{% assign research-lecture = lectures | find:"ll_kind", "research" %}

{% include lindstrom-entry.html talk=public-lecture public=true %}

{% include lindstrom-entry.html talk=research-lecture public=false %}


## Previous Lindström Lectures

{% assign LLs = site.pages | where:"lindstrom-lecture","true" | where_exp:"item","item.year < 2023" | reverse %}
{% for lecture in LLs %}
* [{{ lecture.title }}]({% link {{ lecture.path }} %}): {{ lecture.speaker }}
{%- endfor %}
