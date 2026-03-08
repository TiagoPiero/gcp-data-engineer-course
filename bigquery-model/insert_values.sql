INSERT INTO ecommerce_dataset.users (user_id, name, email) VALUES
(1, 'Alice Jhonson', 'alice.jhonson@example.com'),
(2, 'Bob Smith', 'bob.smith@example.com'),
(3, 'Charlie Brown', 'charlie.brown@example.com');

INSERT INTO ecommerce_dataset.orders (order_id, user_id, product, price) VALUES
(101, 1, 'Laptop', 999.99),
(102, 2, 'Smartphone', 499.99),
(103, 3, 'Headphones', 199.99),
(104, 1, 'Monitor', 299.99),
(105, 2, 'Keyboard', 89.99);
