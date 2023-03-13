---
layout: page
title: Categories
permalink: /categories/
---

{% for cat in site.categories %}
 {% capture cat_name %}{{ cat | first }}{% endcapture %}
## {{ cat_name}}
  {% for post in site.categories[cat_name] %}
- [{{ post.title }}]({{ site.url }}{{ post.url }})
 {% endfor %}
{% endfor %}
