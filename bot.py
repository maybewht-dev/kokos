from aiogram import executor
from dispatcher import dp
import handlers

print("yeah, you can call me loverboy // truepixel studios")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)