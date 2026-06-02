smart_parking = []
next_id = 1
while True:
    print('=== QUẢN LÝ BÃI XE - SMART PARKING ===')
    print('1. Thêm xe mới vào bãi')
    print('2. Hiển thị danh sách xe trong bãi')
    print('3. Tìm kiếm xe theo mã(id)')
    print('4. Xóa xe khỏi bãi(khi xe ra)')
    print('5. Thoát chương trình')

    choice = input('Vui lòng nhập lựa chọn của bạn: ')
    print()

    if choice not in ["1","2","3","4","5"] :
        print('Vui lòng nhập từ 1-5!')
    elif choice =="1":
        while True:
            type = input('Nhập loại xe của bạn: ').strip()
            if not type :
                print('Không được để trống. Vui lòng nhập lại!')
                continue
            break
        while True:
            owner = input('Nhập tên chủ xe: ').strip()
            if not owner:
                print('Không được để trống. Vui lòng nhập lại!')
                continue
            break
        new = {
            "id" : next_id,
            "type" : type,
            "owner" : owner
        }
        smart_parking.append(new)
        print('Thêm xe mới thành công!')
        next_id += 1
    elif choice =="2":
        if len(smart_parking) == 0 :
            print('Bãi xe hiện đang trống!')
        else:
            print('ID       | Loại xe           | Chủ xe')
            for value in (smart_parking):
                print(f'{value["id"]}        | {value["type"]}        | {value["owner"]}')
        
    elif choice == "3":
        search_id = int(input('Nhập id xe cần tìm: '))
        found = False
        for i in smart_parking :
            if i["id"] == search_id :
                found = True
                print(i)
                
        if not found:
            print(f'Không tìm thấy xe có id {search_id}')
    elif choice == "4":
        delete_id = int(input('Nhập id xe cần xóa'))
        found = False
        for i in smart_parking :
            if i["id"] == delete_id :
                found = True
                smart_parking.pop(delete_id -1)
                print(f'Đã xóa thành công xe có id: {delete_id}')
        if not found:
            print(f'Không tìm thấy xe có id: {delete_id}')
    elif choice == "5":
        print('Thoát chương trình!')
        break
