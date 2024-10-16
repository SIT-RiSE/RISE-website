import reflex as rx
from RISE_website.styles.common import link_style

def opening_positions(positions):
    if not positions:
        return rx.box()
    
    return rx.box(
        rx.vstack(
            rx.heading("Open Positions", size="xl", margin_bottom="1em"),
            rx.text(
                positions["description"],
                margin_bottom="1em",
                max_width="800px",
                text_align="center",
            ),
            rx.link(
                positions["link_text"],
                href=positions["link_url"],
                is_external=True,
                style=link_style,
                padding="0.5em 1.5em",
                border_radius="full",
                background="black",
                color="white",
                transition="all 0.3s ease-in-out",
                _hover={
                    "background": "gray.800",
                    "transform": "translateY(-2px)",
                    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                },
            ),
            spacing="1em",
            align_items="center",
            justify_content="center",
            padding="2em",
            width="100%",
            background="white",
            color="black",
        ),
        width="100%",
    )