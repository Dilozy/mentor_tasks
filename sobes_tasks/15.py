'''
SELECT user.id, user.firstname, user.lastname, COALESCE(SUM(price), 0) as total_spent
FROM user LEFT JOIN purchase ON user.id = purchase.user_id
GROUP BY user.id, user.firstname, user.lastname
HAVING COALESCE(SUM(price), 0) > 5000
'''