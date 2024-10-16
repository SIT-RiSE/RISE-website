import reflex as rx
from RISE_website.components.navbar import navbar
from RISE_website.styles.common import link_style

def person_card(name, title, image, note="", tag="", url="#"):
    card_content = rx.box(
        rx.vstack(
            rx.box(
                rx.image(
                    src=image,
                    alt=name,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_top_radius="10px",
                ),
                position="relative",  # 为标签定位
                width="100%",
            ),
            rx.cond(
                tag != "",
                rx.box(
                    rx.text(
                        tag, 
                        font_size="0.6em",
                        color="rgba(255,255,255,0.8)", 
                        font_weight="bold",
                        text_shadow="0 1px 2px rgba(0,0,0,0.1)",
                    ),
                    position="absolute",
                    top="10px",
                    right="10px",
                    padding="2px 8px",
                    border_radius="full",
                    background="rgba(156, 113, 255,0.5)",
                    backdrop_filter="blur(5px)",
                    box_shadow="0 2px 10px rgba(0,0,0,0.1)",
                    z_index="1",
                    white_space="nowrap",
                    overflow="hidden",
                    _before={
                        "content": "''",
                        "position": "absolute",
                        "top": "0",
                        "left": "0",
                        "right": "0",
                        "bottom": "0",
                        "background": "linear-gradient(135deg, rgba(255,255,255,0.3), rgba(255,255,255,0.1))",
                        "border_radius": "inherit",
                        "z_index": "-1",
                    },
                ),
            ),
            rx.vstack(
                rx.heading(name, size="md"),
                rx.text(title, font_size="sm"),
                rx.spacer(),
                rx.text(
                    note, 
                    font_size="0.85em",
                    color="gray.600",
                    line_height="1.3em",
                    overflow="hidden",
                    text_overflow="ellipsis",
                    display="-webkit-box",
                    webkit_line_clamp="3",
                    webkit_box_orient="vertical",
                    text_align="center",
                ),
                align="center",
                justify="space-between",
                height="100%",
                width="100%",
                padding="1em",
                spacing="0.5em",
            ),
            spacing="0",
            bg="white",
            border_radius="10px",
            overflow="hidden",
            height="100%",
            width="100%",
        ),
        padding="2px",
        border_radius="12px",
        margin_bottom="1em",
        transition="all 0.3s ease-in-out",
        position="relative",
        overflow="hidden",
        height="340px",
        width="100%",
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

    return rx.link(
        card_content,
        href=url,
        is_external=url.startswith("http"),
        style=link_style,
        border_radius="12px",
        display="block",
        _hover={
            "transform": "translateY(-5px)",
            "_before": {
                "opacity": "1",
                "animation": "gradient 2s ease infinite",
            },
        },
    )

def section(title, people_list):
    return rx.vstack(
        rx.heading(title, size="xl", margin_bottom="1em"),
        rx.grid(
            *[person_card(p["name"], p["title"], p["image"], p.get("note", ""), p.get("tag", ""), p.get("url", "#")) for p in people_list],
            columns=rx.breakpoints(sm="2", md="3", lg="4", xl="5"),
            spacing="4",
            width="100%",
        ),
        align_items="stretch",
        margin_bottom="2em",
        width="100%",
    )

professors = [
    {"name": "Lu Xiao", "title": "Associate Professor", "image": "/images/people/lxiao6.webp", "note": "", "tag": "PI", "url": "/people/lxiao"},
    # Add more professors as needed
]

students = [
    {"name": "Chenhao Wei", "title": "PhD Student", "image": "/images/people/cwei7.webp", "note": "Research focus: Unit Testing Architecture", "url": "https://scholar.google.com/citations?user=q6kIw60AAAAJ"},
    {"name": "Gengwu Zhao", "title": "PhD Student", "image": "/images/people/gzhao.jpeg", "note": "Research focus: Unit Test Mocking", "url": "https://scholar.google.com/citations?user=QFl5ZekAAAAJ"},
    {"name": "Hanbin Qin", "title": "PhD Student", "image": "/images/people/hqin.jpeg", "note": "Research focus: Unit Test Mocking", "url": "/people/hqin"},
]

Alumni = [
    {"name": "Yutong Zhao", "title": "PhD Student", "image": "/images/people/yzhao.jpeg", "note": "Current position: Assistant Professor", "tag": "Alumni", "url": "https://scholar.google.com/citations?user=aMcoNgEAAAAJ"},
    {"name": "Xiao Wang", "title": "PhD Student", "image": "/images/people/xwang.jpeg", "note": "Current position: SDE II at Amazon", "tag": "Alumni", "url": "https://scholar.google.com/citations?user=4fcRQJoAAAAJ"},
    # Add more students as needed
]

# master_students = [
#     {"name": "Bob Williams", "title": "Master's Student", "image": "/images/people/bob_williams.jpg", "note": "Research focus: AI in SE"},
#     # Add more students as needed
# ]

# collaborators = [
    # {"name": "Charlie Brown", "title": "Undergraduate Researcher", "image": "/images/people/charlie_brown.jpg", "note": "Research focus: AI in SE"},
    # Add more collaborators as needed
# ]

def people():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Our Team", size="2xl", margin_bottom="1em"),
                section("Professors", professors),
                section("PHD Students", students),
                section("Alumni", Alumni),
                max_width="1200px",
                width="100%",
                margin="0 auto",
                padding="2em",
                spacing="2em",
            ),
            margin_top="5em",
            width="100%",
        ),
        width="100%",
        # 添加关键帧动画
        custom_css="""
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        """
    )