def handler(event):
    name = event.get("name","work")
    return {"message" : f"hello , {name}!"}

if __name__ == "__main__":
    result = handler({"name": "devops"})
    print(result)

print("hello world")