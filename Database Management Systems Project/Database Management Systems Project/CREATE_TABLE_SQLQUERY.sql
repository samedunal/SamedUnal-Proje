
/* 2. ADIM: TABLOLARI OLUÞTURMA */

/*   A. CUSTOMER TABLE */
CREATE TABLE Customer (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name  NVARCHAR(50) NOT NULL,
    email      NVARCHAR(100) NOT NULL UNIQUE
);
GO

/*   B. CUSTOMER_PHONE TABLE */

CREATE TABLE Customer_Phone (
    phone_id INT IDENTITY(1,1) PRIMARY KEY,
    phone NVARCHAR(20) NOT NULL,
    customer_id INT NOT NULL,
    CONSTRAINT FK_CustomerPhone_Customer
        FOREIGN KEY (customer_id)
        REFERENCES Customer(customer_id)
        ON DELETE CASCADE
);
GO

/* C. Address TABLE  */ 

CREATE TABLE Address (
    address_id INT IDENTITY(1,1) PRIMARY KEY,
    city NVARCHAR(50),
    district NVARCHAR(50),
    street NVARCHAR(50),
    customer_id INT NOT NULL,
    CONSTRAINT FK_Address_Customer
        FOREIGN KEY (customer_id)
        REFERENCES Customer(customer_id)
        ON DELETE CASCADE
);
GO

/* D. CATEGORY TABLE  */
CREATE TABLE Category (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(50) NOT NULL,
    is_active BIT DEFAULT 1
);
GO

/*   E. FLOWER TABLE */


CREATE TABLE Flower (
    flower_id INT IDENTITY(1,1) PRIMARY KEY,
    flower_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    unit_price DECIMAL(10,2) NOT NULL,
    is_active BIT DEFAULT 1,
    category_id INT NOT NULL,
    CONSTRAINT FK_Flower_Category
        FOREIGN KEY (category_id)
        REFERENCES Category(category_id)
);
GO

/*  F.  ORDERS TABLE */

CREATE TABLE Orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    order_date DATETIME NOT NULL DEFAULT GETDATE(),
    order_status NVARCHAR(30),
    order_type NVARCHAR(30),
    customer_id INT NOT NULL,
    CONSTRAINT FK_Orders_Customer
        FOREIGN KEY (customer_id)
        REFERENCES Customer(customer_id)
);
GO

/*  G.  ORDER_ITEM TABLE */


CREATE TABLE Order_Item (
    order_item_id INT IDENTITY(1,1) PRIMARY KEY,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    order_id INT NOT NULL,
    flower_id INT NOT NULL,
    CONSTRAINT FK_OrderItem_Order
        FOREIGN KEY (order_id)
        REFERENCES Orders(order_id),
    CONSTRAINT FK_OrderItem_Flower
        FOREIGN KEY (flower_id)
        REFERENCES Flower(flower_id)
);
GO

/* H. PAYMENT TABLE  */
CREATE TABLE Payment (
    payment_id INT IDENTITY(1,1) PRIMARY KEY,
    payment_method NVARCHAR(30),
    payment_status NVARCHAR(30),
    payment_amount DECIMAL(10,2),
    order_id INT NOT NULL,
    CONSTRAINT FK_Payment_Order
        FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
);
GO

/*  I.  DELIVERY TABLE */

CREATE TABLE Delivery (
    delivery_id INT IDENTITY(1,1) PRIMARY KEY,
    delivery_date DATE,
    time_slot NVARCHAR(30),
    delivery_type NVARCHAR(30),
    delivery_status NVARCHAR(30),
    order_id INT NOT NULL,
    CONSTRAINT FK_Delivery_Order
        FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
);
GO

/* J. INVENTORY TABLE  */
CREATE TABLE Inventory (
    inventory_id INT IDENTITY(1,1) PRIMARY KEY,
    quantity INT NOT NULL,
    last_updated DATE DEFAULT GETDATE(),
    flower_id INT UNIQUE,
    CONSTRAINT FK_Inventory_Flower
        FOREIGN KEY (flower_id)
        REFERENCES Flower(flower_id)
);
GO

/* K. SUPPLIER TABLE  */
CREATE TABLE Supplier (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    supplier_name NVARCHAR(100) NOT NULL,
    phone NVARCHAR(20),
    email NVARCHAR(100)
);
GO


/* L. SUPPLIER_FLOWER TABLE  */



CREATE TABLE Supplier_Flower (
    supplier_id INT NOT NULL,
    flower_id INT NOT NULL,
    CONSTRAINT PK_SupplierFlower
        PRIMARY KEY (supplier_id, flower_id),
    CONSTRAINT FK_SF_Supplier
        FOREIGN KEY (supplier_id)
        REFERENCES Supplier(supplier_id),
    CONSTRAINT FK_SF_Flower
        FOREIGN KEY (flower_id)
        REFERENCES Flower(flower_id)
);
GO


