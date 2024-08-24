class TicketOffice:
    def __init__(self, ticket_seller):
        self.ticket_seller = ticket_seller

    def buy_ticket(self, audience):
        if self.ticket_seller.get_ticket(audience):
            audience.set_ticket(self.ticket_seller.get_ticket(audience))
            return True
        return False
