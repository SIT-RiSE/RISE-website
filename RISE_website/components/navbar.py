import reflex as rx
from RISE_website.styles.common import link_style

def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("RISE Lab"),
            rx.spacer(),
            rx.link("Home", href="/", style=link_style),
            rx.link("Research", href="/research", style=link_style),
            rx.link("Publications", href="/publications", style=link_style),  # Add this line
            rx.link("People", href="/people", style=link_style),
            rx.link("About", href="/about", style=link_style),
            spacing="1em",
        ),
        width="100%",
        padding="1em",
        background_color="rgba(255, 255, 255, 0.8)",
        backdrop_filter="blur(10px)",
        position="fixed",
        top="0px",
        z_index="1000",
    )