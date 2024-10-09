import reflex as rx
from RISE_website.pages import index, research, people, about

app = rx.App()
app.add_page(index)
app.add_page(research)
app.add_page(people)
app.add_page(about)