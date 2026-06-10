parking_lot = []
id_counter = 1

while True:
    print("\n=============================================")
    print("HỆ THỐNG QUẢN LÝ BÃI ĐỖ XE THÔNG MINH (SRS)")
    print("=============================================")
    print("1. Tiếp nhận xe vào bãi (Check-in)")
    print("2. Báo cáo tồn kho bãi xe (List)")
    print("3. Tìm kiếm xe theo biển số")
    print("4. Tiếp nhận xe ra bãi (Check-out)")
    print("5. Thoát chương trình")
    print("=============================================")
    
    raw_choice = input("Chọn chức năng (1-5): ").strip()
    if not raw_choice:
        print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
        continue
    
    is_digit = True
    for char in raw_choice:
        if char < '0' or char > '9':
            is_digit = False
            break
            
    if not is_digit:
        print("[ERR-02] Sai định dạng số. Vui lòng nhập lại một số nguyên.")
        continue
        
    choice = int(raw_choice)
    
    if choice == 5:
        print("\nCảm ơn bạn đã sử dụng hệ thống! Hẹn gặp lại.")
        break
        
    elif choice == 1:
        print("\n--- TIẾP NHẬN XE VÀO (CHECK-IN) ---")
        
        while True:
            plate = input("Nhập biển số xe: ").strip().upper()
            if plate:
                break
            print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
            
        duplicate = False
        for vehicle in parking_lot:
            if vehicle['plate'] == plate:
                duplicate = True
                break
                
        if duplicate:
            print(f"[ERR-03] Lỗi: Biển số {plate} hiện đang có trong bãi xe!")
            continue
            
        while True:
            raw_type = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if not raw_type:
                print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
                continue
                
            is_digit = True
            for char in raw_type:
                if char < '0' or char > '9':
                    is_digit = False
                    break
            if not is_digit:
                print("[ERR-02] Sai định dạng số. Vui lòng nhập lại một số nguyên.")
                continue
                
            type_code = int(raw_type)
            if type_code == 1:
                vehicle_type = "Xe may"
                break
            elif type_code == 2:
                vehicle_type = "O to"
                break
            else:
                print("[ERR-05] Loại xe không hợp lệ. Chỉ chọn 1 (Xe máy) hoặc 2 (Ô tô).")
                
        while True:
            raw_entry = input("Nhập giờ vào (0 - 23): ").strip()
            if not raw_entry:
                print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
                continue
                
            is_digit = True
            for char in raw_entry:
                if char < '0' or char > '9':
                    is_digit = False
                    break
            if not is_digit:
                print("[ERR-02] Sai định dạng số. Vui lòng nhập lại một số nguyên.")
                continue
                
            entry_time = int(raw_entry)
            if 0 <= entry_time <= 23:
                break
            print("[ERR-06] Giờ vào phải nằm trong khoảng từ 0 đến 23.")
            
        new_vehicle = {
            "id": id_counter,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }
        parking_lot.append(new_vehicle)
        id_counter += 1
        print(f"==> CHECK-IN THÀNH CÔNG! Xe {plate} đã vào bãi (ID: {new_vehicle['id']}).")
        
    elif choice == 2:
        print("\n--- DANH SÁCH XE TRONG BÃI ---")
        if not parking_lot:
            print("[ERR-EMPTY] Hiện tại không có xe nào trong bãi.")
            continue
            
        header = f"{'ID':<5} | {'Biển số':<15} | {'Loại xe':<10} | {'Giờ vào':<8}"
        print(header)
        print("-" * len(header))
        for v in parking_lot:
            print(f"{v['id']:<5} | {v['plate']:<15} | {v['type']:<10} | {v['entry_time']:<8}")
        print(f"Tổng số lượng xe hiện tại: {len(parking_lot)}")
        
    elif choice == 3:
        print("\n--- TÌM KIẾM XE ---")
        if not parking_lot:
            print("[ERR-EMPTY] Bãi xe trống. Không thể tìm kiếm.")
            continue
            
        while True:
            plate = input("Nhập biển số xe cần tìm: ").strip().upper()
            if plate:
                break
            print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
            
        found_vehicle = None
        for vehicle in parking_lot:
            if vehicle['plate'] == plate:
                found_vehicle = vehicle
                break
                
        if found_vehicle:
            print("\n==> ĐÃ TÌM THẤY THÔNG TIN XE:")
            print(f" + ID: {found_vehicle['id']}")
            print(f" + Biển số: {found_vehicle['plate']}")
            print(f" + Loại xe: {found_vehicle['type']}")
            print(f" + Giờ vào: {found_vehicle['entry_time']}h")
        else:
            print(f"[ERR-04] Không tìm thấy xe có biển số {plate} trong bãi.")
            
    elif choice == 4:
        print("\n--- XE RA VÀ THANH TOÁN (CHECK-OUT) ---")
        if not parking_lot:
            print("[ERR-EMPTY] Bãi xe trống. Không thể thực hiện check-out.")
            continue
            
        while True:
            plate = input("Nhập biển số xe ra: ").strip().upper()
            if plate:
                break
            print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
            
        target_index = -1
        for i in range(len(parking_lot)):
            if parking_lot[i]['plate'] == plate:
                target_index = i
                break
                
        if target_index == -1:
            print(f"[ERR-04] Không tìm thấy xe có biển số {plate} trong bãi.")
            continue
            
        vehicle = parking_lot[target_index]
        
        while True:
            raw_exit = input(f"Nhập giờ ra (Giờ vào là {vehicle['entry_time']}h): ").strip()
            if not raw_exit:
                print("[ERR-01] Dữ liệu không được để trống. Vui lòng nhập lại.")
                continue
                
            is_digit = True
            for char in raw_exit:
                if char < '0' or char > '9':
                    is_digit = False
                    break
            if not is_digit:
                print("[ERR-02] Sai định dạng số. Vui lòng nhập lại một số nguyên.")
                continue
                
            exit_time = int(raw_exit)
            if exit_time < 0 or exit_time > 23:
                print("[ERR-06] Giờ ra phải nằm trong khoảng từ 0 đến 23.")
                continue
                
            if exit_time >= vehicle['entry_time']:
                break
            print(f"[ERR-LOGIC] Giờ ra ({exit_time}h) không được nhỏ hơn giờ vào ({vehicle['entry_time']}h). Vui lòng nhập lại.")
            
        duration = exit_time - vehicle['entry_time']
        if duration == 0:
            duration = 1
            
        fee_per_hour = 5000 if vehicle['type'] == "Xe may" else 20000
        total_fee = duration * fee_per_hour
        
        print("\n" + "="*30)
        print("       HÓA ĐƠN THANH TOÁN       ")
        print("="*30)
        print(f" Biển số:    {vehicle['plate']}")
        print(f" Loại xe:    {vehicle['type']}")
        print(f" Thời gian:  {vehicle['entry_time']}h -> {exit_time}h ({duration} giờ)")
        
        hundreds = total_fee % 1000
        thousands = total_fee // 1000
        if thousands > 0:
            print(f" THÀNH TIỀN: {thousands},{hundreds:03d} VND")
        else:
            print(f" THÀNH TIỀN: {hundreds} VND")
        print("="*30)
        
        parking_lot.pop(target_index)
        print(f"==> CHECK-OUT THÀNH CÔNG! Xe {plate} đã rời khỏi bãi.")
        
    else:
        print("[ERR-05] Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")