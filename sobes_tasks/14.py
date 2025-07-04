'''
SELECT DISTINCT user.firstname, purchase.sku
FROM user JOIN purchase ON user.id = purchase.user_id
          LEFT JOIN ban_list ON user.id = ban_list.user_id
WHERE ban_list.date_from IS NULL OR purchase.date < ban_list.date_from
ORDER BY user.firstname, purchase.sku
'''