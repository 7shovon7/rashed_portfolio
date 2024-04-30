import reflex as rx
from typing import Optional

from rashed_portfolio.data.constants import ProfileData
from rashed_portfolio.ui.constants.ui_constants import MENU_ITEMS, STARTING_COLOR


def navbar(active_item: Optional[str] = None):
    return rx.container(
        rx.hstack(
            # Logo
            rx.center(
                rx.text(
                    ProfileData.NICK_NAME.upper(),
                    color='white',
                    font_size='2.5rem',
                    font_weight='bold',
                ),
                height='4.5em'
            ),
            rx.spacer(),
            menu_items(active_item),
            rx.center(
                rx.icon_button(
                    rx.icon(
                        'menu',
                        color='white',
                    ),
                    display=['flex', 'flex', 'flex', 'none', 'none'],
                    background='transparent',
                    size='4',
                ),
                height='4.5rem',
            )
        ),
        height='4.5em',
        padding_top='20px',
    )


def menu_items(active_item):
    def apply_color(item: str):
        if (active_item and active_item.lower() == item.lower()):
            return 'white'
        else:
            return 'lightgray'
        
    items = []
    for item in MENU_ITEMS:
        items.append(rx.text(
            item,
            font_size='1.25em',
            padding_left='10px',
            color=apply_color(item),
        ))

    return rx.center(
        rx.hstack(
            *items,
            display=["none", "none", "none", "flex", "flex"],
        ),
        height='4.5em',
    )