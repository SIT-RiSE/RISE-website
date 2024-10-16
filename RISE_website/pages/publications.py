import reflex as rx
import os
import json
from RISE_website.components.navbar import navbar
from RISE_website.components.footnote import footer

def publication_item(pub):
    return rx.box(
        rx.box(
            rx.vstack(
                rx.text(
                    pub["authors"],
                    color="gray.600",
                    font_size="xs",
                    transition="all 0.3s",
                ),
                rx.hstack(
                    rx.text(pub["title"], font_weight="bold", font_size="md"),
                    rx.spacer(),
                    rx.text(pub['venue'], color="gray.500", font_size="sm"),
                    rx.text(pub['year'], color="gray.500", font_size="sm", margin_left="0.5em"),
                    width="100%",
                ),
                rx.hstack(
                    rx.cond(
                        pub.get("paper_url"),
                        rx.link(
                            rx.icon("file-text", size=16),
                            href=pub.get("paper_url", "#"),
                            is_external=True,
                            color="blue.500",
                            _hover={"color": "blue.600"},
                        ),
                    ),
                    rx.cond(
                        pub.get("github_url"),
                        rx.link(
                            rx.icon("github", size=16),
                            href=pub.get("github_url", "#"),
                            is_external=True,
                            color="gray.600",
                            _hover={"color": "gray.800"},
                        ),
                    ),
                    spacing="1em",
                    margin_top="0.5em",
                ),
                align_items="flex-start",
                spacing="0.2em",
                width="100%",
                padding="1.5em",
                background="white",
                border_radius="10px",
                z_index="1",
                position="relative",
            ),
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
            "> div > div > p:first-of-type": {
                "color": "transparent",
                "background": "linear-gradient(45deg, rgba(255,105,180,1), rgba(100,149,237,1), rgba(50,205,50,1))",
                "background_clip": "text",
                "animation": "gradient 5s ease infinite",
            },
            "_before": {
                "opacity": "1",
                "animation": "gradient 5s ease infinite",
            },
        },
    )

# def publications():
#     pubs = [
#         {
#             "title": "How Do Developers Structure Unit Test Cases? An Empirical Study from the \"AAA\" Perspective",
#             "authors": "Chenhao Wei, Lu Xiao, Tingting Yu, Sunny Wong, Abigail Clune",
#             "year": "2024",
#             "venue": "arXiv preprint",
#             "paper_url": "https://arxiv.org/abs/2407.08138",
#             "github_url": "https://github.com/Codegass/Unit-Test-Empricial-Study-from-AAA-Perspective",
#         },
#         {
#             "title": "Another Research Paper",
#             "authors": "Alice Johnson, Bob Brown",
#             "venue": "Journal of AI",
#             "year": "2022",
#             "paper_url": "https://example.com/another-paper.pdf",
#         },
#         # Add more publications as needed
#     ]
def publications():
    # 尝试读取 JSON 文件
    json_path = "assets/scripts/lu_xiao_publications.json"
    default_pub = {
        "title": "Default Publication Title",
        "authors": "Default Author",
        "year": "2024",
        "venue": "Default Venue",
        "paper_url": "#",
    }

    try:
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as file:
                pubs = json.load(file)
        else:
            pubs = [default_pub]
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        pubs = [default_pub]

    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Publications", size="2xl", margin_bottom="1.5em"),
            rx.vstack(
                *[publication_item(pub) for pub in pubs],
                width="100%",
                max_width="1200px",  # 增加最大宽度
                margin="0 auto",
                align_items="stretch",
                spacing="1.5em",
            ),
            width="100%",
            padding="2em",
            spacing="2em",
            background="gray.50",
        ),
        footer(),
        custom_css="""
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        """,
    )