import os
import shutil
import time

path = input("Enter Path: ")
i = 1
for root,dirs,files in os.walk(path):
    for f in files:
        f_name, f_ext = os.path.splitext(f)
        if f_ext == "":
            continue
        else:
            try:
                ti_m = os.path.getmtime(root + '/' + f)
                m_ti = time.ctime(ti_m)
                t_obj = time.strptime(m_ti)
                f_date = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
                f_year = f_date[:4]
                f_new_name = '#' + str(i) + ' ' + time.strftime("%Y-%m-%d", t_obj) + f_ext
            except:
                f_new_name = '#' + str(i) + f_ext
                f_year = 'No Date'
            print(f_new_name)
            if f_year == '':
                continue
            if os.path.exists(path + '/' + f_year):
                shutil.move(root + '/' + f, path + '/' + f_year + '/' + f)
                os.rename(path + '/' + f_year + '/' + f, path + '/' + f_year + '/' + f_new_name)
                i = i + 1
            else:
                os.makedirs(path + '/' + f_year)
                shutil.move(root + '/' + f, path + '/' + f_year + '/' + f)
                os.rename(path + '/' + f_year + '/' + f, path + '/' + f_year + '/' + f_new_name)
                i = i + 1


