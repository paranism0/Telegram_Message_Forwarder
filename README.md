<h1># In The Name Of God</h1><br>
<h2># Telegram_Message_Forwarder</h2>
<h3>what does this script do ?</h3>
<h6>it will forward messages you sent to some chats automatically .</h6>
<h3>proxy supported ? </h3>
<h6>YES ! , you can use proxy (mtproto not supported because i used pyrogram ! ) <br>set proxy in login_credential config file
</h6>
<h3>how can i use it ?</h3>
<h6>
<h3> get api_id and api_hash </h3>
<h6>
first of all you must go to <b>my.telegram.org</b> and register for getting <b>api_id</b> and <b>api_hash</b><br>
</h6>
<h3> complete login_crendetial requirements </h3>
<h6>
after those works you must complete <b>login_credential</b> file requirements such as api_id,api_hash,phone_number and stuff like that ....<br>
</h6>
<h3> create folders,add chats to them and write that in login_credential file</h3>
<h6>
after that create folders it can be one folder or more and add chats you wanna forward message to them<br>automatically to those folders and add them to folder_name in login_credential config file
</h6>
<h3> waiting for forwarding messages to prevent getting banned </h3>
<h6>
waiting recommended for forwarding message , you can set that in randint_range in login_credential config file<br>
set numbers bigger as soon as possible to prevent getting banned ....<br>
my program will sleep a random number from range you get as input to my program ...<br>
after doing that jobs do next jobs
</h6>
<h3>install requirements of script with <b>pip install -r requirements.txt</b> <br>
THEN RUN SCRIPT with python client.py </h3>
<h3>enable script for forwarding messages</h3>
<h6>
go to saved messages of your telegram account then write /start for enable forwarding messages to chats that you added to folders you write in login_credential config file ...<br>
after writing /start everything you send (except /stop) there will forward to chats ...
</h6>
<h3>disable script for forwarding messages </h3>
<h6>
for disabling this mode you must send /stop in saved message and done [+]<br>
</h6>
</h6>