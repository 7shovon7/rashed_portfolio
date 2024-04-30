import reflex as rx
from typing import Optional

from rashed_portfolio.data.constants import ProfileData
from rashed_portfolio.ui.constants.ui_constants import MENU_ITEMS, STARTING_COLOR, ENDING_COLOR


def navbar(active_item: Optional[str] = None):
    def apply_color(item: str):
        if (active_item and active_item.lower() == item.lower()):
            return STARTING_COLOR
        else:
            return 'black'
        
    return rx.container(
        rx.hstack(
            # Logo
            rx.center(
                rx.text(
                    ProfileData.NICK_NAME.upper(),
                    # class_name="text-4xl text-black-900 font-bold",
                    color=STARTING_COLOR,
                    font_size='2.5rem',
                    font_weight='bold',
                ),
                height='4.5em'
            ),
            rx.spacer(),
            rx.center(
                rx.hstack(
                    *[rx.text(item, font_size="1.25em", padding_left="10px", color=apply_color(item), display=["none", "none", "none", "flex", "flex"],) for item in MENU_ITEMS],
                ),
                height='4.5em',
            ),
            rx.center(
                rx.icon_button(
                    rx.icon(
                        'menu',
                        color=STARTING_COLOR,
                    ),
                    display=['flex', 'flex', 'flex', 'none', 'none'],
                    background='transparent',
                    size='4',
                ),
                height='4.5rem',
            )
        ),
        height='4.5em',
    )