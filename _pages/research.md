---
layout: page
title: Research
permalink: research
published: false
---

### Current and ongoing research projects

{% for project in site.projects %}
 - [*{{ project.title }}*]({% link {{project.path}} %}) lead by *{{ project.pi }}*
 {% endfor %}