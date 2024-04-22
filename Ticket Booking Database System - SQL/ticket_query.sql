/* 1. There are two types of tickets: Adult tickets for those who are over
16 years old and Child tickets for those aged 5 to 15 years old,
available for the Exeter Food Festival 2023. List all relevant
information about this festival, including the venue, the starting and
end time, the total number of each type of tickets. */

SELECT 
	e.Name, -- Name of the event.
	e.Date, -- Date of the event.
    e.StartingTime, -- Time the event starts.
    e.EndingTime,  -- Time the event ends.
    e.Location AS Venue, -- Venue of the event.
    SUM(CASE WHEN tt.Type = 'Adult' THEN tt.NumberOfTicketsAvailable ELSE 0 END) AS TotalAdultTickets, -- Total number of 'Adult' type of tickets available.
    SUM(CASE WHEN tt.Type = 'Child' THEN tt.NumberOfTicketsAvailable ELSE 0 END) AS TotalChildTickets -- Total number of 'Child' type of tickets available.
FROM 
    Event e -- Event entity.
JOIN 
    TicketType tt ON e.EventID = tt.EventID -- Join Event and TicketType entities where EventID matches.
WHERE 
    e.Name = 'Exeter Food Festival 2023' -- Filters only 'Exeter Food Festival 2023'.
GROUP BY 
    e.EventID; -- Group the results by EventID.
    
    
/* 2. Find all the events in Exeter starting from 1 July, 2023 to 10 July,
2023. List the event title, starting time and end time, and
description.*/
SELECT 
	e.name, -- Name of the event.
	e.Date, -- Date of the event.
	e.StartingTime, -- Time the event starts.
	e.EndingTime, -- Time the event ends.
	e.Description -- Description of the event.
FROM 
	Event e -- Event entity.
WHERE 
	e.Date BETWEEN '2023-07-01' AND '2023-07-10'; -- Filter the dates.

/* 3. There are three types of tickets (Gold, Silver, Bronze) for the
Exmouth Music Festival 2023. List available ticket amount for the
Bronze ticket type, together with its price. */
SELECT 
    tt.NumberOfTicketsAvailable AS AvailableTickets, -- Available Tickets for each type.
    tt.Price -- Price for each type of ticket.
FROM 
    TicketType tt -- TicketType Entity.
JOIN 
    Event e ON tt.EventID = e.EventID -- Join TicketType and Event entities where EventID matches.
WHERE 
    e.Name = 'Exmouth Music Festival 2023' AND  -- Filters only 'Exmouth Music Festival 2023' event.
    tt.Type = 'Bronze'; -- Filters only 'Bronze' ticket type
    


/* 4. List all the customer’s names who have booked Gold tickets for the
Exmouth Music Festival 2023, together with the number of Gold
tickets booked for each customer.*/
SELECT 
	c.Name AS CustomerName, -- Name of the customer.
	COUNT(tbd.TicketTypeID) AS NumberOfGoldTickets -- Count number of 'Gold' type of tickets.
FROM 
	Customer c -- Customer Entity.
INNER JOIN 
	Booking b ON c.CustomerID = b.CustomerID -- Joins Customer and Booking entities where CustomerID matches.
INNER JOIN 
	TicketBookingDetails tbd ON B.BookingID = tbd.BookingID -- Joins TicketBookingDetails and Booking entities where BookingID matches.
INNER JOIN 
	TicketType tt ON tbd.TicketTypeID = tt.TicketTypeID -- Joins TicketBookingDetails and TicketType entities where TicketTypeID matches.
INNER JOIN 
	Event e ON b.EventID = e.EventID -- Joins Booking and Event entities where EventID matches.
WHERE 
	e.Name = 'Exmouth Music Festival 2023' AND tt.Type = 'Gold' -- Filters only 'Exmouth Music Festival 2023' event and 'Gold' type of tickets.
GROUP BY 
	c.Name -- Groups by Customer's names.
ORDER BY 
	NumberOfGoldTickets DESC; -- Orders by number of 'Gold' type of tickets in descending order.

/* 5. List all event names and the number of tickets that have been sold
for each event so far, ordered by the number of sold tickets in
descending order.*/
SELECT 
	e.Name AS EventName, -- Name of the event.
	SUM(TBD.Quantity) AS TicketsSold -- Sum of the sold tickets.
FROM 
	Event e -- Event entity.
LEFT JOIN 
	Booking b ON e.EventID = b.EventID -- Join Event and Booking entities where EventID matches.
LEFT JOIN 
	TicketBookingDetails tbd ON b.BookingID = tbd.BookingID -- Join Booking and TicketBookingDetails entities where BookingID matches.
GROUP BY 
	e.Name -- Group by name of the event.
ORDER BY 
	TicketsSold DESC; -- Order by number of sold tickets in descending order.

/* 6. List all the relevant information by offering a booking ID, such as
the customer’s name, booking time, event title, delivery options,
ticket types and the number of tickets for each type, the total
payment and so on.*/
SELECT
    b.BookingID, -- ID of the Booking.
    c.Name AS CustomerName, -- Name of the customer.
    e.Name AS EventTitle, -- Name of the event.
    b.DeliveryMethod, -- Method of delievery of the tickets.
    tt.Type AS TicketType, -- Type of the tickets.
    tbd.Quantity AS NumberOfTickets, -- Number of Tickets.
    tt.Price AS TicketPrice, -- Price of the tickets.
    b.TotalAmount AS TotalPayment, -- Total amount of money paid.
    b.PaymentStatus -- Status of the payment.
FROM 
	Booking b -- Booking Entity.
INNER JOIN 
	Customer c ON b.CustomerID = c.CustomerID -- Join Booking and Customer entities where CustomerID matches.
INNER JOIN 
	Event e ON b.EventID = e.EventID -- Join Booking and Event entities where EventID matches.
INNER JOIN 
	TicketBookingDetails tbd ON b.BookingID = tbd.BookingID -- Join Booking and TicketBookingDetails entities where BookingID matches.
INNER JOIN 
	TicketType tt ON tbd.TicketTypeID = tt.TicketTypeID -- Join TicketBookingDetails and TicketType entitites where TicketTypeID matches.
ORDER BY 
	b.BookingID; -- Order by BookingID in ascending order.

/* 7. Find which event has the maximum income so far. List its event title
and its total income.*/
SELECT
    e.Name AS EventTitle, -- Name of the event.
    SUM(b.TotalAmount) AS TotalIncome -- Sum of total amount of money paid.
FROM 
	Event e -- Event entity.
INNER JOIN 
	Booking b ON e.EventID = b.EventID -- Join Event and Booking Entity where EventID matches.
GROUP BY 
	e.Name -- Group by name of the event.
ORDER BY 
	TotalIncome DESC -- Order by total amount of money paid in descending order.
LIMIT 1; -- Limit to only one event. 




    
    
