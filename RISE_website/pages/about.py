import reflex as rx
from RISE_website.components.navbar import navbar

def about():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("About RISE Lab", size="2xl", margin_bottom="1em"),
                rx.text(
                    "The Research in Software Engineering (RISE) Lab is dedicated to advancing the field of software engineering through innovative research and collaboration."
                ),
                rx.box(
                    rx.heading("Our Mission", size="xl"),
                    rx.text(
                        "To improve software development practices, tools, and methodologies through cutting-edge research and industry partnerships."
                    ),
                    margin_top="1em",
                ),
                rx.box(
                    rx.heading("Our Vision", size="xl"),
                    rx.text(
                        "To be at the forefront of software engineering research, driving innovation and shaping the future of software development."
                    ),
                    margin_top="1em",
                ),
                rx.box(
                    rx.heading("Contact Us", size="xl"),
                    rx.vstack(
                        rx.text("Email: info@riselab.example.com"),
                        rx.text("Phone: +1 (123) 456-7890"),
                        rx.text("Address: 123 University Ave, Anytown, AN 12345"),
                        align_items="flex-start",
                    ),
                    margin_top="1em",
                ),
                max_width="800px",
                width="100%",
                margin="0 auto",
                padding="2em",
                spacing="1em",
            ),
            margin_top="5em",  # 添加顶部边距以避免内容被 navbar 遮挡
        )
    )

# __all__ = ["about"]