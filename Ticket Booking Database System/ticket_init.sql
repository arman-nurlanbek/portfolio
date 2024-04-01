CREATE DATABASE TicketBookingSystem;

USE TicketBookingSystem;

CREATE TABLE Customer (
CustomerID INT PRIMARY KEY,
Name VARCHAR(255),
EmailAddress VARCHAR(255),
PhoneNumber VARCHAR(255)
);

CREATE TABLE Event (
EventID INT PRIMARY KEY,
Description VARCHAR(255),
Name VARCHAR(255),
Date DATE,
StartingTime TIME,
EndingTime TIME,
Location VARCHAR(255),
TotalTickets INT
);

CREATE TABLE TicketType (
TicketTypeID INT PRIMARY KEY,
EventID INT,
Type VARCHAR(255),
Price DECIMAL(10,2),
NumberOfTicketsAvailable INT,
FOREIGN KEY (EventID) REFERENCES Event(EventID)
);

CREATE TABLE Booking (
BookingID INT PRIMARY KEY,
CustomerID INT,
EventID INT,
BookingTime TIME,
TotalAmount INT,
PaymentStatus VARCHAR(255),
DeliveryMethod VARCHAR(255),
UniqueReferenceCode VARCHAR(255),
FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
FOREIGN KEY (EventID) REFERENCES Event(EventID)
);

CREATE TABLE TicketBookingDetails (
DetailID INT PRIMARY KEY,
BookingID INT,
TicketTypeID INT,
Quantity INT,
FOREIGN KEY (BookingID) REFERENCES Booking(BookingID),
FOREIGN KEY (TicketTypeID) REFERENCES TicketType(TicketTypeID)
);

CREATE TABLE Voucher(
VoucherID INT PRIMARY KEY,
EventID INT,
Code VARCHAR(255),
DiscountAmount INT,
FOREIGN KEY (EventID) REFERENCES Event(EventID)
);

CREATE TABLE Payment(
PaymentID INT PRIMARY KEY,
BookingID INT,
Amount INT,
CardType VARCHAR(255),
CardNumber VARCHAR(255),
SecurityCode INT,
ExpiryDate DATE,
FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)
);

INSERT INTO Customer (CustomerID, Name, EmailAddress, PhoneNumber) VALUES
(1, 'Ian Cooper', 'ian.cooper@gmail.com', '555-543-4567'),
(2, 'Bruce Wayne', 'bruce.wayne@hotmail.com', '555-434-5678'),
(3, 'Clark Kent', 'clark.kent@superhero.com', '555-345-6789'),
(4, 'Diana Prince', 'diana.prince@avengers.com', '555-456-7890'),
(5, 'Joe Smiths', 'joe.smithsmail.com', '555-567-8901'),
(6, 'Steve Rogers', 'steve.rogers@gmail.com', '555-678-9012'),
(7, 'Natasha Romanoff', 'natasha.romanoff@avengers.com', '555-789-0123'),
(8, 'Barry Allen', 'barry.allen@hotmail.com', '555-890-1234'),
(9, 'Carol Danvers', 'carol.danvers@outlook.com', '555-901-2345'),
(10, 'Arthur Curry', 'arthur.curry@microsoft.com', '555-012-3456');

INSERT INTO Event (EventID, Description, Name, Date, StartingTime, EndingTime, Location, TotalTickets) VALUES
(1, 'A culinary extravaganza featuring local and international cuisine, live cooking demos, and food tastings.', 'Exeter Food Festival 2023', '2023-07-03', '10:00:00', '20:00:00', 'Exeter', 500),
(2, 'A vibrant celebration of music with performances from renowned artists across diverse genres, set in a picturesque location.', 'Exmouth Music Festival 2023', '2023-07-05', '20:00:00', '22:00:00', 'Exmouth', 1000),
(3, 'A gathering of book lovers, featuring author talks, book signings, and a showcase of literary works from various genres.', 'Devon Literary Expo 2023', '2023-08-15', '10:00:00', '20:00:00', 'Devon', 300),
(4, 'An enchanting weekend filled with soulful jazz and rhythmical blues performances by acclaimed musicians.', 'Plymouth Jazz & Blues Weekend', '2023-09-20', '12:00:00', '15:00:00', 'Plymouth', 600),
(5, 'An artistic haven displaying contemporary art and design pieces, with workshops, interactive sessions, and live art demonstrations.', 'Cornwall Art & Design Fair', '2023-06-11', '10:00:00', '22:00:00', 'Cornwall', 450),
(6, 'An exhilarating coastal marathon offering breathtaking views, challenging courses, and a memorable running experience.', 'Dorset Coastal Marathon', '2023-10-05', '08:00:00', '16:00:00', 'Dorset', 2000),
(7, 'A premier summit for tech enthusiasts and professionals, featuring the latest in technology, innovation, and digital trends.', 'Bristol Tech Summit', '2023-11-17', '10:00:00', '13:00:00', 'Bristol', 1200),
(8, 'A delightful festival celebrating the art of winemaking, with wine tastings, vineyard tours, and expert-led sessions.', 'Somerset Wine Tasting Festival', '2023-05-22', '11:00:00', '21:00:00', 'Somerset', 350),
(9, 'An adventurous expo offering outdoor activities, gear exhibitions, and expert talks on outdoor survival and adventure sports.', 'Dartmoor Outdoor Adventure Expo', '2023-04-18', '10:00:00', '21:00:00', 'Dartmoor', 800),
(10, 'A serene musical event featuring classical music performances by renowned orchestras and soloists in a historic setting.', 'Bath Classical Music Festival', '2023-12-01', '10:00:00', '20:00:00', 'Bath', 500);

INSERT INTO TicketType (TicketTypeID, EventID, Type, Price, NumberOfTicketsAvailable) VALUES
(1, 1, 'Adult', 20.00, 300),
(2, 1, 'Child', 10.00, 200),
(3, 2, 'Gold', 50.00, 100),
(4, 2, 'Silver', 40.00, 150),
(5, 2, 'Bronze', 30.00, 200),
(6, 3, 'Adult', 20.00, 100),
(7, 4, 'Adult', 30.00, 100),
(8, 5, 'Adult', 30.00, 100 ),
(9, 5, 'Child', 15.00, 100),
(10, 6, 'Adult', 30.00, 100),
(11, 7, 'Gold', 50.00, 100),
(12, 7, 'Silver', 40.00, 100),
(13, 7, 'Bronze', 30.00, 100),
(14, 8, 'Adult', 20.00, 400),
(15, 9, 'Adult', 10.00, 300),
(16, 10, 'Adult', 50.00, 200);

INSERT INTO Booking (BookingID, CustomerID, EventID, BookingTime, TotalAmount, PaymentStatus, DeliveryMethod, UniqueReferenceCode) VALUES
(1, 1, 1, '10:00:03', 30.00, 'Paid', 'Email', 'REF100'), 
(2, 2, 1, '11:00:13', 40.00, 'Pending', 'Pickup', 'REF101'), 
(3, 3, 2, '9:00:43', 170.00, 'Paid', 'Email', 'REF102'), 
(4, 4, 2, '4:30:24', 100.00, 'Cancelled', 'Email', 'REF103'),
(5, 5, 2, '10:10:14', 40.00, 'Paid', 'Email', 'REF104'), 
(6, 6, 3, '11:50:52', 60.00, 'Pending', 'Pickup', 'REF105'), 
(7, 7, 4, '18:10:42',  90.00, 'Paid', 'Email', 'REF106'), 
(8, 8, 5, '16:02:24', 45.00, 'Cancelled', 'Email', 'REF107'), 
(9, 9, 6, '05:10:51', 120.00, 'Paid', 'Email', 'REF108'), 
(10, 9, 7, '03:10:45', 170.00, 'Pending', 'Pickup', 'REF109'), 
(11, 8, 8, '05:30:35', 80.00, 'Paid', 'Email', 'REF110'),
(12, 10, 9, '19:20:52', 100.00, 'Paid', 'Email', 'REF111'), 
(13, 10, 10, '15:40:41', 100.00, 'Cancelled', 'Email', 'REF111'), 
(14, 10, 10, '20:10:25', 50.00, 'Paid', 'Email', 'REF111'), 
(15, 10, 10, '08:08:37', 200.00, 'Pending', 'Email', 'REF111'),
(16, 10, 10, '10:10:49', 300.00, 'Cancelled', 'Email', 'REF111');

INSERT INTO Payment (PaymentID, BookingID, Amount, CardType, CardNumber, SecurityCode, ExpiryDate) VALUES
(1, 1, 30, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(2, 2, 40.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(3, 3, 170.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(4, 4, 100.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(5, 5, 40.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(6, 6, 60.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(7, 7, 90.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(8, 8, 45.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(9, 9, 120.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(10, 10, 170.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(11, 11, 80.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(12, 12, 100.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(13, 13, 100.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(14, 14, 50.00, 'American Express', '6666777788889999', '789', '2027-07-01'),
(15, 15, 200.00, 'MasterCard', '2222333344445555', '456', '2026-05-01'),
(16, 16, 300.00, 'American Express', '6666777788889999', '789', '2027-07-01');

INSERT INTO Voucher (VoucherID, EventID, Code, DiscountAmount) VALUES
(1, 1, 'FESTIVAL20', 20.00),
(2, 2, 'FOOD10', 10.00),
(3, 4, 'DIS20', 20.00),
(4, 7, 'COUNT5', 5.00),
(5, 8, 'DISCOUNT10', 10.00),
(6, 10, 'FEST20', 20.00);

INSERT INTO TicketBookingDetails (DetailID, BookingID, TicketTypeID, Quantity) VALUES
(1, 1, 1, 1), 
(2, 1, 2, 1), 
(3, 2, 1, 2), 
(4, 3, 3, 2), 
(5, 3, 4, 1), 
(6, 3, 5, 1),  
(7, 4, 3, 2),  
(8, 5, 4, 1), 
(9, 6, 6, 3), 
(10, 7, 7, 3),
(11, 8, 8, 1), 
(12, 8, 9, 1), 
(13, 9, 9, 4), 
(14, 10, 10, 2),
(15, 10, 11, 1), 
(16, 10, 12, 1),
(17, 11, 13, 4), 
(18, 12, 16, 10), 
(19, 13, 16, 2), 
(20, 14, 16, 1), 
(21, 15, 16, 4), 
(22, 16, 16, 6); 
