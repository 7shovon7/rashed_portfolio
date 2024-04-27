def get_css_display(large: bool):
    if large:
        display=["none", "none", "none", "flex", "flex"]
    else:
        display=['flex', 'flex', 'flex', 'none', 'none']
    return display