---
layout: page
title: The Lindström Lectures
permalink: lindstrom-lectures
---

The Department of Philosophy, Linguistics and Theory of Science at the University of Gothenburg launched a lecture series in 2013 to celebrate the singular achievements of Pelle Lindström, former professor of logic at the department.

Annually, a distinguished logician is invited to deliver a general lecture to the public, and a specialized presentation at the logic seminar.

[About Per (Pelle) Lindström]({% link _pages/lindstrom-lectures/per-lindstrom.md %})

## Next seminar

The 2020 instalment was postponed due to the Corona virus situation. New dates will be announced in due course.

## Previous Lindström Lectures

{% assign LLs = site.pages | where:"lindstrom-lecture","true" | reverse %}
{% for lecture in LLs %}
* [{{ lecture.title }}]({% link {{ lecture.path }} %}): {{ lecture.speaker }} {% endfor %}
