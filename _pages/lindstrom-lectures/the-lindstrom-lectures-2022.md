---
layout: lindstrom-lectures
title: The Lindström Lectures 2022
speaker: Sara Negri
year: 2022
---
{%- assign contact = site.data.people['graham'].name -%}
{%- assign contact-email = site.data.people['graham'].email -%}

The 2022 [Lindström Lectures]({% link _pages/lindstrom-lectures.md %}) were delivered in June 2022 by **Sara Negri**, Professor of Mathematics at the University of Genoa.

The Public Lindström Lecture took place on **Monday, 20 June 2022** at the [Faculty of Humanities](https://www.gu.se/en/humanities) of Gothenburg University and online. 
Details are available on the [GU page about the lectures](https://www.gu.se/en/flov/the-lindstrom-lectures).

The Research Lecture took place on **Wednesday, 22 June 2022** at the [Department of Philosohy, Linguistics and Theory of Science](https://www.gu.se/en/flov).
For more information about the lectures contact [{{ contact }}](mailto:{{ contact-email }}).

{% assign lectures = site.categories['seminars'] | where:"ll_year", 2022 %}
{% assign public-lecture = lectures | find:"ll_kind", "public" %}
{% assign research-lecture = lectures | find:"ll_kind", "research" %}

{% include lindstrom-entry.html talk=public-lecture public=true %}

{% include lindstrom-entry.html talk=research-lecture public=false %}
