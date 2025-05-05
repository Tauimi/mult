#!/usr/bin/env python3
# Скрипт для наполнения базы данных большим количеством товаров электроники и бытовой техники

from app import app
from extensions import db
from models import Product

products = [
    # Телевизоры
    {"name": "Samsung Smart TV 43\"", "description": "43\" 4K UHD Smart TV с HDR и поддержкой Wi-Fi", "price": 34990.00, "image": "/static/images/tv_samsung_43.jpg"},
    {"name": "LG OLED TV 55\"", "description": "55\" OLED телевизор с AI ThinQ и Dolby Vision", "price": 79990.00, "image": "/static/images/tv_lg_55.jpg"},
    {"name": "Sony Bravia 50\"", "description": "50\" LED Full HD с Android TV", "price": 42990.00, "image": "/static/images/tv_sony_50.jpg"},
    # Ноутбуки
    {"name": "ASUS VivoBook 15", "description": "15.6\" FHD, Intel Core i5, 8GB RAM, 512GB SSD", "price": 57990.00, "image": "/static/images/laptop_asus.jpg"},
    {"name": "Dell XPS 13", "description": "13.4\" UHD, Intel Core i7, 16GB RAM, 1TB SSD", "price": 129990.00, "image": "/static/images/laptop_dell.jpg"},
    {"name": "HP Pavilion 14", "description": "14\" FHD, AMD Ryzen 5, 8GB RAM, 256GB SSD", "price": 49990.00, "image": "/static/images/laptop_hp.jpg"},
    # Смартфоны
    {"name": "Apple iPhone 13", "description": "128GB, A15 Bionic, OLED дисплей, 5G", "price": 89990.00, "image": "/static/images/iphone13.jpg"},
    {"name": "Samsung Galaxy S21", "description": "128GB, Exynos 2100, AMOLED дисплей", "price": 74990.00, "image": "/static/images/galaxys21.jpg"},
    {"name": "Xiaomi Mi 11", "description": "256GB, Snapdragon 888, 108MP камера", "price": 55990.00, "image": "/static/images/mi11.jpg"},
    # Холодильники
    {"name": "LG FrostFree 315л", "description": "Двухкамерный No Frost, класс A+", "price": 44990.00, "image": "/static/images/fridge_lg.jpg"},
    {"name": "Bosch 323л", "description": "Однокамерный, класс A++", "price": 37990.00, "image": "/static/images/fridge_bosch.jpg"},
    {"name": "Indesit 270л", "description": "Механическое управление, класс A+", "price": 28990.00, "image": "/static/images/fridge_indesit.jpg"},
    # Стиральные машины
    {"name": "Bosch Series 6", "description": "7кг, 1200 об/мин, A+++", "price": 39990.00, "image": "/static/images/wm_bosch.jpg"},
    {"name": "Samsung EcoBubble", "description": "8кг, 1400 об/мин", "price": 45990.00, "image": "/static/images/wm_samsung.jpg"},
    {"name": "LG TurboWash", "description": "9кг, функция пара", "price": 49990.00, "image": "/static/images/wm_lg.jpg"},
    # Микроволновки
    {"name": "Panasonic NN-SN686S", "description": "20л, 1200ВТ, гриль", "price": 7990.00, "image": "/static/images/mw_panasonic.jpg"},
    {"name": "Samsung GE83MST", "description": "23л, 800ВТ", "price": 5990.00, "image": "/static/images/mw_samsung.jpg"},
    # Пылесосы
    {"name": "Xiaomi Robot", "description": "Робот-пылесос 2000Па", "price": 24990.00, "image": "/static/images/vac_xiaomi.jpg"},
    {"name": "Dyson V11", "description": "Беспроводной с ЖК-дисплеем", "price": 79990.00, "image": "/static/images/vac_dyson.jpg"},
    # Консоли
    {"name": "PlayStation 5", "description": "Консоль нового поколения", "price": 49990.00, "image": "/static/images/ps5.jpg"},
    {"name": "Xbox Series X", "description": "1TB SSD, 4K", "price": 49990.00, "image": "/static/images/xbox.jpg"},
    # Камеры
    {"name": "Canon EOS 1500D", "description": "Зеркальная камера 18-55mm", "price": 29990.00, "image": "/static/images/cam_canon.jpg"},
    {"name": "Nikon D3500", "description": "Зеркальная камера 18-55mm", "price": 32990.00, "image": "/static/images/cam_nikon.jpg"},
    # Аудио
    {"name": "JBL Flip 5", "description": "Bluetooth колонка, 12ч", "price": 6990.00, "image": "/static/images/jbl.jpg"},
    {"name": "Sony XM4", "description": "Наушники с шумоподавлением", "price": 24990.00, "image": "/static/images/sony_xm4.jpg"},
    # Принтеры
    {"name": "HP LaserJet M404", "description": "Монохромный лазерный принтер", "price": 15990.00, "image": "/static/images/pr_hp.jpg"},
    {"name": "Canon PIXMA MG3640", "description": "Струйное МФУ, Wi-Fi", "price": 9990.00, "image": "/static/images/pr_canon.jpg"}
]

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Очистка старых товаров
        db.session.query(Product).delete()
        # Добавление новых товаров
        for item in products:
            prod = Product(
                name=item["name"],
                description=item["description"],
                price=item["price"],
                image=item["image"]
            )
            db.session.add(prod)
        db.session.commit()
        print(f"База данных заполнена {len(products)} товарами.")
