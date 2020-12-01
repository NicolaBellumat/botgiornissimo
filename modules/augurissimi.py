# dependencies

import datetime
import modules.tokens as tokens
import telegram.ext
import telegram

# Variables

# Events dictionary
Events = dict()
Events["compleanno_bottone"] = datetime.date(1992, 11, 26)
# Calendar version
Events_daymonth = {key: [value.day, value.month] for key, value in Events.items()}

# Initalize variables
payload = dict()
CONTINUE = 0

def auguri_bottone(context: telegram.ext.CallbackContext, iterations: int, update: telegram.Update = None) -> int:
    if update is None:
        job = context.job
        chat_id = job.context
    else:
        chat_id = update.effective_chat.id

    if iterations == 0:
        context.bot.send_message(chat_id,
                                 text='ş̵̧̨̢̢̢̢̛̳̳͚̲̮̺̮͙̤̤͙̜̘̹̯̱̯̝̩̲̝̘̝̞̘͕̜̩̞̰̣͉͍͎͓̞͈̦̻̙̻̪̻͚̗̺̜̤̯̼̳̹̭͍͇̜̈̍̋́̀̾̇̇͛̿́̈́̃̈̐̔͑̉̊̋̈́̍̉̑̿͛̂͑͒͒̍̈́̔͂̉̍̅̅̀͋̃͂̀̕̚̕͜͝͠͝ͅͅp̷̧̧̢̢̧̢̨̡̮̩̺̻͇͙̬̱̫̺͎̖̫̺̤͓͍͇͉͎̖̼͈͇̮͖̦̥̖͇̺̯̪͙̹̦̝͎͇͇͚̯̬̳̮̜̬͈̤̗̪̺̮̰͎̭̘̪̞̗̹̀̽̈́͘͜͠a̸̛͎̮̹̤̣͍͓̝̰̬̯̲͚̣̯̬̞͕̥̦͚̔̓͗̀̍͊̂͒̐͑̾̌̀̈̿̏̋̊̂͒͂͊̈̚͘r̶̨̨̢̡̛̛̲͓̩̟̟͎̣͖̭̲̪͉̦̯͎̲̝̺̜̰̖̮̼͎̮͖̹͓̪̲̠̜͔̗̯̜͇͓͓̦͉̙̫̭͙͍̩̮͇͉̂̇̅̓̔́̌͒̆̃͛̑̆͌͐͗̀̉̀͌̇̃͑̅͊͛͂͛̊̇̅̀̎͋̈́͌͋͊̂͐̔̐͊̑̆̈́͒̂̓̄̈̉̀̎͑̊̀͑̔̾͛̓͆̌͋̆̎́̋̈̃͌̾́́͋͐̇̀́̊̿̓́̊̊͛̑͂́̕͘̚̕͜͜͜͝͝͠͝͝͝ͅa̴̢̡͔̺͈̗̠̜̪͓͈͖̲͕̙̝̜̰̖͉̞̟̲͔̞̘͍͔̪͖͇͉̳̰͇̻͕̱͙̗̱͍͖̙͔̣̼͈̘̿̔̎͒̓͑́̍͌̀̉̈́̉͐͒̀́̈̾̏͒̊͂̏̂̌̌͐͗͆̒̀̑̆̑̊̀̏́̈́̀̄͂̾̓͌̈́͜͝͝͠͝͝ģ̸̧̡̢̧̹͕̖̤͇̺̹̱̥͇̣̮̠̻͚̤̻̯͈̩̂̋̽̇͋̅̒͐̈͒̽͛̋̒̾̑̈̍͋̓̈́͑͂̃͌̇͑̈̈̽͊̉̒͐̏́̔͐̌̔͆̆̄͒̍͑̍̆̀͊́̓̋̌͌͌̋́̀̈͗̒́̈́̚͘̕̕̚͘̕͜͠͝n̸̡̢̡̡̢̨̡̢̡̢̛̛̘̬͇͖̮̩̭̲̝̙̯̺͈̘͎͙͕̹̜̱̖̭̼͈͈̣͉̣̞̰̞̩̞̹̹̼̤̺͖͕̺̩̠̠̳̗̩͉̲̤͖̠͎̹̯͖͔̬͔̹̫̺̭͖͔̳͕̥̱̠̘̫̗͔͔̦̹͔͍̠̦̮͎̲̭͓̞̬̬̜̞̙̘̆̀̾̒̉̾͐̀́͒͑̉̀͂̓̊̀͒͛̊͛̿͒͆̈́̂̓̿̋̉̽̏́̅͂͒̎̀̄͛̉́̆͛̆̾͋̋̎̆̏̂́̋̿̓̀͌̓́̄͐͊̾̐͌̓̽̀̎̄͂́̋̓̈́̽͐̓̂̕͘͘͘̕̚͠͠͝͝͝͝ͅ ̶̧̡̛̠͈̹̬̙̣̗̺̩͓̻̤͓͓͓̜͖̭̜͓̰̪̳̖̯̠̻̔͛͗̂̆̀̋̊̒̐̏̂̊̉̏͆̍̃́̊̿͌̅͐͐͌̋̾͌̐͆̆̊͛͌̀̂͗̀̀͆͌̍͊̿̑̈́̿͒̃̊̅̊́̈́̃̀͑̿̒̈̌̀̿̿̓͛̈́͆̔͘̚̕̕͘̚̕͜͠͠͝͝͝͝͝ͅe̷̡̧̧̨̨̢̡̢̢̛̛̛̩̞̯̯̭̝͖͎̜̭͈̘̠̬̼̣̮͉̜̟͎̹̩̹̰̬̯̲̺̠̩̦̰̻̫͍̘͚̳̜̦̝̭͚̗̪̪̰̦̹̟̫̼̼̣͔̻̳̺͎̱̘̜̱̥̜͖͖̟̟̺̞̪̣̭̿͛̀̽̈́͌́̔̒͑̓̒̑̽̾͐̎̇̏̊̌̌͛̔̀̒̐̉̌̈́̄̎̌̔̔̉̈́̔̿̎̑̒̈́̀̃̎̋̅̓͌̒̈͆̆͗͑̈́͛̾̈̀̏̈́̈͆̒̽͐͘̚̚̕͘̚͘̕͝͝ͅͅͅ ̸̡̨̢̢̛̛̛͉̥̘͔̥̠̦̖̜͙͚̤̜̺̪͖̤̮̲̫̻͚͓̹̞̞̠̰̯̰͈̙̘̺̤̰͈̼̜̮͈̹̥͎̒̑̎̿̔̐̽̄́̅̽̎̎͗̀̃̐̒̎̌̏̌̒̓́̌̓̀̀̐́̿̽͊̄͂́̽͋̆͌̍̂̊̾͒́̾̌̓̃͛̅̓̑͆̿̀̏͑̽͆̉̔̎̊̉̆͊̈̊̔̂̀̾̈́͆͑̆̀̔̎͐͆̈́͒̊̑̋̒̀͘̚̚͝͝͝ͅc̸̨̨̡̡̧̢̨̡̨̡̢͍̞̟̹͙̪̤̲̼̬͙̣͚̝̫͈̗̹̳̤̠̩̣̳͇̼̞̹͖̳̥̪̫̣͎͔͕̪̗͇̲̱̟͖͓̮̝͖̰̲̏͌̈́̈́́́̕͜͜͜͜ͅͅų̶̢̢̢̨̢̛̫̼̲̬͙̞̱͎̫̭̱̞̲͍̘̝̗̟͎̮̱͚̙͈̝͈̖̳̤̻̝̳̤̹̣̠̗̺̱͚͕̠̥͎̞͍̪̻̤͇̳͍̩̗͇̦̳̣̦̟͔̪͉̟͓̥̖͎̜̱͕̭̻̳͉͓͙̯͉͇̺̫͎͒̔͗̽͑̏͋̉̽͑̋̍̉͒̉́̈́̇͂̽̀̈́̽͐̒̍̿́͒̃́́́̿̉̀̿́̀͒̾̓̆̔̈́̆͗̄̌̓̒̃̂̐̽̋̅͛̚̚̕̚̕͘͘͜͝͝͠͝ͅͅͅm̷̡̡̨̯̟̜͎̜͎̝̜̘̙̭̣̺͕̭͚̹̗̠̟̾͊̏̈́͐̄͌͐̓̈́̇͘͘͜͜͜b̷̨̧̢̨̧̢̢̢̛̛̛̛̞̫̗̫̳̦͇̱̭͓̲̤͓̣̘͙̹͙̦̙̠͇̙͖̥̬͎͈̮͖̤͍̀͊̄̀͊͋̊͂͋͂͆͂̃̀̀͌̽̓͗̋̽͆͋̃̌̈̏̑͑͒̇̽̓̑̾̈́̂̎̽̔͗͑͂̏̇́̈́̓͗̾̅́̽̽̆̾̑̃̂̋̐̀͐́̀̂̊̓͗̈́̃̊͂̓́̄́́̚̚̕͘̚͜͝͝͠͝͝͝͝͠ͅa̴̧̧̧̢̡̨̢̨̛̞̟̞̹̝̰̠̝̝͓̗̝̟̺̲̲̳̩͔̤͎͉̳̠̥͎͚̯̹͕̱̗̺̗̠̹̖̙̻̯̘̜͖̞̻̼͖̯͇̟̫̟͖̤̖͔̹̣̮̩̪͇̪̬͉̯̰̱͚̼̺̫̖̗̥̦͛̋͗̑̌́͑̏̆̽̏̈͗͑̆̓́̈́̒̓̀̅͌͐̎̉̾̽̔̌̓̅́̀̀̌̏̈́͒̈́̀̃̒̋̊̀̋͊͋͌̊̌̋̌̄̈́͛͘̕̚͜͜͝͠ͅř̷̨̢̢̡̡̢̨̧̨̧̡̡̨̡̧̧̡̛͈̬̦͚͇͓̥̩͓̯̗̭̟̞̱̦̼̲͔̙̞͔͈̠̞͉̮͔̫̣̼̪̰̙̬͖͎͚̗̗̰̳͇͚̩̩̦͍͓̼͎̞̺͈̟̗̜̼̫̙̝͎̟͍̗̻͉̲̰͚͚̩̰̙͚̗̜̲̫͇͖̒́̒̾̈́̑͊̐͐̆̉́̏͌͌̆̎̃̆̔̃̉̆̈͐̃́̈͛̊͋̔͛̿̍́̑͒̍́͛̅̃̀̍̒͊̉́̔͊́̂̍̎̉̆̒̆̇̃͗̈̌̂͒́͊̊̀̂͆̏̈̉͛́̉̔̔̈́̆̊̃̄͆̎́͘̕͜͜͝͝͝͝͝͝͠͝͝ͅͅͅį̵̛̛̤̻̝̤̙͈̪̫͇̻͇̟̱͇̻͔̅̾̓̎̔͑̐́̽̃͌͒̃͋̈́̾͑̓̅̒̄̎̓̌̓̓͐̍̐͆̀̄́̅̇̃͐́̏̒̆̓̌͌͂͗̐̂̓̒̂̊̅͗̌͌͋̂̇͌͒͗͗̒̊̊̀̃̆͒͛̀̉̅̆̒̾́̀́́̓̀̓̋̕̕̕͘̕̚̕̕̕͘̚͝͝͝ͅş̵̨̨̨̨̨̧̨͎̙̩̪͕̮̜̰̭͓͔̣̻̗͉̞͓̻̠̮͈̬̫͔̫̠̬͍̖̻̪̫͇͕̟̳͔̪̪̼̣̦̖̱̠͓̻̻̣̩̻̪͍̬̦͔̘̩̣̫̘̊̒̑͋̃̿̀̃͂͂̆͛̔̾̾̃̔̌͑̆̋̎̾͗̌̇̋͆̾̂̎̔͗̈́̀͗̈́͋̃̈͛̓̈́͐̐̌̒̈̀̽̏̊̂͑͑̿̊̋̊̎̕̚̕͜͝͝͝͝ͅͅc̸̨̢̧̨̡̧̡̨̡̢̢̜͖͙̩̺͖̟̘̤̗̤͍̙͕̥̭̬̲̥̝͈̬̙̺̣̪̼̞͇̻͍͇̜͖͇͚̥̝̤̼̗̘̭̣̙̼͈͇̥̭̭͍͎͇͌̃̓͑̅͛͌͋̂͒͒͐̔͂͑̀̓̽̀̐̽̓͐̿̓́͜͝ͅ!')
        return CONTINUE
    elif iterations == 1:
        context.bot.send_message(chat_id,
                                 text='D̴̨̨̢̢̡̧̢̗͖̱̩̳͙̣̺̙̦͖̩͙͕͈̦̱̯͇̟̺͇͕̬̬͕͓̣͓͇̥̣̦͚̯̗̙͚̬̦̲̮͇̭̭͇̫͈̠̻̠̱̣̞̳̙̣̱̹͔̰̪̤͔͖͉͙̤̞̳͇͔͔̅ͅͅͅa̴̡̡̧̡̨̨̢̧̧̢̢͍̙̜̲̩̬̤̝̞͔̦̳̗̦̦̱̤̱͙̱͖̖̰̲̦̖̭̫̯̤͓͔̱͇̤̥̙͖̗̳͍̬̥̜͓̰̙͙͇̱͚̯͉̫̹͖͈̭̹͇̞̪̗̳͎̯̘̹̼̱͔͕͓̼̙̦͍̳̟̗̦̝̼̫̳̟͙̖̞̬̥̲̝̥̞̜̤̗͈̪͚̱̥͓͔̥̖͉͈̟̘̗̪̜̲̐̎́̃̈́͒̇̅̏̾̀̽̏͗̋̅͌͆̒̌̉̓͒̑̿̐͋͆͆́́̓̚̚̕͘͜͝ͅǰ̵̡̧̢̢̨̨̧̧̢̨̧̨̛̭̮̯͚̰̪̻̩̭̼̖̘̣̖̯̩̤̖̘̜̙̳̤̩̺̥̥̳͙̺̺͔̰̪̥̞̭̻͚̜͈̹͙͙̰̹͎͓̲̬̼̣̩̟̤͓̝͔͉̠̪̗̻̤̲̤̱̭̦͕̝̲͇̞̝͓̦̩͇̣̠̝̗̯͚̘̠̝̯͎̺͖̣̈́͗̀̍̉̃͌͗̄̆̾̾͛́̈́̀̒́͂̊̌̾̃͐̒̊̏̀̊̍̾̓̒̑͂̉̐͋́̈́͛̀̌̇̄̀̍͋̿̽̾̾̍̈́̃͌̈̌͐̎͗̃́͆̄́͆̍̓̅̈́̋́̈́̊̐̌̓̋͊̇̽̅͛̀̊̓̾̈́̈́̾͐͐̓̆̑̕̚̕̕̚̚̕͜͜͜͝͝͠͝͝͝͝͝͠ͅͅͅe̶̢̧̡̡̧̡̨̢̨̢̧̢̢̜̪̻͎̣̦̱̘̥̰̫̫̹̼̜̟͖͚̙͎̱̫̯̱̼͍̝̪̗̬̲̥̞̼͓̬̖̭̳̳̟̥͉̜͙͚̜̭͖͚̙͙͎͔̹͔̭̪̞͎̳̬̠̯̲͓͓̼̰̼̘͙̭͙͉͇̳͚̪̲͉̤̭̯̬̳̬̥̟̜̗͉͇̞͚͖͓̮͖͕̞̻̒̂̎͛̍́̄̒̐͋͆͂́͂́͒̍̋͊̒́͑̑̌͑́̑̔͆́̐͒̎́̋̐̌̐̽̅͊̽͐̆̅̒́̓̄̈́̿̏͑̂̍̈́̀̿̈́͊̏͌͊̀́̔̾͗̐̿͘̚͘͘͜͝͠͝͝͝ͅͅͅͅͅ,̷̧̢̛̛̛̘͙̥̮̲̺̗̊̔̌̒̐̐͐͗͗͌̒͌̽͆̑̆͗̈́̀͌̓͌͑̋̃̀͗̐̾̉̂̊̇̐̾̾͋́͂͑̽̓̓̊̈́́̆̒͌̒̊̿̆̎͛̊̄̉͒̇̉̀̈́̒̀́́͛̒̈́̅͌̑̉̿̏̾͛̽̑̈́̆́͌̅̎̀̀̊̽̂̏̍̆̅̑͑͂͘̕̚̚͘͘̚̚̕̚͝͝͝͝͝ ̷̢̦̬̤̲̽̽̔̈̅͜ḑ̷̨̡̧̢̧̧̠̱̥̜͉̱͉͙̳̻̪̱̭̜̘͕͓̻͇̻̝̳̪̰̺̯̙͇̙̜̺̘͉̝̖̜̠̱̘̞̫̪̳͖͔̮̲͔̪̻͚̫̟̟̠̝͈͉̭̹̖̖̟̤̠̖͍̘̘͉̲̜͖̮͕̞̟̀̀̄͜͜͜͜͜ä̴̡̧̛̛̛̛̬͔̝̭̭͉̖̟̹̝͖͔̣̫͖̻̳͖̩̣͙̼̺̬͈͔͓́̾̇̾̽͒͛̈́͋̽̆̂̿͐̈́͌͛͋̍͊͌̎̓̐͛̋̏̿͗͆̍͑͆̓̾͊̉̒̓́̍̐͗̔͒̓̅̐̐̌̊͛̈͌̐̐̒̉̈́̆̔̚̚͘͠j̵̡͙̝̠̦̬̫͚̘̳͖̼̙͖͚͍̥̲͇̺̮͔̬̪͈̮͉͍̦̞̫̤̬͖̲̞̳̠̪͉͈̟͚̱͑̅̄͗̾͂͊̐́ͅȅ̸̼̤͚̮̗͙͇͔̱͔͎̪̥͍̰̖̀͌̽̓̒͂̇͘ͅ ̸̨̡̨̡̨̨̨̢̢̢̡̧̢̛̛̛͙̬̭̜̠͉̣͚͈͕̱̱͍̫͍̳̫̱̺̬͇͓̩͍͕̠̳̰̖̟̦̦̻͚̯͔͖̯̠͙̞͈̼̪̤͚͈̥̥̠̩̪̪̥̬̰̥̲̙̗͓̮̩͎̹̤̖͚̯̩̟̲̤̜̻̠̜̈͂̑́͗̈́̂̂̓͛͗̅̈́̈́̿̈̔̾̌̿́̀̎͗̏̑͂̃̈̎͛̓̇̔͂͒̈́̒͆͛͊͛͗̋͋̍́̍̈́̓̋͑̋̌̐̎̿̎́̐̈͋͆̽̆̽̍͊̂̐̎̈́͘̚̕̚̚̕͘͜͜͜͠͝͝͠͝͝͝ͅͅe̷̢̢̧̛̛̛̛̺͍̝̹̪̭̥͖̣̻͎̯̮͔̻͉̩̟̝̯͚̘͈̤̹͖͙̖͈͖̲͒̔̇̋̓̒̍͆͆̈̌̄̔̏̾̂̊͋͋̀́͂̈́̋͛̐̓͆͊͊͑̈̾̍̆̿̇͊̋͑̈́́͋̔̔̎̔͛̿̓͛͂̿̀͋͌͑̀͋̑̇͆̅̓̈́̈́͂̀͑͌̕͘̚̚͠͠͝͠͠͝͝͝ ̷̧̡̢̡̢̡̥̯͕̝̫̺̠̭͚̲͚̣̝̻̦̱͙̠̙͎̹̥̦͕̗͉̗̩̭̼̱͙̭̣̞͙̤̰̯̻̩̗̿̆͋̔͗͐̀͆͂̇̇́̇̀̂̉͂̏͆̓̌̒͋̈́͘ͅḏ̵̨̨̡̨̧̨̡̢̧̛̹̝̗̖̫̞̺͙̮͓̩̻̼̟̟̜̭̘̜͙̮̯̫̣͔̟̲̙͖̺͈̙͈͎̗̹̫̹̰̱̯͚̰̖̙͓̟̝͔̲̤̲̙̫̖̗̜̘̬̜͎͓͉̞̪̝̯̙̗̠̦̙͓̹͉͚̗͉̳͈̫̫̳͈̙̥̤̰͖́̉͋͐́̀͆̔̏͛̽͛̋͛̿̈́̑̅̽̅̃͆̀͑͆̑͆̾͋̋͆̈͛̚͘̕͜͝͝͠a̴̛͍̟̰̜̟̙̮̭̅̆̌̐̾̐̍̿͌̑̅́̓̄̄̃̔̊̎́̈̈̅̔͂̄͛̿̽̽̂́͛̀̓̈͐͌̈͆̇͛̀̿͛́͒͋̐̌̍͑͊͌̔̉͊́͆̈́͐̽͑͛̈́͊̓̆͐̉̄̆̾̉͆̌͂͛͑͆̄̇̊̀̿͌̈̍̿̾̾͗̾̿͐̌̑̈̈́̎̏͆͒̏͑͆̕͘̚̕̕̚͘̚̕̚͘͝͠͝͠͠͠͠͝ĵ̴̛̩̙̖̞͚̳̖͇̠̟̺͕̲͈̙̖̪̬͔̬̦̤͙̜̿̈́͋̍̾̿̾̇̃͒̅̔̃̓̓́́͛̾̓̓̃̈́̽̓̒̑͐̀̐̽͒̆͌̌̒͂̅͋̈́̾̈́͂̉̃̑̏̀̍̽̓̒̈́́̾͂̓́̓́̃̿̏̊͌̔̋͆̆̅́̒̎͊̈́̾̽́̏̒̔͐̾́̏͛̑̐̍́̈́̏̋͆̍͊̈͗͒̿͒̀͒͆́͒͘͘͘̕̚̕̕̕͘͜͝͝͝͠͠͠͠͠ͅͅȩ̷̢̨̡̡̨̢̨̪͉͔͙̹̺͙͕̱̯͍̙̹̺̯͙̤̯͈̫͙̟͓͉̻͚̫̘̣͙̬̫̺̜̳̭͍͙̞͎̼͉̼͔̱̜̦̪̯͍̖̤̮͈̣̤̻̻͉͖̱̬͓͉͕̗͚̺̞̙̪͙̥̱̈͐̄̈̓̽͆̍́͌̄̾̓̓̀͛͌́̈́̏̇̑̈́͋̉̈́͐̋͆̒̇̂͆͌̎͐͂̇̄̎̎̈́̋̉̓̽͋̚̕͘͘͜͜͝ͅͅ')
        context.bot.send_message(chat_id,
                                 text='l̵̨̧̡̨̡̧̧̗̙̜͎̬̻̬̖̠̱̹̞͇̹͇̗̦̼̟͇͈̳͚̩͓͉̭͚̟̭̥͓̙͎̠̰̮͇̙̭̱̘͈̳̼̍̔͆͑͛̽̃́͛̈́͊͊̑̈̄̐̓̾̿̇̿̀̾͌̋͆͌̍̈̓͛̈́̎͌̍͐̈́͜͜͠͝͝͝ͅͅa̷̡̡̨̧̢̡̛̛̰̦̪͇̖͕̭̟̩͓̣̥̞̲͈͎̳̹̺̘̻̭̲̣̭͙͇͉͙̻̱͍̙̽̔͆͆͋́̾̅́̇̌̑̈́̒͑̊͛̀͑̐̃̍̐̇͛́̒̂͌̐́̋̈͛̐͂͒͐̑̈́͛́́͑̅̓͋͐͒̔̌̋͊̆̈́͋͆̀̋͒̈̈́̐̅͒̐̔̈́̈́͛̊́̔̅̇̀̇͌̄̔̿̽͌͋͌̅̉̚͘̕̚͘͝͝͝͝͠͝͝͝͝ͅ ̵̛̺̯̱͔̞͔̝͍̹͍͕͐̓͋̇͛́͆͒̉̃̀̅͌́͗͆͑͊̿̔̔̈͋͊̓̆͊̉̇͌͊̓́̇̑̆̂̉̅̔̅͊͘͘̚̕̚͝͝͝͝͠͝͝ç̴̢̧̨̨̡̢̡̡̡̨̢̡̢̢̛̹̰̳̣̦̲̦͓͉̥̟̞͍̟̻͔̠̳̳̘̣̯̖͇̹͇̣͈̤̠̼̹̱͈͓̼̘̺̤͎̞̠̩̜̝̦̺̺̮̝̺̙͚̫͇̣̱̟̮̙͈̟͇̱͎͔̣̯͙̜̱̭̟͔̱̥͓̣͍̖̺̟̠̖̺͖̮̯͙͇͇̦̞͓͔͖͕̣̲̥͕͈̙͙͈̙̖̝̼͙͕͛͊͗̅͛̈͛̿̒͆̂̈́̑̾̈́͐͊̃͗̃͑̎̂̂́͂̓̔̓̈́̍̊̊̏̌̎̊̏͒͌̃̌̑̊̽̔͂͗̚͜͝͝͝ͅͅi̸̢̧̡̡̢̨̨̧̢̧̧̡̢̨̨̖͉̺͔̲̱̯̤̜̣̥͔̩̱̩̼͓̳̺̤̥̗͉̗̘̦̫̘̝͍͇͎͙̻̣̭̦̯͈̩̪̞̯̙̝͖͔͕̣̫̻̰̟̭̯͇͎̱̲̝̳̯̼̼̹͓̲̺̰̺͖̪̦̭̬̬͇̰̦̳̟͕̦͙̘̰̱͕̯͔͓̠̼̜̙͉̝̮̬̼̗̘̐̈́͑͌́̈́̇͐̎̽́̾̔̃̌̉͌̐́͆͊̑͒́̾̊̄͆̀̕̕͜͜͜͜͜͠͠͠͝ͅͅp̷̢̛̯̳̘̖̰̫͙̗̥̘̲̲̼̪̜͈̥̜͇̩̺͎̑́̿͗̒̂̽̈́̿͒͊̈́̑̑̀̌̉̌͐͒̒͗̀̍̎̅̂̈͒̋͂̓̇͊̈̒̈́̾̄̇̊̄̈͗̈̔̅̅͑̽̊̀͋̄̈́̈́͂̌̆͐͊̎̌͌̓̓̅͗̕͘͘͘͝͝͝͠͝͝͝͠͠ͅǫ̴̨̧̡̢̡̛̛̦͓̘̜͇̺̫̜͓̭̬͕͕͍̱̣͔̙͈̦̰͙̖̲̹̼̗̺̼̱̗̰͓͇̠̥̬̲̠͎̬͈͙̼̩̤̠͍̞̣̀́̅͆̓̈̒͐̏̑͂̿̓̏͆̊̅̿̄̂͑̉̉̊̐͂̏̀̃̀́́́͊̔̏̀̓̋͂̿̊̀̔̅̀̈̊̍̊́͋͆́̎͋͌̑̃̀̽̍̄̽͐̓̏̍̑̒͐̀̏͐̄́̂͊̍̚̕͘͘̚̕͘͘͜͜͝͠͝͝͠͠ͅͅl̸̡̡̧̢̨̢̨̛̰͇̹̙͔̞̻̞̬̪̞̝̫͚͖͙͕̯̺̫̳̺̫̦̰͔̘͚͚̺̺̤̦̭̗͚͓̤̯̮̬̹̲̦̫̦̦͉͔̝̩̺̙̮͆̓͐̽̍̋͐̽̏̉̓̄̓̏͋̒̒͛̄̏̅͐͒̔̂̽̕̕̚͜͠͝ͅͅl̶̢̨̨̡̢̢̨͖̮̗̖̹͈͔͙͓͕͙̮̙̳̻̞̫͓̙̳̺̭̲̰̪͍̬̹̖̝͉̩̝̫͉̲̺͎̗̖̠̲̲͇̭̰͎̯̞̮͉͖̞̝͕̺̖͉̗̜̼̘̞̫͎̩͖̪̲̺̩̬̮̙͙͕̣̟̩͔̬͉̫̖̤͉͚̹͕̠̹̦͇͙̙̮̮̟̳̺̙̮͈͇̣͑̍̂͛͆͂͆̇̂̅͛͌̈́̆̾͒͆̈́̄̅̐̽̈́̊̐̑̀͊̒̐͆̐̂̉́̀̆̌̈́͋̿͊̾̒̈́͌͐̌̽͊̓̾̍͊̑̂͛͛̈̓́̈́̅̆̾͛̇͊͂̓̓̅͐̑͐̔̽̾̌́̇͊͒̐̅͒̈́̀̄͊̕̕͘̚̚̚͘͘͜͝͠͠͝͝͠͠ͅͅë̸̟̩͙̝̘̣̣̬̙͕̖́̓̊̌͂̈́̈́̇͆̔̎̓̀̈́͗̾̀͛͋̃͑̽́̋̿́̈͊͒̾̆̌̎͛̃̑͊̀͌̈̓̃̏̄͐̑̇̇͂̕͠͠ͅ ̵̡̨̨̢̡̧̨̢̢̛̛͚̮̱͖̦͇̫͖̻͕̬̙̼̲̖̭̹̲̪̙̗͖̠͉͇̤̳̤̘̯̝͓͚̞͚͍̠̯̞̮̦͍͉̬͔̤̯̭̺̣͎͚͓̤͖̟̥̰͉̻̹͙̠͔͎̬͉̫̝͉̩͎̠͉̣͔͖̮̤̘̙̬̙̪͔͈͎̞͎͓̲͈̟͕̞̪̥̜͓̩͖̫̣̫͑͊̆̈́̊̏̇͋̉̋̒͗͐̌͌͌͆͋͗̔̅͌͛̽̎̇̎̇̑̑̃͋̐̋͂̆͐͑͌̋͋̑͗̋̍͑̓̈́̀̎͒̀̽͋̅̑͊̒̈́́̊̐̊͑͂̾̉͗̃̿͑̉̉̓̑̾̓̐̄̇̂̈́̆̀̄͐͗̂̚̕̕͘̕̚̕̕͜͜͝͠͝͝͠͠ͅͅd̴̨̢̡̢̡̧̨̤̳̻͖̠̣̣̝͔̟̘̘̫͈͍̰̜̬̱̫̰̦͙͔͔͚͎̫̼̩͍̝̭̗̘͓̥̺̬̲̲̺̭͓̖̝̙͉̠̲̭͙̼̠͔̮̠̖͚͉͓̙͉̖̖̯͉̯͎̤̻̠͕̫̪̪̬̼͙̱̩͉͉͕̱̙͉̰̱͇͎̱̱̖͙͉̺̪̬̘̓̂̃̉̍̂̈̂̅̆̿̀͂͑͂̄̒̒̄̇̓́͋̌̈́̋͌̒͊͘̕͝͝͝͝ͅͅͅi̶̧̡̧̡̢̧̢̯̜̩͕̙̤̞͎̣̘͓̥̹͍̼̻̣̫̻̟͙͙̳̼͚͓̗̳̬̙̼̥̝͉̪̱͔̤̲̙̜̘̦͎̥̬̯͚̘̪̰̲̗̣̮̫̪̳̠̣͉̻̬̰͕͓̻̰̫̝̹̤̳̖̳̳̲̼͚̝̙̩̹̪̬̬̒̄̍̔̑̌̀̄̀̃̎̚͘͜͜͝ͅv̶̨̧̡̢̡̡̡̨̢̧̛͔̜̰͚̲͎̱̘̖̼̭͖͙̺̱͚͈̰͕͙̠̤̻͍̣͇͖̫̠̼̥̜̙̙͓͎̞̞̞͓̮̜̞͓̩̜̖̻̩̠͓͙͔̭͖͕͈̬̹̖̜̪͓̞͔̺̪͍̰͍͍͔͓͉͉̺͇̫̥̹̱̭͇͙̙̼̘̘̥̗͍̳̗̻̥̻͕̣̫̯͋͒̄̍̅͐͌̐̊̐̆̀͑̀̈̋̈̀̈́̀̿̓̚͜͠͠͝͠ͅͅͅͅͅę̵̢̨̧̢̡̡̡̧̡̧̧̡̨̡͍̫͓̱̦̼̤̹͈̯̳̺̰͓͕̹̤͉̩̠̖̦͉̤͓͖͈̥̗͙̠̫͕͍̙͙̮͎̻̲̠̥̪̗͎͇̭̳̞͓̥̗̼̜̟͇̟̣̲̻̻̰̝̙̩̘̳̙͉̤̬̞͉̠̜̹͔̫͖̲̙͈̳̖͎͙̥͓̘̳͇̺͎̯̝̭̙̀͊͌̀͊̀͆͌̑̅̊̂̀͌̋̎̌̀̅̈́͒͗͘̕͜͜͜͝͝͝ͅͅͅͅn̴̛̛̛̛̛͍̲̻͚͖͇̲͉͇̫̯͎̂͒̓́̋͌͊̌̏̏̋̓̂͂́̇͒͋͑̌̂̊̋̄̀̐́̒̅̈́̾̊͆̄̋̉͋̏͐̃̀̈̏̄̈́̃͒́̍͊̋͒͗̂͐̿̏̅́̄̈́͑̊̄͛͌͛͗̑̾̔̑͊̈͆̄̆̐͋̓͒͊̾̂́̆̀̏̍́̀͆̀͆̂͆̐̓̅̚̚͘͘̕͝͝͠͝͝͝d̸̡̢̢̢̧̧̨̢̛̛̛̛̺̹͖̩̭̫̝̭̦͖̭͖̪͖̹̩͈͉͓̯̣͔͙͔̫̱̮̺͎̤̦̤̰̼̜̯̲̘̦̱̞͖͓̠̭̫̯͚͉̻͓͙̺̜̯͚̰̱͑̄́͆̋̏̈́̔͑̾̃̃̅̒͒̅̌̇́̊̈͐̀́̏̀͛̇̈́̾̇̄̑̈́̃͊̀́͊̈́̈́̆̈̀̈́̈́̈́͋̓̐̾̌̀̎̂͐̈́̑̔̈́͂̓̀̊̅͌͛͌͊́̆̉͂͋͑̈́̾̊̓̏̑́͒̃̐̚̚͘̕̕̕͜͜͜͝͝͝͠͠͝͠͝ę̵̧̢̧̨̡̣̞̬̭̣̟͔̜͖̪͍̫͔͓̘͈̯͖̗͓͉͖̦̪̤̼̖̼͍͍̙͚̯̭̜̘̱̫̫̤̹̖̹̬̮̯͕̝͔̣̰͔͓̹̞̳͕̯̟̘̥͙̫̺͉̩͕͍̙͎͍̘̱̭͙̥̠̺͎̘̦̫̞͎̺̻͖̣̽̾̽̈́̐̉́͂̔̔̊̅̀̑̊̃͊̓̋̿̀̈́͌͋͌͋͛̑͋̆̋̔̽̐̄́̉̎̈́̀͑̌̔̾̾̂̾̓̃̃͑͌͆̅͊̾̽̋͑̽̚͘͘͘͜͜͠͝͠ͅ ̸̢̢̢̧̢̢̛̛̛̘̻͈͈̞̠͚̜̟̫͈̠̼̗̜̖̠̺̼̤͇̥̣̺̼̳͇͐͆̇͒͐͐̃́̂͂̆̏́̌͐̏̌̈̏̄́͑͌̓͆̍̆̈́͑͐͑͗̍̽̋̒̿́͐̆̂͑͋͐̊͗̂̑̐̈́̀͂́͛͌̃̊̉̀̌̂͛̄̋̕̕͘̚͝͝͠ą̵̧̢̨̡̡̢̡̛̛̣̹̺̪͓̤̤͉̰͔̮̱̩͎̱̤͕͇̱͕̤̟̗̼͎̬̳͕͉̲͇̙̬̰͖͖̝̦̜̲͚̲̤͓̤̦̰̦̗̪̲͇̮̣̯̟͎̥̱͈̠̻̻͔̜̝̠̼̥͎͓̲̩̯͎̬̹͎̯̹͖͚͉̞̜̟̼͙̳͖͕̥̀̅̈͛́̇͑͌͊͘͜͜͜͝͠ͅͅj̵̢̛̛̙̘͓̭̜̱̝̪̰̻̹̗̰̜͙̩̦͖͚̙́̿́̋͂̀́̍̈́̍̐͌͑̀̑̋̀̀̀̅̊̒̃͋̑̇̈́̊͒̿̈́̈́̆̀̊̈́̂̄̓̆̃̀̉̑̑͌̆̈̉͗͊͌͗̾̃͂́̆̒̑́͂̉̆͆̆̾͋̽͊͌̈͋̐̄̏̈́̀͒̽͆̈́̋̎͗̽͒͆̅͑̽̌̈́̄͛̉͋́̈͘̕̕̕̚͘̚͜͝͝͝͝͝͠͠͝͝͠͠͝͠͠e̵̢̢̧̨̢̛̛̛̻̺͈͇̮̲̜̤̼̝̜̣̪͎͇̤̺̘̼͈͓̪̻̱̹̰̘̫͓͚̲̪̦͕̯͖͓̮͇͕̖̼̘͔̹̠̯͓̤̳̣͇̰̰̥͙̩̤̲̪̝̬̭̫͇͉͉̞̲̊͒̓̽̋̃̋̑̑̀͛̎̑̆̀͊͊̆̓̈́̾̉̃̎̾̅̎͗͗͆̉̽͑͂̊̉̾͌̄̂̓̇͐̈́̑̈́́͂̋̂̽̓́̈́̉͂̄̽̄̑̑̓̈́̒̂̇̽̔̍́̌̋̅̒͐̆̄̃̊̊̽̒̃͘̚̕͜͜͜͝͠͝͝͠ͅͅͅͅͅ')
        return CONTINUE
    elif iterations == 2:
        context.bot.send_photo(chat_id,
                               photo="https://raw.githubusercontent.com/naelvis/botgiornissimo/master/buongiornissimo/hamtaro_ctulhu.png")
        return CONTINUE
    else:
        context.bot.send_photo(chat_id,
                               photo="https://raw.githubusercontent.com/naelvis/botgiornissimo/master/buongiornissimo/bottonbirthday.png")
        return telegram.ext.ConversationHandler.END


def augurissimi(context: telegram.ext.CallbackContext, update: telegram.Update = None) -> int:
    if update is None:
        job = context.job
        chat_id = job.context
    else:
        temp = update
        update = context
        context = temp
        chat_id = update.effective_chat.id
        if not update.message is None:
            user = update.message.from_user
            text = update.message.text
            chat = update.message.chat
            if user.id != tokens.gatto or chat_id != tokens.gruppissimo:
                context.bot.send_message(tokens.gatto,
                                         "I received a message from user ({0}, {1} {2}, {3}).\nContent: {4}\nChat type is {5}, chat title is {6} and chat ID is {7}".format(
                                             str(user.id), str(user.first_name), str(user.last_name), str(user.username), str(text), str(chat.type), str(chat.title), str(chat.id)))

    [day, month] = [datetime.datetime.now().day, datetime.datetime.now().month]

    if (chat_id == tokens.gruppissimo and [day, month] in Events_daymonth.values()):
        event = next(key for key, value in Events_daymonth.items() if value == [day, month])

        if (event == "compleanno_bottone"):

            if update is None:
                payload["iterations"] = payload.setdefault("iterations", 0)
                context.bot_data.update(payload)
            else:
                if update.message.from_user.id == tokens.bottonissimo:
                    context.bot_data["iterations"] += 1

            iterations = context.bot_data["iterations"]

            auguri_bottone(context=context, update=update, iterations=iterations)

            if (iterations > 2):
                return telegram.ext.ConversationHandler.END

        else:
            return telegram.ext.ConversationHandler.END

def done(update: telegram.Update, context: telegram.ext.CallbackContext) -> int:
    update.message.reply_text("If you are reading this, something went wrong...")
    return telegram.ext.ConversationHandler.END
