"""
name, phone, email, addr
"""
class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print('이름 : {} | 휴대폰번호 : {} | 이메일 : {} | 주소 : {}'.format(self.name, self.phone, self.email, self.addr))

    @staticmethod
    def set_contact():
        name = input('이름')
        phone = input('휴대폰번호')
        email = input('이메일')
        addr = input('주소')
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contacts(list):
        for i in list:
            i.print_info()

    @staticmethod
    def del_contact(list, name):
        for i, t in enumerate(list):
            if t.name == name:
                del list[i]

    @staticmethod
    def print_menu():
        print('1. 연락처 입력')
        print('2. 연락처 출력')
        print('3. 연락처 삭제')
        print('4. 종료')
        menu = input('메뉴 선택')
        return int(menu)

    @staticmethod
    def run():
        list = []
        while 1 :
            menu = Contact.print_menu()
            if menu == 1:
                t = Contact.set_contact()
                list.append(t)
            elif menu == 2:
                Contact.get_contacts(list)
            elif menu == 3:
                name = input('삭제할 이름 : ')
                Contact.del_contact(list, name)
            elif menu == 4:
                break