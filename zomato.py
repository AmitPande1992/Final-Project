from ast import Try, dump
from cgi import print_arguments
from fileinput import close
from importlib.resources import contents
import json
import datetime
from math import trunc
from os import truncate
from pickle import APPEND
from textwrap import indent
def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "age": age,
        "phone number": phn,
        "order history":[]
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "user already exist"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except json.JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"
print(register_user("user.json", "Mona", 123456, 24, 9028513779))

def user_order_history(user_json, user_id):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            print("order History")
            print("date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    file.close()
    return False 

#CRUD Operation for Food(Create, update, read, delete)
def add_food(food_json, food_name, no_plates=1):
    food = {
        "id" :1,
        "name": food_name,
        "no. of plates" : no_plates
    }
    try:
        fp = open(food_json, "r+")
        content = json.load(fp)
        for i in range(len(content)):
            if content[i]["name"] == food_name:
                fp.close()
                return "Food already available"
        food["id"] = len(content) +1
        content.append(food)
    except json.JSONDecodeError:
        content = []
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content, fp, indent=4)
    fp.close()
    return "Success"

def update_food(food_json, food_id, no_plates=1):#no_plates=-1, price=-1):
    file = open(food_json, "r+")
    content = json.load(file)
#    if price > -1 and no_plates > -1: bla bla bla
#    elif price > -1: bla bla bla
#    else: bla bla bla
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no. of plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def remove_food(food_json, food_id):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "success"
    return "Pls Enter Valid ID"

def read_food(food_json):
    file = open(food_json)
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print("Id: ", content[i]["id"])
        print(f"---> Name: {content[i]['name']}")
        print(f"---> Number of Plates: {content[i]['no. of plates']}")
    file.close()
    return True
