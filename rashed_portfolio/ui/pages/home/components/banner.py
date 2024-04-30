import reflex as rx

from rashed_portfolio.data.constants import ProfileData
from rashed_portfolio.ui.constants.ui_constants import STARTING_COLOR


def home_banner() -> rx.Component:
    return rx.container(
        rx.container(
            rx.image(
                src='/images/hero_image.png',
                border_radius='15px',
                margin='auto',
                width=['90%', '90%', '70%', '60%', '60%'],
                height=['auto', 'auto', 'auto', 'auto', 'auto'],
                float=['none', 'none', 'none', 'left', 'left'],
            ),
            rx.container(
                rx.vstack(
                    rx.text(
                        'Hello, I am'.upper(),
                        letter_spacing='3px',
                        font_size='0.8rem',
                    ),
                    rx.text(
                        ProfileData.PREFERRED_FULL_NAME.upper(),
                        font_size='3rem',
                        font_weight='bold',
                    ),
                    rx.text(
                        ProfileData.TITLE.upper(),
                        font_weight='bold',
                    ),
                    rx.text(
                        ProfileData.SHORT_DESCRIPTION,
                        color='gray',
                        margin_top='20px',
                        margin_bottom='20px',
                    ),
                    banner_widget_one(
                        icon='calendar-days',
                        txt=ProfileData.BIRTHDAY,
                    ),
                    banner_widget_one(
                        icon='phone',
                        txt=ProfileData.PHONE,
                        is_phone=True,
                    ),
                    banner_widget_one(
                        icon='mail',
                        txt=ProfileData.EMAIL,
                        is_email=True,
                    ),
                    banner_widget_one(
                        icon='map-pin',
                        txt=ProfileData.CITY + ', ' + ProfileData.COUNTRY,
                    ),
                    rx.hstack(
                        banner_widget_two(
                            icon='facebook',
                            url='https://www.facebook.com/rashedul.imsf/'
                        ),
                        banner_widget_two(
                            icon='linkedin',
                            url='https://www.linkedin.com/in/rashedulimsf/'
                        ),
                        margin_top='20px',
                    )
                ),
                style={
                    'padding': '50px',
                }
            ),
            style={
                'margin-top': '60px',
                'padding': '25px',
                'border-radius': '15px',
                'background': 'white',
                'box-shadow': '5px 5px 5px 5px rgba(0, 0, 0, 0.05)',
            }
        ),
    )


def banner_widget_two(
        icon: str,
        url: str,
):
    return rx.link(
        rx.container(
            rx.icon(icon, color='white'),
            border_radius='6px',
            background=STARTING_COLOR,
            padding='10px',
        ),
        href=url,
    )


def banner_widget_one(
        icon: str,
        txt: str,
        is_email: bool = False,
        is_phone: bool = False
):
    f_txt = rx.text(txt)
    if is_email:
        f_txt = rx.link(
            f_txt,
            href=f'mailto:{txt}',
            color='black',
        )
    elif is_phone:
        f_txt = rx.link(
            f_txt,
            href=f'tel:{txt.replace(' ', '')}',
            color='black',
        )
        
    return rx.hstack(
        rx.icon(icon, color=STARTING_COLOR),
        f_txt,
        padding_top='5px',
        padding_bottom='5px',
    )