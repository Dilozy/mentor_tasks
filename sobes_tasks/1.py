'''
SELECT SUM(price) as total_earnings
FROM Salespersons JOIN Customers ON Salespersons.id = salesperson_id
				  JOIN Orders ON Customers.id = customer_id
GROUP BY Salespersons.id
ORDER BY Salespersons.id
'''