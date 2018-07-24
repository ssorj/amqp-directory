import site as _site
import sys as _sys

_sys.path.extend(_site.getsitepackages())

import yaml as _yaml

_component_html = """
<div class="component">
  <a class="component-icon" href="{url}"><img src="images/icons/{icon_file}" height="{icon_height}" width="{icon_width}"/></a>
  <div class="component-text">
    <a class="component-title" href="{url}">{name}</a>
    <span class="component-tags">{tags_html}</span>
    <p class="component-description">{description}</p>
    <p class="component-links">
      <a href="{url}">Home</a>
      {links_html}
    </p>
  </div>
</div>
"""

with open("data/icons.yaml") as f:
    _icon_data = _yaml.safe_load(f)

def components(data_file):
    with open(f"data/{data_file}") as f:
        data = _yaml.safe_load(f)

    out = list()

    for component in data["components"]:
        component["tags_html"] = ""

        if "tags" in component:
            tags = list()

            for tag in component["tags"]:
                tags.append(f"<span>{tag.upper()}</span>")

            component["tags_html"] = " ".join(tags)

        try:
            icon_file = component["icon_file"]
        except KeyError:
            icon_file = data["icon_file"]
            component["icon_file"] = icon_file

        icon_data = _icon_data[icon_file]

        component["icon_height"] = icon_data["height"]
        component["icon_width"] = icon_data["width"]

        links = list()

        if "docs_url" in component:
            links.append(_html_link(component["docs_url"], "Docs"))

        if "api_url" in component:
            links.append(_html_link(component["api_url"], "API"))

        if "examples_url" in component:
            links.append(_html_link(component["examples_url"], "Examples"))

        if "download_url" in component:
            links.append(_html_link(component["download_url"], "Download"))

        if "maven_url" in component:
            links.append(_html_link(component["maven_url"], "Maven"))

        if "package_url" in component:
            links.append(_html_link(component["package_url"], "Package"))

        if "source_url" in component:
            links.append(_html_link(component["source_url"], "Source"))

        component["links_html"] = "".join(links)

        out.append(_component_html.format(**component).strip())

    return "<div class=\"components\">\n{}\n</div>".format("\n".join(out))

def _html_link(href, text):
    return f"<a href=\"{href}\">{text}</a>"
