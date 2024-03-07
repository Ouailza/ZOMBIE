import random
import string
import json
import os


# قاعدة بيانات تخزين الرموز لكل شخص
codes_database = {}

def generate_unique_code():
    # توليد رمز عشوائي مكون من 6 أحرف وأرقام
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    return code

def save_codes_to_file(filename='ZOMBIE.json'):
    # حفظ قاعدة البيانات في ملف
    with open(filename, 'w') as file:
        json.dump(codes_database, file)

def load_codes_from_file(filename='ZOMBIE.json'):
    # استرجاع قاعدة البيانات من الملف
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def get_or_generate_code(user_id):
    global codes_database
    
    # جلب قاعدة البيانات من الملف
    codes_database = load_codes_from_file()
    
    # إذا كان الشخص مسجل مسبقًا، استرجاع الرمز المخزن له
    if user_id in codes_database:
        return codes_database[user_id]
    else:
        # إنشاء رمز جديد وتخزينه للشخص الجديد
        new_code = generate_unique_code()
        codes_database[user_id] = new_code
        # حفظ قاعدة البيانات في الملف
        save_codes_to_file()
        return new_code

# محاكاة استخدام الرموز للمستخدمين
user1_id = 'user123'

# الحصول على الرموز للمستخدمين
user1_code = get_or_generate_code(user1_id)
#بداية الاداة
os.system('clear') 
print('\033[1;36m''~'*50)
print('\033[1;32m'"""  ███████╗░█████╗░███╗░░░███╗██████╗░██╗███████╗
  ╚════██║██╔══██╗████╗░████║██╔══██╗██║██╔════╝
  ░░███╔═╝██║░░██║██╔████╔██║██████╦╝██║█████╗░░
  ██╔══╝░░██║░░██║██║╚██╔╝██║██╔══██╗██║██╔══╝░░
  ███████╗╚█████╔╝██║░╚═╝░██║██████╦╝██║███████╗
  ╚══════╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝╚══════╝""")
print('\033[1;36m''~'*50)
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''TOOL :''\033[1;32m'' ZOMBIE')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''TYPE :''\033[1;31m'' PAID')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''VERSION :''\033[1;33m'' 0.1')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''DEVELOPER :''\033[1;36m'' OUAIL')
print('\033[1;36m''~'*50)
print('\033[1;32m''YOUR KEY : ',user1_code)
print('\033[1;36m''~'*50)
print('\033[1;32m''[''\033[1;37m''1''\033[1;32m'']''\033[1;37m'' CREATE FILE') 
print('\033[1;32m''[''\033[1;37m''2''\033[1;32m'']''\033[1;37m'' CRACK FILE')
print('\033[1;32m''[''\033[1;37m''3''\033[1;32m'']''\033[1;37m'' 2009-2010')
print('\033[1;32m''[''\033[1;37m''4''\033[1;32m'']''\033[1;37m'' EXIT')
print(" ")
num = input('\033[1;32m''CHOSE ONE OF SERVICE: ''\033[1;37m') 
if num == '1':
	import os
os.system('clear') 
print('\033[1;36m''~'*50)
print('\033[1;32m'"""  ███████╗░█████╗░███╗░░░███╗██████╗░██╗███████╗
  ╚════██║██╔══██╗████╗░████║██╔══██╗██║██╔════╝
  ░░███╔═╝██║░░██║██╔████╔██║██████╦╝██║█████╗░░
  ██╔══╝░░██║░░██║██║╚██╔╝██║██╔══██╗██║██╔══╝░░
  ███████╗╚█████╔╝██║░╚═╝░██║██████╦╝██║███████╗
  ╚══════╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝╚══════╝""")
print('\033[1;36m''~'*50)
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''TOOL :''\033[1;32m'' ZOMBIE')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''TYPE :''\033[1;31m'' PAID')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''VERSION :''\033[1;33m'' 0.1')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''DEVELOPER :''\033[1;36m'' OUAIL')
print('\033[1;32m''[''\033[1;37m''※''\033[1;32m''] ''\033[1;37m''SERVICE :''\033[1;34m'' CREATE FILE')
print('\033[1;36m''~'*50)

