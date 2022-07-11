 

В Биткоин-пространстве продолжается дискуссия на тему пользовательского опыта _(UX)_. Биткоин до сих пор выглядит странно, неуклюже и порой сложно. Основной причиной этого является то, что Биткоин и его составляющие (сеть, протокол, криптография, язык программирования) действительно странные, неуклюжие и сложные. Таким же был и, возможно, до сих пор остается интернет.

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/Oh2YB--e8_C06mR7Bu057J44uhJvZI4W19IuYL6lGADS4RcdzFPjALsD8LqVMJe9PLhYvlTgXuFrIiEW3ZregsnxtxcAmGR1GeaHXGGl29TszR0--nOeO--OfsSAnfxEB_e9XtAN=s0"/><figcaption><em>До LNP/BP и TCP/IP имел место IPX/SPX</em></figcaption></figure>

Причина, по которой интернет больше не кажется таким неуклюжим, двояка: (1) люди привыкли ко многим новым понятиям, которые принес с собой интернет, и (2) бесчисленные абстрагирующие слои облегчают взаимодействие с базовым протоколом. Сопутствующие технологии, такие как _plug-and-play_, помогли сделать работу пользователя еще комфортнее. Дни установки номера IRQ вашей сетевой карты вручную уже в прошлом!

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/P3FjRRJ6DJsTuq2xc-sREtgP7OTK5sf6BPhRn3R-bu3xYtjlA7WOThdxvNrRK1oAbWV6pbX3jA5EVOjk4fW1u0n2peO5kFi_k7SejXfhg_7WLMH7xaUxr2K7At_T6RJzsDKL-aVP=s0"/><figcaption><em>"Что такое IRQ?"</em></figcaption></figure>

Как и интернет, Биткоин — это развивающаяся экосистема. Имейте в виду, что многое уже изменилось к лучшему. Например, первый кошелек, который поддерживал QR-коды, был выпущен в 2012 году. В том же году были предложены XPUB ([BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)). Сид-фразы ([BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)) были предложены в 2013 году. [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) (HD-кошельки, они же "аккаунты") появился в 2014 году. SegWit ([BIP141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)) был предложен в 2015 году и — после продолжительной гражданской войны — активирован в 2017 году. Сегодня большинство воспринимает QR-коды и сид-фразы как должное, не осознавая, что они не всегда были частью Биткоина. Я уверен, что некоторые воспринимают сеть _lightning_ (появившуюся благодаря SegWit) также в порядке вещей.

Я считаю, что все эти “закулисные” технические улучшения безумно важны для UX. Без них взаимодействие с сетью Биткоин показалось бы адом. Сид-фразы? Простое восстановление кошелька? Сеть lightning? Забудь! Тем не менее, все эти улучшения безумно технологичны и требуют технического обсуждения. Не за горами новые улучшения (Шнорр, Тапрут и [многие другие](https://bitcoinmagazine.com/articles/2020-and-beyond-bitcoins-potential-protocol-upgrades)), так что готовьтесь к тому, что обсуждения в Биткоин-пространстве останутся техническими еще довольно долго. Ассоциируйте Биткоин с "Linux", а не с "iPhone".

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/FQB2bxvJXxcfE353hCFuoWxnVsEeBRng_EDwhl0cvGC0Hcd0i3IRMuSKT3R6EabGBl_ZV4ShGyegO3C1FMMVEY4sREtgIWjOUIhlq5eH0K8jAmBoiSgB_0g1z_XKwlYQJcUlgMWq=s0"/><figcaption><em>Git был иным в 1998 году</em></figcaption></figure>

Кстати об айфонах: Наблюдается напряженность в отношениях между изобретателями и фанатами айфонов и компании, ожидающими, что все будет работать идеально и будет супер-интуитивно, причем ПРЯМО СЕЙЧАС.

Ну, прямо сейчас идеально работать ничего не будет. Точно так же, как во времена зарождения интернета нужно было знать, что такое IP-адрес и как работает коммутация пакетов, так и сегодня нужно знать, что такое XPUB. DHCP, по сути, решил проблему IP-адресов, так же, как Google расправился с проблемой "ввода точных URL". Всё это придет и в Биткоин. Просто это не произойдет в мгновение ока.

Базовый протокол, вероятно, будет постепенно “отвердевать”, так же, как и TCP/IP окреп со временем. Как только базовый уровень будет достаточно оптимизирован, большинство инноваций начнут происходить на более высоких уровнях.

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/K9iDcBmiUJBnqPDOFzT1qGKCyuK3tLgRrTU55B4kurIy82fX2S-kzPnUztA9p3pARqAt_DliiSiD8MfiPhkgTjq06i5OoXG4yhOQCASqbC9OXOZyEAnNCR9lll15xEWsG_070dIx=s0"/><figcaption><em>Круто. Теперь, когда мы разобрались с пользовательским интерфейсом, давайте обновимся до IPv6.</em></figcaption></figure>

Я считаю, что те, кому разработка знакома не понаслышке, просто устали от слов "это так сложно, все должно быть проще". Да, мы согласны, все должно быть проще, и мы упорно работаем над тем, чтобы это было именно так.

Некоторые из них создают простые в использовании продукты (Strike, Casa, Coinkite, Samourai и т.д.), другие работают над улучшением протоколов, чтобы в будущем все было проще и лучше (спасибо Core-разработчикам!), третьи работают над более широкой экосистемой (Raspiblitz, BTCPay Server, Umbrel и т.д.), а четвертые — над просвещением и распространением информации(Nakamoto Institute, Bitcoin-only, Bitcoin Translated), чтобы больше людей могли принять участие в проекте и помочь сделать Биткоин лучше.

Со временем люди привыкнут к понятиям, от которых нельзя абстрагироваться. Я убежден, что все станет проще, наподобие того, как и подключиться к сети интернет сейчас легче, чем это было в 1995 году.  

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/lXinHGZ3fWHzhVDXUUb8f-cNliWgx_6Hc8_RfLS2bkAjuKQQKgjEDgDGPK5k-ejnV7j_v8-2r75gzngf24_5QcAVBZXDgGrC-mLhdO_BxT8Q5QuHFbiktNtIgo2R1rDcDs4I-IxA=s0"/><figcaption><em>Делай хорошие вещи</em></figcaption></figure>

Биткоин — это новая парадигма, как и интернет в свое время. Точно так же, как нельзя было избавиться от адресов электронной почты ("Что это за странный знак @?") и URL ("Что такое http/https/ftp/ssh?"), на сегодняшний день нет возможности обойти биткоин-адреса, приватные ключи, и, как вы уже догадались, XPUB.

Некоторые концепты очень важны, отказ от них с целью получения лучшего UX, может привести к фатальным результатам. Откажитесь от коммутации пакетов ([сетевой нейтралитет](https://www.battleforthenet.com/)) в сети интернет, и вы уничтожите то, что изначально сделало интернет великим. Пожертвуйте самостоятельным хранением монет (или созданием учетной записи посредством математики, или нейтралитетом, или множеством других вещей) в Биткоине, и вы уничтожите то, что делает его великим в первую очередь. Само собой разумеется, что самостоятельное хранение всегда будет хуже с точки зрения UX, по сравнению с тем, чтобы позволить кому-то другому хранить ваши монеты. Точно так же, создание собственного домена и хостинг собственного сайта всегда принесет больше хлопот, чем создание страницы в Facebook. Это всегда вопрос компромиссов.

Сосредоточение внимания исключительно на максимизации UX может привести к неоптимальным результатам в долгосрочной перспективе. Просто сравните Facebook, TikTok и огороженный сад iOS с не требующими разрешения открытыми протоколами и экосистемой FLOSS. Лично я всегда предпочту свободу удобству. 

Впереди светлое будущее. Просто у нас много работы.

_Gigi_

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://www.swanbitcoin.com/on-bitcoins-ux"><div class="kg-bookmark-content"><div class="kg-bookmark-title">On Bitcoin’s UX</div><div class="kg-bookmark-description">Swan makes Bitcoin investing easy. Buy automatically every day, week, or month, starting with as little as $10.</div><div class="kg-bookmark-metadata"><img alt="" class="kg-bookmark-icon" src="https://www.swanbitcoin.com/apple-touch-icon.png"/><span class="kg-bookmark-author">Swan Bitcoin</span><span class="kg-bookmark-publisher">Gigi</span></div></div><div class="kg-bookmark-thumbnail"><img alt="" src="https://www.swanbitcoin.com/static/3849b05e193fd956d3b4cbc4f300183b/2891c/ux-cover-image.png"/></div></a></figure>
