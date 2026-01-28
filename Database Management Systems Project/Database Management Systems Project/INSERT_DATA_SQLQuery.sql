USE FlowerShopDB;
GO

/*  INSERT DATA */

/* Customer */
INSERT INTO Customer(first_name,last_name,email)
VALUES 
(N'Fevzi Samed', N'ÜNAL',  N's220205032@ankarabilim.edu.tr'),
(N'Anýl',        N'GÜNGÖR',N's220205003@ankarabilim.edu.tr'),
(N'Hamit',       N'GÜNEÞ', N's220204042@ankarabilim.edu.tr');
GO

/* Customer_Phone */
INSERT INTO Customer_Phone(phone, customer_id)
VALUES 
('05419630640', 1),
('05416531560', 2),
('05511026576', 3);
GO

/* Address */
INSERT INTO Address(city,district,street,customer_id)
VALUES
(N'Ankara', N'Keçiören', N'Kuþcaðýz mah',   1),
(N'Ankara', N'Keçiören', N'Atapark mah',    2),
(N'Ankara', N'Çankaya',  N'Demirtepe mah',  3);
GO

/* Category */
INSERT INTO Category(category_name)
VALUES
(N'Gül'),
(N'Papatya'),
(N'Kýr Çiçeði'),
(N'Lilyum');
GO

/* Flower */
INSERT INTO Flower(flower_name, description, unit_price, category_id)
VALUES
(N'Kýrmýzý Gül',     N'Taze kýrmýzý güller',   50.00, 1),
(N'Beyaz Papatya',   N'Bahar papatyalarý',     30.00, 2),
(N'Mor Kýr Çiçeði',  N'Nefis kýr çiçekleri',  120.00, 3),
(N'Sarý Lilyum',     N'Mis kokulu lilyumlar',  50.00, 4);
GO

/* Orders  */
INSERT INTO Orders (order_status, order_type, customer_id)
VALUES
(N'Tamamlandý',   N'Online', 1),
(N'Hazýrlanýyor', N'Maðaza', 2),
(N'Hazýrlanýyor', N'Online', 3);
GO

/* Order_Item  */
INSERT INTO Order_Item (quantity, unit_price, order_id, flower_id)
VALUES
(2,  50.00, 1, 1),
(5,  30.00, 1, 2),
(1, 120.00, 2, 3),
(2, 175.00, 3, 2);   -- Hamit için örnek item
GO

/* Payment */
INSERT INTO Payment (payment_method, payment_status, payment_amount, order_id)
VALUES
(N'Kredi Kartý', N'Ödendi', 250.00, 1),
(N'Nakit',       N'Ödendi', 120.00, 2),
(N'Kredi Kartý', N'Ödendi', 350.00, 3);
GO

/* Delivery */
INSERT INTO Delivery (delivery_date, time_slot, delivery_type, delivery_status, order_id)
VALUES
(GETDATE(), N'09:00-12:00', N'Eve Teslim',      N'Teslim Edildi', 1),
(GETDATE(), N'12:00-15:00', N'Maðazadan Alým',  N'Hazýrlanýyor',  2),
(GETDATE(), N'10:00-13:00', N'Eve Teslim',      N'Hazýrlanýyor',  3);
GO

/* Inventory */
INSERT INTO Inventory(quantity, flower_id)
VALUES
(100, 1),
(200, 2),
(50,  3),
(80,  4);
GO

/* Supplier */
INSERT INTO Supplier (supplier_name, phone, email)
VALUES
(N'Dilþad Çiçekçilik',      '03122234488', 'dilsadcicekcilik@hotmail.com'),
(N'Ankara Çiçek Gönderimi', '03122237555', 'ankaracicekgonderimi@gmail.com'),
(N'Ankara Çiçek Sipariþi',  '03122234488', 'ankaraciceksiparisi@gmail.com');
GO

/* Supplier_Flower */
INSERT INTO Supplier_Flower (supplier_id, flower_id)
VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 4);
GO
