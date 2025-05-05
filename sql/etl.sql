SELECT seller_id,
        SUM(price) AS total_revenue,
        COUNT(DISTINCT T1.order_id) AS qt_salles
FROM tb_order_items AS t1
GROUP BY seller_id