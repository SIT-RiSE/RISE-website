import reflex as rx
from RISE_website.components.navbar import navbar

def person_card(name, title, image_src, description):
    return rx.box(
        rx.vstack(
            rx.image(src=image_src, alt=name, height="200px", width="200px", border_radius="50%"),
            rx.heading(name, size="lg"),
            rx.text(title, font_style="italic"),
            rx.text(description),
            align="center",
            padding="1em",
            border="1px solid #eaeaea",
            border_radius="10px",
        )
    )

def people():
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Our Team", size="2xl", margin_bottom="1em"),
            rx.grid(
                person_card(
                    "Dr. Jane Smith",
                    "Principal Investigator",
                    "/assets/images/jane_smith.jpg",
                    "Expert in software architecture and design patterns."
                ),
                person_card(
                    "Dr. John Doe",
                    "Senior Researcher",
                    "/assets/images/john_doe.jpg",
                    "Specializes in AI applications in software engineering."
                ),
                person_card(
                    "Alice Johnson",
                    "PhD Student",
                    "/assets/images/alice_johnson.jpg",
                    "Researching agile methodologies and team dynamics."
                ),
                columns="1 2 3",  # 修改这里
                spacing="2em",
            ),
            max_width="1000px",
            margin="0 auto",
            padding="2em",
            spacing="2em",
        )
    )

# __all__ = ["people"]