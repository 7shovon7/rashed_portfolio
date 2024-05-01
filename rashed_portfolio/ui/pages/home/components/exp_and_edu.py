import reflex as rx


def experience_and_education():
    return rx.container(
        rx.hstack(
            section_button(
                txt='My Experiences',
                is_active=True,
            ),
            section_button(
                txt='My Education',
                is_active=False,
            ),
            justify='center',
        ),
        style={
            'width': '100%',
            'background': "linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(131,145,255,1) 0%, rgba(100,185,252,1) 100%)",
            'padding-top': '60px',
            'padding-bottom': '60px',
        }
    )


def section_button(txt: str, is_active: bool):
    return rx.button(
        txt,
        padding_x='35px',
        padding_y='25px',
        background='white' if is_active else "linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(131,145,255,1) 0%, rgba(100,185,252,1) 100%)",
        color='black' if is_active else 'white',
    )