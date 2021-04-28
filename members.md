## Members of the Logic Group at GU

A list of current members with links to GU homepages

{% for member in site.members %}
  <h3><a href="{{ member.homepage }}">{{ member.name }}</a> – {{ member.position }}</h3>
  <p>{{ member.content | markdownify }}</p>
{% endfor %}

Previous and associate members
