from OOP_Encapsulation import Coffee, Customer, CoffeeShop

def input_coffee_menu(shop):
    print("กรอกเมนูกาแฟ (พิมพ์ว่างเพื่อเลิก)")
    while True:
        name = input("ชื่อกาแฟ: ").strip()
        if not name:
            break
        description = input("คำอธิบาย: ").strip()
        while True:
            try:
                price = float(input("ราคาต่อแก้ว (บาท): "))
                break
            except ValueError:
                print("กรุณาใส่ตัวเลขราคาถูกต้อง")
        shop.add_coffee(Coffee(name, description, price))
    print("บันทึกเมนูเรียบร้อย\n")

def order_coffee(shop, customer):
    while True:
        shop.show_menu()
        choice = input("เลือกเมนูกาแฟ (เลข) หรือ พิมพ์ 'exit' เพื่อออก: ").strip()
        if choice.lower() == 'exit':
            break
        if not choice.isdigit():
            print("กรุณาใส่ตัวเลขเมนู")
            continue
        coffee_index = int(choice)
        if coffee_index < 1 or coffee_index > len(shop._CoffeeShop__menu):
            print("เลือกเมนูไม่ถูกต้อง")
            continue
        while True:
            qty = input("จำนวนแก้ว: ").strip()
            if qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                break
            else:
                print("กรุณาใส่จำนวนเป็นตัวเลขบวก")
        shop.add_to_cart(customer, coffee_index, qty)

# ---- เริ่มโปรแกรม ----
shop = CoffeeShop("Juppa Coffee")

# ให้ผู้ใช้กรอกเมนูเอง
input_coffee_menu(shop)

# สร้างลูกค้า
name = input("ชื่อผู้ซื้อ: ")
email = input("อีเมล: ")
customer = Customer(name, email)

# ให้ลูกค้าสั่งซื้อ
order_coffee(shop, customer)

# สรุปชำระเงิน
shop.checkout(customer)