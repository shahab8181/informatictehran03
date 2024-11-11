from random import seed, randint
from .melipayamak import Api


# TODO: melipayamk web service conf
class SMSSystem:
    username = ''
    password = ''
    sender = ''
    IR_MCI = (
        '0910', '0911', '0912',
        '0913', '0914', '0915',
        '0916', '0917', '0918',
        '0919', '0990', '0991',
        '0992', '0993'
    ) 

    def __init__(self, phone_number, start=1000, end=9999) -> None:
        seed()
        self.active_code = randint(start, end)
        self.phone_number = phone_number

    # TODO: for irancell and Rightel (REST)
    def send_otp_sms(self) -> None:
        if self.phone_number[0:4:1] not in self.IR_MCI:
            try:
                api = Api(self.username, self.password)
                sms = api.sms()
                _from = self.sender
                to = self.phone_number
                text = f"به وب سایت 'خوش نشان' خوش آمدید!\n\nکد تایید شما {self.active_code} می باشد."
                response = sms.send(to, _from, text)
                print(response)
            except:
                pass
        else:
            self.send_otp_sms_MCI()

    # TODO: for IR-MCI (SOAP)
    def send_otp_sms_MCI(self):
        try:
            api = Api(self.username, self.password)
            sms_soap = api.sms('soap')
            to = self.phone_number
            text = f'{self.active_code};'
            bodyId: int = 179190
            sms_soap.send_by_base_number(text, to, bodyId)
        except:
            pass
        
    # TODO: welcome message for irancell and Rightel (REST)
    # def welcome_message(self, user, id, login_date) -> None:
    #     if self.phone_number[0:4:1] not in self.IR_MCI:
    #         try:
    #             api = Api(self.username, self.password)
    #             sms = api.sms()
    #             _from = self.sender
    #             to = self.phone_number
    #             text = f"{user} عزیز!\n\nورود شما با ایدی کاربری {id} در تاریخ {login_date} موفقیت امیز بود.\n\nبه 'خوش نشان' خوش امدید:)"
    #             response = sms.send(to, _from, text)
    #             print(response)
    #         except:
    #             pass
    #     else:
    #         self.welcome_message_MCI(user=user, id=id, login_date=login_date)
    
    # TODO: for IR-MCI (SOAP)
    # def welcome_message_MCI(self, user, id, login_date):
    #     try:
    #         api = Api(self.username, self.password)
    #         sms_soap = api.sms('soap')
    #         to = self.phone_number
    #         text = f'{user};{id};{login_date};'
    #         bodyId: int = 179310
    #         sms_soap.send_by_base_number(text, to, bodyId)
    #     except:
    #         pass

