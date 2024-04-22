/* 1. Increase the amount of Adult tickets for the Exeter Food Festival
by 100.  */
UPDATE 
	TicketType -- Ticket Type Entity.
SET 
	NumberOfTicketsAvailable = NumberOfTicketsAvailable + 100 -- Increase Number of Available Tickets by 100.
WHERE 
	EventID = (SELECT EventID FROM Event WHERE Name = 'Exeter Food Festival 2023') AND Type = 'Adult'; -- Filter only 'Exeter Food Festival 2023' event and 'Adult' type of tickets.

/* 2. Ian Cooper would like to book 2 adults and 1 child tickets for the
Exeter Food Festival today, using voucher code ‘FOOD10’ to get
10% off discount. He used his credit card to pay for it, and has
chosen the tickets sent by email. */
INSERT INTO Booking (BookingID, CustomerID, EventID, BookingTime, TotalAmount, PaymentStatus, DeliveryMethod, UniqueReferenceCode) -- Booking Entity
VALUES (17, 1, 1, CURTIME(), (20*2 + 10)*0.9, 'Paid', 'Email', 'REF112'); -- Booking Values.

INSERT INTO TicketBookingDetails (DetailID, BookingID, TicketTypeID, Quantity)  -- TicketBookingDetails Entity.
VALUES (23, 17, 1, 2),  -- 2 Adult tickets for EventID 1
       (24, 17, 2, 1);  -- 1 Child ticket for EventID 1

INSERT INTO Payment (PaymentID, BookingID, Amount, CardType, CardNumber, SecurityCode, ExpiryDate) -- Payment Entity.
VALUES (17, 17, (20*2 + 10)*0.9, 'MasterCard', '2222333344445555', '456', '2026-05-01'); -- Payment Values.

/* 3. Joe Smiths had a booking for one event which has not taken place.
Today he would like to cancel this booking by offering the booking
ID. */
UPDATE 
	Booking -- Booking entity.
SET 
	PaymentStatus = 'Cancelled' -- Set status to 'Cancelled'
WHERE 
	BookingID = 5; -- Filter where BookingId = 5.

INSERT INTO Voucher (VoucherID, EventID, Code, DiscountAmount) -- Voucher Entity.
VALUES (7, 2, 'SUMMER20', 20.00); -- Voucher Values.




