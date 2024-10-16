link_style = {
    "color": "black",
    "text_decoration": "none",
    "transition": "all 0.3s ease-in-out",
    "position": "relative",
    "z_index": "1",
    "_before": {
        "content": "''",
        "position": "absolute",
        "top": "0",
        "left": "0",
        "right": "0",
        "bottom": "0",
        "background": "linear-gradient(45deg, rgba(255,105,180,0.8), rgba(100,149,237,0.8), rgba(50,205,50,0.8))",
        "background_size": "300% 300%",
        "opacity": "0",
        "transition": "opacity 0.3s ease-in-out",
        "z_index": "-1",
    },
    "_hover": {
        "color": "white",
        "text_decoration": "none",
        "_before": {
            "opacity": "1",
            "animation": "gradient 5s ease infinite",
        },
    }
}