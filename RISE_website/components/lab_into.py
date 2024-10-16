import reflex as rx

def lab_introduction(professor):
    return rx.box(
        rx.vstack(
            rx.heading("Lab Introduction", size="xl", margin_bottom="1em"),
            rx.hstack(
                rx.image(
                    src=professor["image"],
                    alt=professor["name"],
                    width="200px",
                    height="200px",
                    object_fit="cover",
                    border_radius="lg"
                ),
                rx.vstack(
                    rx.heading(professor["name"], size="lg"),
                    rx.text(professor["title"]),
                    rx.text(professor["bio"]),
                    align_items="flex-start",
                ),
                spacing="2em",
                align_items="flex-start",
            ),
            width="100%",
            padding="2em",
            background="gray.50",
            border_radius="xl",
        ),
        width="100%",
    )