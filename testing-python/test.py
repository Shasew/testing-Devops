def handler(event):
    name = event.get("name","work")
    print(f"Handling event for {name}")
    print("Event processed successfully")
    return {"message" : f"hello , {name}!"}

if __name__ == "__main__":
    result = handler({"name": "devops"})
    print(result)

print("hello world")
print ("hi there")