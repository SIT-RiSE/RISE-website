import reflex as rx
from RISE_website.components.navbar import navbar

def person_card(name, title, image):
    return rx.box(
        rx.vstack(
            rx.image(src=image, alt=name, width="150px", height="150px", border_radius="50%"),
            rx.heading(name, size="md"),
            rx.text(title),
            align="center",
            spacing="3",
        ),
        padding="1em",
        border="1px solid #eaeaea",
        border_radius="10px",
        transition="all 0.3s ease-in-out",
        _hover={
            "border_color": "blue.500",
            "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
            "transform": "translateY(-5px)",
        },
    )

def section(title, people_list):
    return rx.vstack(
        rx.heading(title, size="xl", margin_bottom="1em"),
        rx.grid(
            *[person_card(p["name"], p["title"], p["image"]) for p in people_list],
            columns=rx.breakpoints(sm="1", md="2", lg="3", xl="4"),
            spacing="4",
        ),
        align_items="stretch",
        margin_bottom="2em",
    )

professors = [
    {"name": "Dr. Jane Smith", "title": "Professor of Software Engineering", "image": "/images/jane_smith.jpg"},
    {"name": "Dr. John Doe", "title": "Associate Professor of AI", "image": "/images/john_doe.jpg"},
    # Add more professors as needed
]

students = [
    {"name": "Alice Johnson", "title": "PhD Student", "image": "/images/alice_johnson.jpg"},
    {"name": "Bob Williams", "title": "Master's Student", "image": "/images/bob_williams.jpg"},
    {"name": "Charlie Brown", "title": "Undergraduate Researcher", "image": "/images/charlie_brown.jpg"},
    # Add more students as needed
]

def people():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Our Team", size="2xl", margin_bottom="1em"),
                section("Professors", professors),
                section("Students", students),
                max_width="1200px",
                width="100%",
                margin="0 auto",
                padding="2em",
                spacing="2em",
            ),
            margin_top="5em",  # 添加顶部边距以避免内容被 navbar 遮挡
        )
    )