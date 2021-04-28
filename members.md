## Members of the Logic Group at GU

A list of current members with links to GU homepages

# Current members

{% for member in site.members %}
* **[{{ member.name }}]({{ member.homepage }}) – {{ member.position }}**
  {{ member.content | markdownify }}
{% endfor %}

# Previous and associate members
