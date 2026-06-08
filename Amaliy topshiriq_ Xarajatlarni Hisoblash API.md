**Amaliy topshiriq: Xarajatlarni Hisoblash API**

**Maqsad**

FastAPI yordamida foydalanuvchilar o'z kundalik xarajatlarini boshqarishi mumkin bo'lgan REST API yaratish. Tizimda foydalanuvchi ro'yxatdan o'tishi, tizimga kirishi va faqat o'ziga tegishli xarajatlarni boshqarishi kerak.

**Ishlatilishi shart bo'lgan texnologiyalar**

* FastAPI  
* SQLAlchemy  
* Alembic  
* Pydantic  
* python-jose (JWT)

**Jadvallar**

**Foydalanuvchi**

Ustunlar:

* id  
* ism  
* elektron\_pochta  
* parol\_xeshi

**Xarajat**

Ustunlar:

* id  
* nomi  
* summa  
* toifa  
* sana  
* foydalanuvchi\_id

Misol:

| Nomi | Summa | Toifa |
| ----- | ----- | ----- |
| Tushlik | 35 000 | Oziq-ovqat |
| Taksi | 18 000 | Transport |
| Kino | 50 000 | Ko'ngilochar |

**Talablar**

1.Foydalanuvchini ro'yxatdan o'tkazish endpointini yarating.

Endpoint: POST /auth/register

Talablar:

* Elektron pochta takrorlanmas bo'lishi kerak.  
* Parol xeshlangan holda saqlanishi kerak.

2.Tizimga kirish endpointini yarating.

Endpoint: POST /auth/login

Talablar:

* Elektron pochta va parol orqali tekshirish amalga oshirilsin.  
* Muvaffaqiyatli kirishda JWT qaytarilsin.

Misol javob:

{  
 "access\_token": "jwt\_token"  
}

3\. Joriy foydalanuvchi ma'lumotlarini olish endpointini yarating.

Endpoint: GET /users/me

Talablar:

* JWT orqali foydalanuvchi aniqlansin.  
* Foydalanuvchi ma'lumotlari qaytarilsin.

4\. Xarajat qo'shish endpointini yarating.

Endpoint: POST /expenses

So'rov namunasi:

{  
 "name": "Tushlik",  
 "amount": 35000,  
 "category": "Oziq-ovqat"  
}

Talablar:

* Faqat tizimga kirgan foydalanuvchi xarajat qo'sha oladi.  
* Xarajat avtomatik ravishda foydalanuvchiga bog'lansin.

5\. Foydalanuvchining barcha xarajatlarini olish endpointini yarating.

Endpoint: GET /expenses

Talablar:

* Faqat joriy foydalanuvchining xarajatlari qaytarilsin.

6\. Xarajat ma'lumotlarini yangilash endpointini yarating.

Endpoint: PUT /expenses/{id}

Talablar:

* Faqat xarajat egasi yangilay olishi kerak.  
* Boshqa foydalanuvchining xarajatini yangilash taqiqlanadi.

7\. Xarajatni o'chirish endpointini yarating.

Endpoint:

DELETE /expenses/{id}

Talablar:

* Faqat xarajat egasi o'chira olishi kerak.

