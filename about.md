---
layout: page
title: About
permalink: about
---
## Members of the Logic Group at GU

A list of current members with links to GU homepages

## Current members

<ul>
{% for member in site.data.members %}
<li> <strong><a href="{{ member.homepage }}">{{ member.name }}</a> – {{ member.position }}</strong> {{ member.description | markdownify }} </li>
{% endfor %}
</ul>

## PhD students

## Previous and associate members
