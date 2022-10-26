SELECT id FROM invoices WHERE customer_id=(SELECT id FROM customers WHERE name="Ozai");
