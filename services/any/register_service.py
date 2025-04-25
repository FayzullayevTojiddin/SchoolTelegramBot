
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register import RegisterState
from states.any_states import MainState

from helpers.get_main_keyboard_helper import get_main_keyboard

from locales.message import start_message as start_message_text

from models.user import User

class RegisterService():
    async def controller(self, message: Message, state: FSMContext):
        inState = await state.get_state()
        if not message.text:
            text = "❗️Iltimos, xabar ko‘rinishida yuboring."
            keyboard = None
            state = inState
            return text, keyboard, state

        if inState == RegisterState.getFullName:
            return await self.getAge(message, state)
        elif inState == RegisterState.getAge:
            return await self.getPhoneNumber(message, state)
        elif inState == RegisterState.getPhoneNumber:
            return await self.completedRegister(message, state)
        elif inState == RegisterState.main or inState == None:
            return self.getFullName()
        
    def getFullName(self):
        text = "👤 *To‘liq ismingizni* kiriting:"
        state = RegisterState.getFullName
        return text, None, state
    
    async def getAge(self, message, state):
        await state.update_data(full_name=message.text)
        text = "📅 *Yoshingizni* kiriting:"
        state = RegisterState.getAge
        return text, None, state
    
    async def getPhoneNumber(self, message, state):
        await state.update_data(age=message.text)
        text = "📞 *Telefon raqamingizni* yuboring:"
        keyboard = None
        state = RegisterState.getPhoneNumber
        return text, keyboard, state
    
    async def completedRegister(self, message, state):
        try:
            data = await state.get_data()
            phoneNumber = message.text
            age = data['age']
            full_name = data['full_name']
            user = User.registerUser(
                message.from_user.id, full_name, age, phoneNumber
            )
            role = User.get_role(message.from_user.id)
            text = start_message_text
            keyboard = get_main_keyboard(role)
            state = MainState.main
            return text, keyboard, state
        except Exception as error:
            text = "⚠️ *Ma’lumotlar noto‘g‘ri ko‘rsatildi.*\n\nIltimos, qaytadan urinib ko‘ring."
            keyboard = None
            await state.clear()
            state = RegisterState.main
            return text, keyboard, state