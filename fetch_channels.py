import requests
import json
import time

BASE_URL = "https://nextdaywithme.shop/api/channels/"
BASE_ASSETS = "https://nextdaywithme.shop"

HEADERS = {
    "User-Agent": "okhttp/4.12.0",
    "Accept-Encoding": "gzip",
    "x-app-ver": "18"
}

def main():
    channels = []
    page = 1
    
    while True:
        params = {"page": str(page), "limit": "30"}
        print(f"جلب الصفحة {page}...")
        try:
            res = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)
            if res.status_code != 200:
                break
            data = res.json().get("data", [])
            if not data:
                break
            for ch in data:
                logo = ch.get("logo", "")
                channels.append({
                    "id": ch.get("id"),
                    "name": ch.get("name"),
                    "category": ch.get("category_label") or "عام",
                    "logo": BASE_ASSETS + logo if logo else "",
                    "streams_count": ch.get("streams_count", 0)
                })
            page += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"خطأ: {e}")
            break

    with open("channels.json", "w", encoding="utf-8") as f:
        json.dump(channels, f, ensure_ascii=False, indent=2)
    print(f"تم حفظ {len(channels)} قناة في channels.json")

if __name__ == "__main__":
    main()
