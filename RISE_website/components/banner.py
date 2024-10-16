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
                font_size=rx.breakpoints(sm="32px", md="40px", lg="48px"),
                font_weight="bold"
            ),
            rx.text(
                "Research in Software Engineering for the Future",
                font_size=rx.breakpoints(sm="16px", md="18px", lg="20px")
            ),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            text_align="center",
            z_index="10",
            color="black",
            width="80%",  # 限制文本宽度
            max_width="800px",  # 设置最大宽度
        ),
        width="100%",
        height="100vh",
        overflow="hidden",
        position="relative",
    )