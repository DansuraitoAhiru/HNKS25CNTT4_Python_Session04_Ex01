total_price = int(input("Nhập tổng tiền hóa đơn ban đầu: "))
if total_price < 0:
    print("Lỗi tổng tiền ko thể < 0")
else:
    print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")

    if total_price > 500000:
        discount = int(total_price * 0.1)
        total_price = total_price - discount
    else:
        discount = total_price * 0
        total_price = total_price - discount
    
    print(f"Số tiền được giảm giá: {discount} VND")
    print(f"Tổng tiền khách phải trả: {total_price} VND")
