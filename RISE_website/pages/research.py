import reflex as rx
from RISE_website.components.navbar import navbar

def research_area(title, description):
    return rx.box(
        rx.box(
            rx.heading(title, size="lg"),
            rx.text(description),
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

def research():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Our Research", size="2xl", margin_bottom="1em"),
                research_area(
                    "Software Engineering Processes",
                    "We investigate agile methodologies, DevOps practices, and continuous integration/continuous deployment (CI/CD) pipelines to improve software development efficiency and quality."
                ),
                research_area(
                    "Software Architecture and Design",
                    "Our team explores microservices architecture, cloud-native application design, and software design patterns to create scalable and maintainable systems."
                ),
                research_area(
                    "AI in Software Engineering",
                    "We research the application of machine learning and artificial intelligence techniques in code generation, bug prediction, and automated testing to enhance developer productivity."
                ),
                max_width="800px",
                width="100%",
                margin="0 auto",
                padding="2em",
                spacing="1em",
            ),
            margin_top="5em",  # 添加顶部边距以避免内容被 navbar 遮挡
        ),
        # 添加关键帧动画
        custom_css="""
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        """
    )