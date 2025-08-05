# == main.py ==
from coffee_shop import Coffee, Customer, CoffeeShop

# สร้างร้านกาแฟ
shop = CoffeeShop("Juppa Coffee")

# เพิ่มเมนูกาแฟ
shop.add_coffee(Coffee("Espresso", "เข้มข้นไม่มีน้ำตาล", 45))
shop.add_coffee(Coffee("Latte", "เอสเปรสโซ่นมสด", 55))
shop.add_coffee(Coffee("Cappuccino", "ฟองนมนุ่มๆ หอมหวาน", 60))
shop.add_coffee(Coffee("Americano", "กาแฟดำ รสเข้ม", 50))

# สร้างลูกค้า
customer = Customer("Joy", "joy@example.com")

# แสดงเมนู
shop.show_menu()

# เพิ่มลงตะกร้า
shop.add_to_cart(customer, 2, 1)  # Latte 1 แก้ว
shop.add_to_cart(customer, 4, 2)  # Americano 2 แก้ว

# ชำระเงิน
shop.checkout(customer)

# หมายเลข order จะเปลี่ยนไปทุกครั้ง — ให้ copy มาจาก output เพื่อ track ได้
# ตัวอย่าง (ต้องแก้ให้ตรงกับเลขจริง):
# shop.track_order(customer, "ใส่เลข order_id ที่ได้ตรงนี้")