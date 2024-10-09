import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("RISE Lab"),
            rx.spacer(),
            rx.link("Home", href="/"),
            rx.link("Research", href="/research"),
            rx.link("People", href="/people"),
            rx.link("About", href="/about"),
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