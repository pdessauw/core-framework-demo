from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


Menu.add_item(
    "main", MenuItem("Home", reverse("core_website_home"))
)

Menu.add_item(
    "main", MenuItem("Help", reverse("core_website_help"))
)
