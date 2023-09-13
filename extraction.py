import easyocr
import os
import pprint as pp
import re

def extract_text(image):
    reader =  easyocr.Reader(["en"])
    text = reader.readtext(image,detail=0,paragraph=True)
    return text



def companyname(text):
    text = text
    exe = r'com'
    for x in text:
        if re.search(exe,text[-1]):
            res = text[-2]
        else:
            res = text[-1]
    return res

def card_holder_name(text):
    text = text 
    name = ""
    name_desc = text[0]
    tempn = name_desc.split(' ')
    if len(tempn) == 3:
        name = tempn[0]
    else:
        name = tempn[0] +" "+ tempn[1]
    return name




def desgination(text):
    text = text 
    des= text[0]
    desgination =""
    tempn = des.split(' ')
    if len(tempn) == 3:
        desgination = tempn[1] +" "+ tempn[2]
    else:
        desgination = tempn[2] +" "+ tempn[3] +" "+ tempn[4]

    return desgination



def mobile_number(text):
    text =text
    exp = r'\+?\d{2,}-\d{3}-\d{4}'
    for x in text:
        x = re.findall(exp,x)
        if len(x)>=1:
            result = x
            return result


def email_address(text):
    text = text 
    exp = r'\S+@\S+'
    for x in text:
        result = re.findall(exp,x)
        if len(result)>=1:
            return result

def website_URL(text):
    text = text 
    exp =  r'[wW]{3}[a-zA-Z\s\.]+com'
    for x in text:
        result = re.findall(exp,x)
        if len(result)>=1:
            return result

def state(text):
    text =text
    exp =  r'TamilNadu' 
    for x in text:
        result = re.findall(exp,x)
        if len(result)>=1:
            return result

def pin_code(text):
    text = text 
    exp = r'6\d{5,}'
    for x in text:
        result = re.findall(exp,x)
        if len(result)>=1:
            return result
        

def details(text):
    text = text
    data ={}
    data["COMPANY NAME"] = companyname(text)
    data["CARD HOLDER NAME"] = card_holder_name(text)
    data["DESIGN"] = desgination(text)
    data["MOBILE NUMBER"] = ",".join(mobile_number(text))
    data["EMAIL ADDRESS"] = "".join(email_address(text))
    data["WEBSITE URL"] = "".join(website_URL(text))
    data["STATE"] = "".join(state(text))
    data["PINCODE"] = "".join(pin_code(text))
    return data