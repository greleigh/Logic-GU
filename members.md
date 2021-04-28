## Members of the Logic Group at GU

A list of current members with links to GU homepages

{% for member in site.members %}
  <h2>{{ member.name }} - {{ member.position }}</h2>
  <p>{{ member.content | markdownify }}</p>
{% endfor %}

Previous and associate members
