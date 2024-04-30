import reflex as rx

from rashed_portfolio.data.constants import ProfileData
from rashed_portfolio.ui.global_components.nav_bar import navbar
from rashed_portfolio.ui.pages.home.components.banner import home_banner


@rx.page(route='/', title=ProfileData.PREFERRED_FULL_NAME)
def index() -> rx.Component:
    return rx.fragment(
        navbar(active_item='Home'),
        home_banner(),
    )
