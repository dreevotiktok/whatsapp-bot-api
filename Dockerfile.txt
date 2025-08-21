# استخدم صورة بايثون أساسية
FROM python:3.9

# تثبيت المتصفح ومشغل الويب (Chrome) لـ Pywhatkit
RUN apt-get update && apt-get install -y \
    chromium-browser \
    libnss3-dev \
    libgconf-2-4 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# تعيين مسار العمل في الحاوية
WORKDIR /app

# انسخ ملفات المكتبات وقم بتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# انسخ كود التطبيق
COPY . .

# تحديد المنفذ الذي سيستخدمه التطبيق
EXPOSE 10000

# الأمر الذي سيتم تشغيله عند بدء الحاوية
CMD ["python", "app.py"]