import reflex as rx
from RISE_website.components.navbar import navbar
from RISE_website.components.banner import banner
from RISE_website.components.opening_positions import opening_positions
from RISE_website.components.recent_news import recent_news
from RISE_website.components.lab_into import lab_introduction
from RISE_website.components.footnote import footer

def index():
    # 示例数据，实际使用时应从数据库或配置文件中获取
    positions = {
        "description": "We are currently looking for students to join our research team.",
        "link_text": "Learn More",
        "link_url": "/join-us"  # 或者任何适合的URL
    }
    
    news_items = [
        {"date": "2023-05-01", "content": "Our paper on AI-driven testing was accepted at ICSE 2023."},
        {"date": "2023-04-15", "content": "Dr. Lu Xiao received the NSF CAREER Award."},
    ]
    
    professor = {
        "name": "Dr. Lu Xiao",
        "title": "Associate Professor",
        "image": "/images/people/lxiao6.webp",
        "bio": "Dr. Lu Xiao is an Associate Professor specializing in software engineering...",
    }
    
    projects = [
        {"title": "AI-Driven Software Testing", "description": "This project aims to..."},
        {"title": "Automated Code Review", "description": "We are developing tools for..."},
        {"title": "Software Architecture Analysis", "description": "Our research focuses on..."},
    ]

    return rx.box(
        navbar(),
        banner(),
        lab_introduction(professor),
        recent_news(news_items),
        opening_positions(positions),
        footer()
    )

# __all__ = ["index"]