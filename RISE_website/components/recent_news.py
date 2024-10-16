import reflex as rx

def recent_news(news_items):
    return rx.box(
        rx.heading("Recent News", size="xl", margin_bottom="1em"),
        rx.vstack(
            *[rx.box(
                rx.text(item["date"], font_weight="bold"),
                rx.text(item["content"]),
                padding="1em",
                border="1px solid",
                border_color="gray.200",
                border_radius="md",
                margin_bottom="1em",
            ) for item in news_items],
            width="100%",
            align_items="stretch",
        ),
        width="100%",
        padding="2em",
        background="gray.50",
    )