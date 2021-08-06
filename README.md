# handwriting_recognition_thesis

## Cài đặt môi trường và mô hình

### Cài đặt Python
Tải và cài đặt Python 3 từ trang [web](https://www.python.org/)

### Tải thư viện OpenNMT
Vào link [github](https://github.com/OpenNMT/OpenNMT-py/tree/legacy) của OpenNMT bản legacy, tải về và cài đặt theo hướng dẫn.

Nếu OpenNMT báo lỗi, cài thêm các thư viện sau:
```
pip install torchaudio==0.6.0
pip install torchtext==0.4.0
pip install torch==1.6.0+cu101 torchvision==0.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

### Tải file mô hình
Tải file mô hình tại [link](https://drive.google.com/file/d/1C-YFUEod8egCE1BNKbmzA5kFznuIdjUG/view?usp=sharing)
Sau đó để file mô hình ở thư mục chứa file chạy phần mềm

## Sử dụng

### Vẽ khung vị trí
![Vẽ khung vị trí](https://github.com/soiluahung/handwriting_recognition_thesis/blob/main/readme/mockup_one.png)

### Nhận diện chữ viết tay
![Nhận diện chữ viết tay](https://github.com/soiluahung/handwriting_recognition_thesis/blob/main/readme/mockup_one.png)

## Demo

[Link nhận diện trên tập ảnh test](https://youtu.be/odQlA9J7kTc)

[Link nhận diện trên file pdf](https://youtu.be/HQOG-r7jzO0)
