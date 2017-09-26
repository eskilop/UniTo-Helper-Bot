### UniToHelperBot for Telegram

![Image](http://www.eskilop.it/art/unitohelperbot/scrot/screenshot-1.jpg)

## Building
First ensure you've installed python 3.x on your system. Then, you have 
2 options to install PyTelegramBotAPI:

* Installation using pip (a Python package manager)*:

```
$ pip3 install pyTelegramBotAPI bs4
```

* Installation from source (requires git):

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python3 setup.py install
```
then, once you have installes pyTelegramBotAPI on your system you might want to configure your own bot, so:

* go to [@botfather](http://telegram.me/botfather) and create a new bot.

* once you created copy the http Api key and paste it into ```api_token``` in ```options.py```

Note that unless you modify the code, you must also insert an id for the ```log_channel```, and an id for ```super_user```

make sure to allow execution of the botstarter.sh by typing:

```
$ chmod +x botstarter.sh
```

So, now you're ready to go, just type in from your working directory:

```
$ ./botstarter.sh
```

Your bot should now be up & running, you can check it by chatting with him in telegram.
Have a look at options.py file, there are a bunch of parameters you can customize.

If you see some strange behaviour in the bot feel free to open an issue.

## License
-------------

    Copyright 2016-2017 Eskilop

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
