
def add_product(product_list):
    # รับชื่อกาแฟ (ห้ามว่าง)
    while True:
        name = input("กรอกชื่อกาแฟ: ").strip()
        if name:
            break
        print("❌ กรุณากรอกชื่อกาแฟให้ถูกต้อง")

    # รับจำนวนแก้ว (ตรวจสอบว่าเป็นตัวเลขบวก)
    while True:
        try:
            quantity = int(input("กรอกจำนวนแก้ว: "))
            if quantity > 0:
                break
            else:
                print("❌ จำนวนแก้วต้องมากกว่า 0")
        except ValueError:
            print("❌ กรุณากรอกตัวเลขเท่านั้น")

    # ตรวจสอบว่ากาแฟมีอยู่แล้วหรือยัง
    for product in product_list:
        if product["name"].lower() == name.lower():
            product["quantity"] += quantity
            print(f"✅ เพิ่มกาแฟ '{name}' อีก {quantity} แก้ว (รวมเป็น {product['quantity']} แก้ว)")
            return  # จบการทำงานของฟังก์ชัน

    # กาแฟยังไม่มี สร้างใหม่
    product = {"name": name, "quantity": quantity}
    product_list.append(product)
    print(f"✅ เพิ่มเมนูกาแฟใหม่: {product['name']} - {product['quantity']} แก้ว")


def show_products(product_list):
    print("\n☕ รายการกาแฟที่ขายทั้งหมด:")
    
    if not product_list:
        print("⚠️ ยังไม่มีรายการกาแฟที่ขาย")
    else:
        for i, product in enumerate(product_list, start=1):
            print(f"{i}. {product['name']} - {product['quantity']} แก้ว")


# ----------------------------------------
# เริ่มโปรแกรม
product_list = []

while True:
    print("\n📌 เมนูร้านกาแฟ")
    print("1. เพิ่มรายการกาแฟที่ขาย")
    print("2. แสดงรายการกาแฟทั้งหมด")
    print("3. ออกจากระบบ")

    choice = input("เลือกเมนู (1/2/3): ").strip()

    if choice == "1":
        add_product(product_list)
    elif choice == "2":
        show_products(product_list)
    elif choice == "3":
        print("👋 ออกจากระบบแล้ว ขอบคุณที่ใช้ระบบจัดการร้านกาแฟ")
        break
    else:
        print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1, 2 หรือ 3)")