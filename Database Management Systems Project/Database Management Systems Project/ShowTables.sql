USE FlowerShopDB;
GO

SELECT
    o.order_id,
    o.order_date,
    o.order_status,
    c.first_name,
    c.last_name,
    c.email,
    cp.phone,
    a.city,
    a.district,
    a.street,
    f.flower_name,
    cat.category_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS total_price,
    p.payment_method,
    p.payment_status,
    d.delivery_status
FROM Orders o
INNER JOIN Customer c
    ON o.customer_id = c.customer_id
LEFT JOIN Customer_Phone cp
    ON c.customer_id = cp.customer_id
LEFT JOIN Address a
    ON c.customer_id = a.customer_id
INNER JOIN Order_Item oi
    ON o.order_id = oi.order_id
INNER JOIN Flower f
    ON oi.flower_id = f.flower_id
INNER JOIN Category cat
    ON f.category_id = cat.category_id
INNER JOIN Payment p
    ON o.order_id = p.order_id
INNER JOIN Delivery d
    ON o.order_id = d.order_id
ORDER BY c.first_name, o.order_id;


USE FlowerShopDB;
GO

/* CUSTOMER */
SELECT * FROM Customer;

/* CUSTOMER PHONE */
SELECT * FROM Customer_Phone;

/* ADDRESS */
SELECT * FROM Address;

/* CATEGORY */
SELECT * FROM Category;

/* FLOWER */
SELECT * FROM Flower;

/* INVENTORY */
SELECT * FROM Inventory;

/* SUPPLIER */
SELECT * FROM Supplier;

/* SUPPLIER - FLOWER */
SELECT * FROM Supplier_Flower;

/* ORDERS */
SELECT * FROM Orders;

/* ORDER ITEM */
SELECT * FROM Order_Item;

/* PAYMENT */
SELECT * FROM Payment;

/* DELIVERY */
SELECT * FROM Delivery;
SELECT 
    o.order_id,
    o.order_date,
    o.order_status,
    c.first_name,
    c.last_name
FROM Orders o
JOIN Customer c ON o.customer_id = c.customer_id;

SELECT
    o.order_id,
    f.flower_name,
    oi.quantity,
    oi.unit_price
FROM Order_Item oi
JOIN Orders o ON oi.order_id = o.order_id
JOIN Flower f ON oi.flower_id = f.flower_id;

SELECT
    o.order_id,
    p.payment_method,
    p.payment_status,
    d.delivery_type,
    d.delivery_status
FROM Orders o
JOIN Payment p ON o.order_id = p.order_id
JOIN Delivery d ON o.order_id = d.order_id;

USE FlowerShopDB;
GO

SELECT
    o.order_id,
    c.first_name,
    c.last_name,
    f.flower_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS toplam_tutar
FROM Orders o
INNER JOIN Customer c
    ON o.customer_id = c.customer_id
INNER JOIN Order_Item oi
    ON o.order_id = oi.order_id
INNER JOIN Flower f
    ON oi.flower_id = f.flower_id
ORDER BY o.order_id;

USE FlowerShopDB;
GO

SELECT
    c.first_name,
    c.last_name,
    o.order_id,
    p.payment_method,
    p.payment_status
FROM Customer c
INNER JOIN Orders o
    ON c.customer_id = o.customer_id
INNER JOIN Payment p
    ON o.order_id = p.order_id
ORDER BY o.order_id;
