import reflex as rx
from RISE_website.components.navbar import navbar
from RISE_website.components.banner import banner

def index():
    return rx.box(
        navbar(),
        banner(),
        # rx.vstack(
        #     rx.heading("欢迎来到RISE实验室"),
        #     rx.text("我们致力于推进...领域的研究"),
        #     rx.button("了解更多", on_click=rx.redirect("/about")),
        #     spacing="1em",
        #     padding="2em",
        # ),
        # width="100%",
    )

# __all__ = ["index"]