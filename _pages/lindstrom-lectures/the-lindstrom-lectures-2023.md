---
layout: lindstrom-lectures
title: The Lindström Lectures 2023
speaker: Rineke Verbrugge
year: 2023
---
{%- assign contact = site.data.people['graham'].name -%}
{%- assign contact-email = site.data.people['graham'].email -%}

The 2023 [Lindström Lectures]({% link _pages/lindstrom-lectures.md %}) were delivered in June 2023 by **Rineke Verbrugge**, Professor of Logic and Cognition at the Bernoulli Institute of Mathematics, Computer Science and Artificial Intelligence, University of Groningen, The Netherlands.

The Public Lindström Lecture took place on **Thursday, 11 May 2023** at the [Faculty of Humanities](https://www.gu.se/en/humanities) of Gothenburg University and online. The Research Lecture took place on **Friday, 12 May 2022** at the [Department of Philosohy, Linguistics and Theory of Science](https://www.gu.se/en/flov).

See below for information about the talks. Further details and contact information are available on the [GU page about the lectures](https://www.gu.se/en/flov/the-lindstrom-lectures).

{% assign lectures = site.categories['seminars'] | where:"ll_year", 2023 %}
{% assign public-lecture = lectures | find:"ll_kind", "public" %}
{% assign research-lecture = lectures | find:"ll_kind", "research" %}

{% include lindstrom-entry.html talk=public-lecture public=true %}

{% include lindstrom-entry.html talk=research-lecture public=false %}
