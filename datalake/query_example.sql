SELECT product, COUNT(*) as total
FROM ecommerce_dataset.orders_ext
GROUP BY product
ORDER BY total DESC;