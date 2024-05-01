import reflex as rx

from rashed_portfolio.data.constants import ProfileData


def home_about():
    description_section = [rx.text(d, color='gray', text_align='justify', padding_bottom='10px') for d in ProfileData.LONG_DESCRIPTION.split('\n')]
    return rx.container(
        rx.heading(
            'About Myself'.upper(),
            font_size='3rem',
            align='center',
            margin_top='50px',
            margin_bottom='50px',
        ),
        *description_section,
    )