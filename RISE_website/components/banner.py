import reflex as rx
from reflex.components.component import NoSSRComponent

class PixelCanvas(NoSSRComponent):
    """A pixel canvas component."""

    library = "/public/PixelCanvas"
    tag = "PixelCanvas"

def banner():
    return rx.vstack(
        PixelCanvas.create(),
        rx.vstack(
            rx.heading(
                "RISE @ SIT",
                size=rx.breakpoints(sm="4", md="3", lg="2"),
                font_weight="bold"
            ),
            rx.text(
                "Research Lab of Software Engineering for the ",
                font_size=rx.breakpoints(sm="md", md="lg", lg="xl")
            ),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            text_align="center",
            z_index="10",
            color="black",
        ),
        width="100%",
        height="100vh",
        overflow="hidden",
        position="relative",
    )