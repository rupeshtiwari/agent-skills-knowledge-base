---
layout: default
---
{% capture hub %}{% include_relative README.md %}{% endcapture %}
{{ hub | replace: 'href="troubleshooting/README.md"', 'href="troubleshooting/"' | replace: 'href="catalog/collections.md#', 'href="catalog/collections.html#' }}
