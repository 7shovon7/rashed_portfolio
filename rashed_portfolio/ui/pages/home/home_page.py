import reflex as rx

from rashed_portfolio.data.constants import ProfileData
from rashed_portfolio.ui.global_components.nav_bar import navbar
from rashed_portfolio.ui.pages.home.components.about import home_about
from rashed_portfolio.ui.pages.home.components.banner import home_banner
from rashed_portfolio.ui.pages.home.components.exp_and_edu import experience_and_education


# @rx.page(route='/', title=ProfileData.PREFERRED_FULL_NAME)
def index() -> rx.Component:
    style = {
        'position': 'absolute',
        'height': '500px',
        'width': '100%',
        'background': "linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(131,145,255,1) 0%, rgba(100,185,252,1) 100%)",
        'z-index': '-1',
    }
    return rx.fragment(
        rx.container(
            style=style,
        ),
        navbar(active_item='Home'),
        home_banner(),
        home_about(),
        experience_and_education(),
    )

