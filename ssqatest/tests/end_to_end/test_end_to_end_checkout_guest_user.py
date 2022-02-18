
import pytest
from ssqatest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        # go to home page
        home_p.go_to_home_page()
        # add 1 item to cart

        # go to cart

        # apply free coupon

        # select free shipping

        # click on checkout

        # fill in form

        # click on place order

        # verify order is received

        # verify order is recorded in db(via SQL or via API)