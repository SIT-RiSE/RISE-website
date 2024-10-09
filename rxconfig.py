import reflex as rx

config = rx.Config(
    app_name="RISE_website",
    db_url="sqlite:///RISE_website.db",
    env=rx.Env.DEV,
    frontend_packages=[
        "react",
        "react-dom",
    ],
)