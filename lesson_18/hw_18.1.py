import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()
search_data = search_response.json()

items = search_data.get("collection", {}).get("items", [])
nasa_ids = []

for item in items:
    data = item.get("data", [])
    if data:
        nasa_id = data[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)

selected_ids = nasa_ids[:2]

for index, nasa_id in enumerate(selected_ids, start=1):
    asset_url = asset_url_template.format(nasa_id=nasa_id)

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()
    asset_data = asset_response.json()

    asset_items = asset_data.get("collection", {}).get("items", [])

    jpg_url = None
    for item in asset_items:
        href = item.get("href", "")
        if href.lower().endswith(".jpg"):
            jpg_url = href
            break

    if jpg_url:
        image_response = requests.get(jpg_url)
        image_response.raise_for_status()

        filename = f"mars_photo{index}.jpg"
        with open(filename, "wb") as f:
            f.write(image_response.content)

        print(f"Saved {filename}")
    else:
        print(f"No JPG found for {nasa_id}")