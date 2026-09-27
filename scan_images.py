import os
import json

# Thư mục chứa ảnh
image_folder = 'images'

# Lọc các định dạng ảnh phổ biến
valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

try:
    # Quét tất cả file trong thư mục
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
    
    # Tạo file Javascript chứa mảng tên ảnh
    with open('image_data.js', 'w', encoding='utf-8') as f:
        f.write(f"const imageList = {json.dumps(image_files)};")
        
    print(f"Đã quét thành công {len(image_files)} ảnh và lưu vào image_data.js!")
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy thư mục '{image_folder}'. Bạn nhớ tạo thư mục và cho ảnh vào nhé.")