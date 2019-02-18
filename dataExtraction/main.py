from dataExtraction.extractions import extractor
from dataExtraction.management import write_list_to_csv

def preparation():
    file_path = r"C:\Users\parsitech\Documents\ScrapyAttempt\crawler\bama\crawled.txt"
    with open(file_path, "r") as myfile:
        for line in myfile:
            print(line)
            result_set = prepare_details(line)
            if result_set is not None:
                write_list_to_csv(result_set)





def prepare_details(line):
    result_set = []
    try:
        brand, model, release_date, extra_info, price, type, mileage, gear, fuel, body,  color = extractor(line)
        if "NA" in brand:
            return
    except TypeError:
        return

    try:
        price = price.replace(",","")
        price = int(price)
    except ValueError:
        return
    try:
        mileage = mileage.replace("کیلومتر","")
        mileage = mileage.replace(',','')
        mileage = int( mileage)
    except ValueError:
        #some craze put a dash instead of a zero
        mileage = 0

    release_date= int(release_date)
    if "اتوماتیک" in gear:
        gear = 1
    else:
        gear = 0
    if " بنزین" in fuel:
        fuel = 0
    elif "دوگانه سوز" in fuel:
        fuel = 1
    elif "هیبرید" in fuel:
        fuel =2
    else:
        fuel= 3
    if "بدون رنگ" in body:
        body =1
    elif "صافکاری بدون رنگ" in body:
        body =2
    elif "یک لکه رنگ" in body:
        body =3
    elif "دو لکه رنگ" in body:
        body=4
    elif "چند لکه رنگ" in body:
        body =5
    elif "گلگیر رنگ" in body:
        body = 6
    elif "گلگیر تعویض" in body:
        body = 7
    elif "یک درب رنگ" in body:
        body =8
    elif "دو درب رنگ" in body:
        body =9
    elif "درب تعویض" in body:
        body =10
    elif "کاپوت رنگ" in body:
        body =11
    elif "کاپوت تعویض" in body:
        body =12
    elif "دور رنگ" in body:
        body =13
    elif "کامل رنگ" in body:
        body =14
    elif "تصادفی" in body:
        body =15
    elif "اتاق تعویض" in body:
        body =16
    elif "سوخته" in body:
        body =17
    elif "اوراقی" in body:
        body = 18
    color = color.split('،')
    interior_color = color[1].replace('داخل ',"")
    exterior_color = color[0]
    if "سفید" in exterior_color:
        exterior_color = 0
    elif "مشکی" in exterior_color:
        exterior_color = 1
    elif "خاکستری" in exterior_color:
        exterior_color = 2
    elif "سفید صدفی" in exterior_color:
        exterior_color = 3
    elif "نقره ای" in exterior_color:
        exterior_color = 4
    elif "نوک مدادی" in exterior_color:
        exterior_color = 5
    elif "قهوه ای" in exterior_color:
        exterior_color = 6
    elif "قرمز" in exterior_color:
        exterior_color = 7
    elif "آبی" in exterior_color:
        exterior_color = 8
    elif "سرمه ای" in exterior_color:
        exterior_color = 9
    elif "بژ" in exterior_color:
        exterior_color = 10
    elif "سربی" in exterior_color:
        exterior_color = 11
    elif "تیتانیوم" in exterior_color:
        exterior_color = 12
    elif "مسی" in exterior_color:
        exterior_color = 13
    elif "آلبالویی" in exterior_color:
        exterior_color = 14
    elif "نقرآبی" in exterior_color:
        exterior_color = 15
    elif "زرد" in exterior_color:
        exterior_color = 16
    elif "سبز" in exterior_color:
        exterior_color = 17
    elif "یشمی" in exterior_color:
        exterior_color = 18
    elif "کربن بلک" in exterior_color:
        exterior_color = 19
    elif "دلفینی" in exterior_color:
        exterior_color = 20
    elif "بادمجانی" in exterior_color:
        exterior_color = 21
    elif "کرم" in exterior_color:
        exterior_color = 22
    elif "زیتونی" in exterior_color:
        exterior_color =23
    elif "طلائی" in exterior_color:
        exterior_color =24
    elif "نارنجی" in exterior_color:
        exterior_color =25
    elif "گیلاسی" in exterior_color:
        exterior_color =26
    elif "طوسی" in exterior_color:
        exterior_color =27
    elif "زرشکی" in exterior_color:
        exterior_color =28
    elif "برنز" in exterior_color:
        exterior_color =29
    elif "عنابی" in exterior_color:
        exterior_color =30
    elif "اطلسی" in exterior_color:
        exterior_color =31
    elif "پوست پیازی" in exterior_color:
        exterior_color =32
    elif "بنفش" in exterior_color:
        exterior_color =33
    elif "خاکی" in exterior_color:
        exterior_color =34
    elif "موکا" in exterior_color:
        exterior_color =35

    if "مشکی" in interior_color:
        interior_color =1
    elif "کرم" in interior_color:
        interior_color =2
    elif "طوسی" in interior_color:
        interior_color =3
    elif "نامشخص" in interior_color:
        interior_color = -1
    elif "مارون" in interior_color:
        interior_color =4
    elif "موکا" in interior_color:
        interior_color =5
    elif "قرمز" in interior_color:
        interior_color =6
    elif "قهوه ای" in interior_color:
        interior_color =7
    elif "شتری" in interior_color:
        interior_color =8
    elif "خاکستری" in interior_color:
        interior_color =9
    elif "سفید" in interior_color:
        interior_color =10
    elif "سرمه ای" in interior_color:
        interior_color =11
    elif "نارنجی" in interior_color:
        interior_color =12
    elif "آبی" in interior_color:
        interior_color =13
    elif "نوک مدادی" in interior_color:
        interior_color =14
    elif "بژ" in interior_color:
        interior_color =15
    elif "زرشکی" in interior_color:
        interior_color =16
    elif "ذغالی" in interior_color:
        interior_color =17
    elif "نقره ای" in interior_color:
        interior_color =18
    elif "دلفینی" in interior_color:
        interior_color =19
    elif "زیتونی" in interior_color:
        interior_color =20
    elif "خاکی" in interior_color:
        interior_color =21
    elif "مسی" in interior_color:
        interior_color =22
    result_set.append(brand)
    result_set.append(model)
    result_set.append(release_date)
    result_set.append(extra_info)
    result_set.append(price)
    result_set.append(type)
    result_set.append(mileage)
    result_set.append(gear)
    result_set.append(fuel)
    result_set.append(body)
    #result_set.append(description)
    result_set.append(exterior_color)
    result_set.append(interior_color)
    print(result_set)
    #print(extra_info)
    return result_set



#prepare_details("https://bama.ir/car/details-2-6765734/1397-renault-tondar90-plus-at-for-sale")

preparation()
