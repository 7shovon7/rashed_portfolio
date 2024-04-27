import reflex as rx

from rashed_portfolio.ui.utils.utils import get_css_display


def hero_content(large):
    if large:
        width = '50%'
        text_align = 'start'
    else:
        width = '100%'
        text_align = 'center'
    details_msg = 'You will begin to realise why this exercise is called the Dickens Pattern with reference to the ghost showing Scrooge some different futures.'
    vstack = rx.vstack(
        rx.text(
            'This is me'.upper(),
        ),
        rx.text(
            'Rashedul Islam'.upper(),
            font_size='3rem',
            font_weight='bold',
        ),
        rx.text(
            details_msg,
            color='grey',
        ),
        rx.button(
            rx.text('Discover Now'.upper(), font_weight='bold'),
            padding='20px 40px 20px 40px',
            background="linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 0%, rgba(0,212,255,1) 100%)",
        ),
        hero_image(large=False),
        display=get_css_display(large=large),
        align=text_align,
        width=width,
        spacing='4',
    )
    if large:
        return vstack
    else:
        return rx.center(
            vstack
        )


def hero_image(large):
    if large:
        width = '50%'
        image_height = '100%'
        image_width = 'auto'
        frame1_height = '70%'
        frame1_width = 'auto'
        frame2_height = '62%'
        frame2_width = 'auto'
    else:
        width = '100'
        image_height = 'auto'
        image_width = '80%'
        frame1_height = '50%'
        frame1_width = 'auto'
        frame2_height = '44%'
        frame2_width = 'auto'
    return rx.center(
        rx.vstack(
            rx.container(
                background='linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 0%, rgba(0,212,255,1) 100%)',
                height=frame1_height,
                width=frame1_width,
                aspect_ratio='4/5',
                transform='translate(-10%, 10%)',
                position='absolute',
            ),
            rx.container(
                background='#f9f9ff',
                height=frame2_height,
                width=frame2_width,
                aspect_ratio='4/5.1',
                transform='translate(-3%, 18%)',
                position='absolute',
            ),
            rx.image(
                src='/images/rashed_grad_hero.png',
                height=image_height,
                width=image_width,
                position='relative',
            ),
            margin_left='40px',
            display=get_css_display(large=large),
        ),
        width=width,
    )


def home_banner() -> rx.Component:
    return rx.container(
        rx.hstack(
            hero_content(large=True),
            hero_content(large=False),
            hero_image(large=True),
            align='center',
        ),
        background_color='#f9f9ff',
    )
