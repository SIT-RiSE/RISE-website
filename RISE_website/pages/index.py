import reflex as rx
from RISE_website.components.navbar import navbar
from RISE_website.components.banner import banner

def index():
    return rx.box(
        navbar(),
        banner()
    )

# __all__ = ["index"]