from aiogram import Bot, Dispatcher, executor, types
import python_weather

# bot init
bot = Bot(token="6182451711:AAHsOJsqNPKT_A5VozDlExWylZBLs_LagZw")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

# echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)
    
    resp_msg = weather.location_name + "\n"
    resp_msg += f"Поточна температура: {celsius}\n"
    resp_msg += f"Стан погоди: {weather.current.sky_text}"
    
    await message.answer(resp_msg)
    
# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)