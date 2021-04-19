import base64

# @param img_file_name 传入文件路径
# @return base64_String
# img_file_name: ./dog.png
def img_to_base64(img_file_name):
    f = open(img_file_name,'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    img_name = img_file_name[:img_file_name.index('.')]
    return dict({"img_name":img_name,"base64_string":ls_f});

# 将转化后的base64存在txt文件中
# path = '/user/bobtang/desktop/'
# info['img_name'] = 'dog'
# txt文件: /user/bobtang/desktop/dog.txt
def save_as_txt(path,info):
    file_name = path + info['img_name']+'txt'
    with open(file_name,"w") as file:   #”w"代表着每次运行都覆盖内容
        file.write(str(info['base64_string'],encoding='utf8'))
        file.close()

if __name__ == '__main__':
    # img_file_name
    img_file_name = '/Users/bobtang/desktop/deskfile/vue-command/note/v-show-display:none.png'
    # 当前文件夹
    path = ''
    info = img_to_base64(img_file_name)
    save_as_txt(path,info)

