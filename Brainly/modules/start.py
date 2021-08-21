from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,                                                                                                                                                                                                 
        text="**Halo Gaess Aku Adalah Bot Brainly Yang Di Buat Untuk Mencari Jawaban Dibrainly!**, Ketik /cari pertanyaan untuk mencari pertanyaan, Bisa menggunakan inline juga loh! Contoh `@BrainlyTgBot cari siapa presiden pertama RI?` .",
        reply_to_message_id=update.message_id,
        parse_mode="markdown"
    )
