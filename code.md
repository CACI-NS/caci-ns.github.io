---
layout: page
title: Code
permalink: /code/
---

{% for repo in site.github.public_repositories %}

{% if repo.fork == false and repo.name != "CACI-NS" and repo.name != "caci-ns.github.io" %}

## [{{ repo.name }}]({{ repo.html_url }})

{{repo.description}}

Topics: {{ repo.topics | array_to_sentence_string}}

Last updated: {{repo.updated_at | date_to_string}}

{% endif %}

{% endfor %}
