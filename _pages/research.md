---
layout: page
title: Research
permalink: research
---

### Current and ongoing research projects

{% for project in site.projects %}
 - [*{{ project.title }}*]({% link {{project.path}} %}) lead by *{{ project.pi }}*
 {% endfor %}