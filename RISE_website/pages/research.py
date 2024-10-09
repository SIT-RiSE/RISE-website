import reflex as rx
from RISE_website.components.navbar import navbar

def research_area(title, description):
    return rx.box(
        rx.heading(title, size="lg"),
        rx.text(description),
        padding="1em",
        border="1px solid #eaeaea",
        border_radius="10px",
        margin_bottom="1em",
        transition="all 0.3s ease-in-out",
        _hover={
            "border_color": "blue.500",
            "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
            "transform": "translateY(-5px)",
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
        )
    )