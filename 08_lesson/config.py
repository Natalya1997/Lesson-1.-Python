class Config:
    BASE_URL = "https://ru.yougile.com"
    API_URL = f"{BASE_URL}/api-v2"

    API_TOKEN = "сюда"

    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }