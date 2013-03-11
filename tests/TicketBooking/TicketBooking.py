
class TicketBooking :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("Travles Ticket Booking Sample Test")
        main.step("Searching Bus")
        search_result = main.BitlaSoftReservationPage.search_bus()
        utilities.assert_equals(expect=main.TRUE,actual=search_result,onpass="Search Bus success",onfail="Failed to search Bus")
    
        main.step("Selecting Bus for next day")
        select_bus_result = main.BitlaSoftReservationPage.select_bus()
        utilities.assert_equals(expect=main.TRUE,actual=select_bus_result,onpass="Selected Bus successfully",onfail="Failed to select Bus")
    
        main.step("Selecting Seat")
        select_seat_result = main.BitlaSoftReservationPage.select_seat()
        utilities.assert_equals(expect=main.TRUE,actual=select_seat_result,onpass="Selected seat successfully",onfail="Failed to select seat ")
    
        main.step("Filling the details ")
        fill_details_result = main.BitlaSoftReservationPage.fill_details(title=main.params['CASE1']['STEP4']['title'], passenger_name=main.params['CASE1']['STEP4']['passenger_name'], passenger_age=main.params['CASE1']['STEP4']['passenger_age'], drop_off=main.params['CASE1']['STEP4']['drop_off'], email=main.params['CASE1']['STEP4']['email'], phone_number=main.params['CASE1']['STEP4']['phone_number'], id_card_number=main.params['CASE1']['STEP4']['id_card_number'], id_card_issued=main.params['CASE1']['STEP4']['id_card_issued'], address=main.params['CASE1']['STEP4']['address'])
        utilities.assert_equals(expect=main.TRUE,actual=fill_details_result,onpass="Filled details successfully",onfail="Failed to fill the details ")
    
        deselect_result = main.BitlaSoftReservationPage.deselect_seat()
        utilities.assert_equals(expect=main.TRUE,actual=deselect_result,onpass="Deselected the seat",onfail="Failed to deselect seat")
    
        main.log.info("Ticket Booked Successfully")