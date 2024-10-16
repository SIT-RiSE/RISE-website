import reflex as rx

def news_item(item):
    return rx.box(
        rx.box(
            rx.text(item["date"], font_weight="bold"),
            rx.text(item["content"]),
            bg="white",
            border_radius="10px",
            padding="1em",
            z_index="1",
            position="relative",
        ),
        padding="2px",  # 为彩色边框留出空间
        border_radius="12px",  # 稍微大一点以包含内部内容
        margin_bottom="1em",
        transition="all 0.3s ease-in-out",
        position="relative",
        overflow="hidden",
        _before={
            "content": "''",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "right": "0",
            "bottom": "0",
            "border_radius": "12px",
            "background": "linear-gradient(45deg, rgba(255,105,180,0.8), rgba(100,149,237,0.8), rgba(50,205,50,0.8))",
            "background_size": "300% 300%",
            "opacity": "0",
            "transition": "opacity 0.3s ease-in-out",
            "z_index": "-1",
        },
        _hover={
            "transform": "translateY(-5px)",
            "_before": {
                "opacity": "1",
                "animation": "gradient 5s ease infinite",
            },
        },
    )

def recent_news(news_items):
    return rx.box(
        rx.heading("Recent News", size="xl", margin_bottom="1em"),
        rx.vstack(
            *[news_item(item) for item in news_items],
            width="100%",
            align_items="stretch",
        ),
        width="100%",
        padding="2em",
        background="gray.50",
        custom_css="""
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        """
    )