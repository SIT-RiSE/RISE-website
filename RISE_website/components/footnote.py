import reflex as rx
from datetime import datetime

def footer():
    current_year = datetime.now().year

    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    f"Email: lxiao6@stevens.edu",
                    font_size="sm",
                    color="gray.600",
                ),
                rx.text(
                    f"©{current_year} RISE Lab @SIT",
                    font_size="sm",
                    color="gray.600",
                ),
                align_items="flex-start",
            ),
            rx.spacer(),
            rx.hstack(
                rx.image(src="/images/logo/sit.png", alt="Stevens Logo", height="200px"),
                rx.image(src="/images/logo/lab_logo.svg", alt="Lab logo", height="140px"),
                spacing="0em",
            ),
            width="100%",
            justify_content="space-between",
            align_items="center",
            padding="1em",
        ),
        width="100%",
        background="gray.100",
        padding_top="2em",  # 增加顶部内边距
        padding_bottom="2em",  # 增加底部内边距
        margin_top="2em",  # 增加顶部外边距，与主页面分开
    )