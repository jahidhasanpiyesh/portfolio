import json
import os

def add_blog():
    file_path = 'posts.json'
    
    # posts.json chack json file .
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    print("\n--- Add New Blog Post ---")
    title = input("Enter Post Title: ")
    link = input("Enter LinkedIn/Post Link: ")
    img = input("Enter Image URL: ")
    desc = input("Enter Short Description: ")

    # append new post to data list
    data.append({
        "title": title,
        "link": link,
        "img": img,
        "desc": desc
    })

    # write updated data back to posts.json
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("\nSuccess! Post added to posts.json. Now push to GitHub.")

if __name__ == "__main__":
    add_blog()