from pyrogram import Client,filters
import pyrogram
import config
c=config.Profile
app=Client('n',api_id=c['api_id'],api_hash=c['api_hash'],app_version=c['version'],device_model=c['model'],lang_code=c['lang'],hide_password=True,system_version=c['System_version'])
@app.on_message(filters.private)
def avtootvet(client,message):
    app.send_photo(message.from_user.id,"s-min.gif",caption=config.welcome)
app.run()