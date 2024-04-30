import reflex as rx

from rashed_portfolio.ui.utils.utils import get_css_display


def hero_content():
    details_msg = 'You will begin to realise why this exercise is called the Dickens Pattern with reference to the ghost showing Scrooge some different futures.'
    vstack = rx.vstack(
        rx.text(
            'This is me'.upper(),
        ),
        rx.text(
            'Rashedul Islam'.upper(),
            font_size='3rem',
            font_weight='bold',
            align='center',
        ),
        rx.text(
            details_msg,
            color='grey',
        ),
        rx.button(
            rx.text('Discover Now'.upper(), font_weight='bold'),
            padding='20px 40px 20px 40px',
            background="linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(131,145,255,1) 0%, rgba(100,185,252,1) 100%)",
        ),
        # hero_image(large=False),
        align_items=['center', 'center', 'center', 'baseline', 'baseline'],
        width=['100%', '100%', '100%', '50%', '50%'],
        padding=['30px', '30px', '30px', '0', '0'],
        margin_top=['0', '0', '0', '120px', '120px'],
        spacing='4',
        float='left',
    )
    return vstack


def hero_image(large: bool):
    return rx.container(
        rx.image(
            src='/images/hero_image.png',
            height=['auto', 'auto', 'auto', '100%', '100%'],
            width=['100%', '100%', '100%', 'auto', 'auto'],
            # display=get_css_display(large),
        ),
        # align='center',
        # justify='center',
        width=['100%', '100%', '100%', '50%', '50%'],
    )
    # return rx.center(
    #     rx.vstack(
    #         rx.container(
    #             background='linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 0%, rgba(0,212,255,1) 100%)',
    #             height=['50%', '50%', '50%', '70%', '70%'],
    #             width='auto',
    #             aspect_ratio='4/5',
    #             transform='translate(-10%, 10%)',
    #             position='absolute',
    #         ),
    #         rx.container(
    #             background='#f9f9ff',
    #             height=['44%', '44%', '44%', '62%', '62%'],
    #             width='auto',
    #             aspect_ratio='4/5.1',
    #             transform='translate(-3%, 18%)',
    #             position='absolute',
    #         ),
    #         rx.image(
    #             src='/images/rashed_grad_hero.png',
    #             height=['auto', 'auto', 'auto', '100%', '100%'],
    #             width=['80%', '80%', '80%', 'auto', 'auto'],
    #             position='relative',
    #         ),
    #         margin_left='40px',
    #         display=get_css_display(large),
    #     ),
    #     width=['100%', '100%', '100%', '50%', '50%'],
    # )


def home_banner() -> rx.Component:
    return rx.container(
        hero_content(),
        hero_image(large=True),
        # align=['center', 'center', 'center', 'baseline', 'baseline'],
        background_color='#f9f9ff',
        padding_top='60px',
    )
