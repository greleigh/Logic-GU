---
layout: lindstrom-lectures
title: The Lindström Lectures 2022
speaker: Sara Negri
year: 2022
---
The 2022 [Lindström Lectures]({% link _pages/lindstrom-lectures.md %}) were delivered in June 2022 by Sara Negri, Professor of Mathematics at the University of Genoa.

{% assign lectures = site.categories['seminars'] | where_exp:"item", "item.tags contains 'LL22'" %}
{% assign public-lecture = lectures | find:"public", true %}
{% assign research-lecture = lectures | find:"public", nil %}

{% include lindstrom-entry.html talk=public-lecture public=true %}

{% include lindstrom-entry.html talk=research-lecture public=false %}
