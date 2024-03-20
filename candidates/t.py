t = [{"item": "one"}, {"item": "two"}]

key = "one"
search_res = []

for item in t:
    if key.lower() in item["item"].lower():
        search_res.append(item)

print(search_res)