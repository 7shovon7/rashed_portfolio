import reflex as rx

from rashed_portfolio.data.constants import ProfileData


def home_banner() -> rx.Component:
    return rx.container(
        rx.container(
            rx.image(
                src='/images/hero_image.png',
                border_radius='15px',
                margin='auto',
                width=['90%', '90%', '50%', '50%', '50%'],
                height=['auto', 'auto', 'auto', 'auto', 'auto'],
                float=['none', 'none', 'left', 'left', 'left'],
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
                        padding_top='20px',
                        padding_bottom='20px',
                    ),
                    rx.text('birth and other data'),
                ),
                style={
                    'padding': '25px',
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
