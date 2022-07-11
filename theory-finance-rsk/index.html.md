 >  _Продолжаем серию статей, посвященных DeFi на Биткоине и подготовленных создателем телеграм-канала [CryptoBotan](https://t.me/CryptoBotan) при участии проекта 21 идея. Все статьи на эту тему собраны по тэгу [Bitcoin DeFi](https://www.21ideas.org/tag/bitcoin-defi/)._

В ранние времена смарт-контракты на Биткоине являлись достаточно простыми и примитивными, что не позволяло в полной мере создавать финансовые приложения и платформы. С приходом таких крупных обновлений как Segwit и Taproot, ситуация изменилась, хотя подавляющее большинство гибких и сложных финансовых взаимодействий до сих пор вынесено за пределы цепи.

Такой подход к конструированию протоколов не является новинкой и не уникален ни для Биткоина, ни для криптовалют в целом. Так называемая компартментализация (разделение чего-то целого на отсеки) применяется и в программном обеспечении, и даже в более обыденных сферах человеческой деятельности, таких как [дизайн](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF) и [строительство](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F). Более того, мы можем наблюдать эту самую модульность и в [биологии](https://en.wikipedia.org/wiki/Modularity_%28biology%29), и в [эволюционной психологии](https://en.wikipedia.org/wiki/Modularity_of_mind).

Причина тому кроется в практичности данного подхода, а также в вытекающей из этого повышенной безопасности систем. Вот как объясняет этот принцип гуру Unix Эрик Стивен Реймонд:

<blockquote class="kg-blockquote-alt"><em>"Единственный способ написать сложное, но при этом стабильное программное обеспечение — это снизить его глобальную сложность - построить его из простых частей, связанных четко определенными интерфейсами, так, чтобы большинство проблем были локальными, и у вас была возможность обновить часть, не ломая целое"</em></blockquote>

Таким образом мы оставляем основной слой протокола Биткоин невероятно надежным, цензуроустойчивым и простым, добавляя возможность исполнять гибкие смарт-контракты и предоставлять новые возможности для экспериментов и внедрения новых инструментов как разработчикам, так и пользователям сети, при этом не подвергая опасности основной монетарный слой Биткоина. Более того, помимо гибкости этот подход значительно повышает масштабируемость сети, снижая транзакционные издержки и позволяя передавать огромные объемы данных, не увеличивая давление на блокчейн Биткоина.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh6.googleusercontent.com/9oTc0EiC1VZ2NUNwO9f9mYjgQKJu56Yn4thhaiA5cUGe6QYsk2w6WMvH57azNkTCOIWcwFiOjpXZIYgXt-K58zGq5rmRl4mqJyqhIPKdq4bINkytkKlpiFY0ZpWHEr4nH_IqDFVqcFlfDGyLsA"/></figure>

Одним из способов преодолеть ограничения базового протокола Биткоина является вынос значительной части процессов и функций за пределы сети, сохраняя привязку к главной криптовалюте на уровне безопасности и обеспечения ценности. Первым таким решением являлся сайдчейн RSK, позволивший создавать многофункциональные смарт-контракты для построения финансовых приложений. Сегодня RSK – это обширная экосистема, внутри которой представлено множество DeFi-протоколов и инструментов.

<h1 id="%D0%BE-%D1%81%D0%B0%D0%B9%D0%B4%D1%87%D0%B5%D0%B9%D0%BD%D0%B0%D1%85">О сайдчейнах</h1>

Сайдчейны или боковые цепи – это решения для масштабирования сети Биткоин, которые являются отдельными блокчейнами со своими правилами и функциональностью. Функционирование сайдчейна как и основной сети обеспечивается за счет майнинга, при этом процессы, протекающие на сайдчейне никак не влияют на основную сеть. 

Движение биткоинов между блокчейном и сайдчейном обеспечивается при помощи “Двойной фиксации” (2-way-peg, 2WP) – функции блокировки биткоинов в одной сети и разблокировки в другой. Существует множество вариантов использования 2WP с различными способами хранения:

*   __Единственный хранитель:__ полностью централизованный метод хранения; не требует изменений протокола Биткоина;
*   __Федерация:__ использование так называемых “федераций нотариусов” и технологии [мультиподписи](https://www.21ideas.org/tag/multisig/); не требует изменений протокола Биткоина; используется в RSK;
*   __Сайдчейн SPV:__ децентрализованный подход к обеспечению 2WP, применяющий метод "Упрощенной проверки платежей" (Simplified Payment Verification, SPV); требуется софтфорк Биткоина;
*   __Drivechain:__ более развитая идея сайдчейнов, где хранителями средств являются майнеры, которые, с точки зрения теории игр, являются наименее “проблематичными” хранителями; требуется софтфорк Биткоина;
*   ______Гибридные:__ ____сочетают в себе свойства нескольких способов хранения

Сайдчейны позволяют расширить экосистему Биткоина, предлагая более гибкие и функциональные решения. К примеру, сайдчейн Liquid от компании Blockstream используется крупнейшими биржами и компаниями для быстрого перемещения средств, а RSK предлагает более быстрый блокчейн с более гибкими смарт-контрактами и поддержкой DeFi-приложений. Стоит также отметить, что исходя из трилеммы блокчейна – децентрализации, безопасности и масштабируемости, мы можем полноценно обеспечить только два из трех свойств, поэтому создание сайдчейнов для увеличения пропускной способности связано с определенными рисками.

<h1 id="%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-rsk">Что такое RSK?</h1>

Rootstock – это сайдчейн, разработанный компанией RSK Labs и поддерживаемый сообществом. Разработка блокчейна ведется с 2015 года, в то время как mainnet был запущен в 2018 году. На сегодняшний день RSK предлагает гибкие смарт-контракты за счет совместимости с инструментами и приложениями Ethereum, так как наследует формат учетных записей, Virtual Machine и интерфейс Web 3.0. Внутри экосистемы поддерживаются стейблкоины USDT, USDC, DAI и другие активы из различных сетей. 

Для взаимодействия с блокчейном RSK можно использовать кошельки Web 3.0 – Metamask, Nifty, Liquality, аппаратные – Trezor и Ledger, мобильные – rWallet а также другие решения, информацию о которых вы сможете найти в [разделе о кошельках](https://developers.rsk.co/wallet/use/) в руководстве платформы.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/KtxNHJYgn_C5WJCpE2MiEUJriwy9XLcG-JVSFUxpjXFYyXYbZalRDnEdITjPo6D_FC-cotB0DE1vC-q5U4RWv25DJSpa_Up0tAFe2nbwGFmQWvrsbqy3_gwVvt1m6HjMpg1UvuCkXlFF0GTduw"/></figure>

RSK также предлагает набор инфраструктурных протоколов, при помощи которых можно осуществлять простую и масштабируемую разработку dApps. Фреймворк RIF OS – это среда для разработчиков, упрощающая доступ к различным сервисам. В экосистему RIF входят:

*   Одноименный токен RIF стандарта ERC677;
*   Служба имен RNS;
*   RIF Lumino Network – Layer 3 на Биткоине, обеспечивающий каналы состояния для токенов внутри экосистемы;
*   RIF Marketplace – пользовательский интерфейс и рынок децентрализованных услуг: хранение данных, платежи, связь, службы данных и др;
*   RIF Gateways – инструменты для создания шлюзов между сетями и реальным миром;

<h1 id="%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B">Принцип работы</h1>

RSK является отдельным блокчейном и экосистемой, но при этом не имеет собственного токена или коина. Вместо этого внутри RSK представлен RBTC, привязанный к курсу BTC. Он добывается за счет объединенного с BTC майнинга (merge mining). Это возможно, поскольку в RSK используется тот же алгоритм хэширования и это также означает, что сайдчейн полагается на алгоритм консенсуса и уровень безопасности Биткоина.

Ниже представлена сравнительная таблица характеристик RSK и других блокчейнов:

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/lHM1YqPRda8FEr-pTBwSlgGj3AcsSSBEmxS87IotIUExGApI4yGqmsEoiAkSnHSXPPZP-ARq_zJIg43ipNbWEJhZGfWwB35Gx5oqfGTBxQa8rxBfUMWgXtJKK4ra8TLT9znQu5qfL3UFB33x3g"/></figure>

Чтобы переводить средства между основным блокчейном и сайдчейном необходимо воспользоваться специальным мостом. Хранение и разблокировка активов осуществляется при помощи автономной системы управления мультиподписями Powpeg, в то время как ее участниками являются так называемые “pegnatories”, куда входят крупнейшие известные компании например Xapo, Bitpay, Jaxx, BitGo, OKCoin, Zeppelin и другие.

RSK исследует гибридный способ достижения 2WP – &nbsp;Drivechain BIP, где хранителями также могут быть и майнеры. Для внедрения такого подхода двойной фиксации необходимо активировать в протоколе Биткоина специальные опкоды и расширения.

<h1 id="%D1%8D%D0%BA%D0%BE%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0">Экосистема</h1>

Пространство RSK является одним из крупнейших для построения DeFi-протоколов на Биткоине. Полный список приложений и платформ, интегрированных с цепочкой Rootstock вы можете найти в [данном перечне](https://developers.rsk.co/solutions/).

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/u0fAxSCLeObC2r_xKitWkIfcQgjcafV1mz9rmxab6v_gtSNYLsa823A3EaT4ijhD_J7Mq55MpVsw5ZPBJeMBuO527XL_xv5DNONYQnx8Alx6JZKvxCGDg6QQCekr8y6dGNjkDrZ-hn5Q1oG1tw"/></figure>

<h2 id="sovryn">Sovryn</h2>

Торговая платформа [Sovryn](https://www.sovryn.app/) – это одно из популярных приложений, построенных на RSK. Пользователям предлагается многофункциональное решение для спотовой и маржинальной торговли, возможности обмена активов, кредитования, займов и многое другое.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/8i66sc_CpTsrBs-ZZ2SoATDzjzapEfJU9XENJMoXukBdjtWGfSyZf2JailAbxCmn8MDgbY2Tj4rlmM5LJ470c_S5XUF7bs2uwoJ-x99k8C-nqJvx1FEV4o9Qda6lYhkcf3e5UBvrCBolecbpcA"/></figure>

Более подробно узнать о возможностях и преимуществах протокола Sovryn вы можете в одном из наших [предыдущих обзоров](https://www.21ideas.org/theory-finance-sovryn/).

<h2 id="%D1%81%D1%82%D0%B5%D0%B9%D0%B1%D0%BB%D0%BA%D0%BE%D0%B8%D0%BD%D1%8B">Стейблкоины</h2>

<h3 id="money-on-chain">Money on Chain</h3>

Экосистема RSK включает в себя набор смарт-контрактов [Money on Chain](https://alpha.moneyonchain.com/wallet/stable) для создания стабильных монет. Токен MoC является токеном управления протокола, а модель создания и использования стейблкоинов основано на взаимообратной трехуровневой системе:

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/t6bUBawV1HhjJTj_iDt7vr964bkMaQqMBTg4gX8rXTXKCNtV4miSHKn3HJ20FE4Uy_w5xaqTdDG_l9Rj5_ZE_EnCcnJJPx_zeRCaGzHqwz5ouJhMXDm5tJdNceIfSBXpYKkJGlOFOKWydgEm_Q"/></figure>

*   DOC (Dollar on Chain) – это стабильный токен стандарта ERC20 с привязкой к USD, где в качестве обеспечения используется RBTC;
*   BPro (BitPro) – токен ERC20 для держателей биткоинов. Пользователи могут отправить свои RBTC в протокол MoC, получая взамен BPro, которые используются для получения дополнительного пассивного дохода. Их владельцы получают доступ к бесплатному кредитному плечу, а также прибыль за счет процентной ставки и комиссий за использование платформы. Таким образом владельцы BPro предоставляют ликвидность для протокола;
*   BTCX – токен для трейдеров, являющийся длинной позицией с кредитным плечом к BTC на DEX для деривативов. Владельцы BTCX выплачивают комиссии за использование кредитного плеча владельцам BPro и снижают волатильность токена BPro

Для более глубокого погружения в суть работы протокола вы можете обратиться к [руководству](https://medium.com/moneyonchain/deep-dive-into-money-on-chain-8122e45657ba) Money on Chain.

<h3 id="babelfish">BabelFish</h3>

BabelFish – это кроссчейн-протокол стейблкоинов, который позволяет объединить ликвидность из разных сетей и эмитентов. [Стейблкоин XUSD](https://wiki.sovryn.app/en/technical-documents/xusd-overview) имеет привязку к доллару США и позволяет конвертировать такие стейблкоины как DAI, USDT, USDC и BUSD между собой.

<figure class="kg-card kg-image-card kg-card-hascaption"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/iVM4bo68-wVeGS25Z3vNGzEIzGLTagKLF_kiJn3nfHC1Cl-wFrWdbaeTEHZQyZmkvmNdRTva3xI4pRecv4sSHUe3FfHEkbPVrfIQ7J5x6ssSYKFTvYUKcGN_slaYsk0p9xbj0YiSWf1DDjUzlg"/><figcaption><a href="https://babelfish.gitbook.io/the-babelfish-gitbook/tutorials-and-guides/xusd-statistics"><em>https://babelfish.gitbook.io/the-babelfish-gitbook/tutorials-and-guides/xusd-statistics</em></a></figcaption></figure>

Функции XUSD реализованы при помощи моста Sovryn, где пользователи могут обменивать представленные стейблкоины из сетей BSC и ETH в XUSD на Sovryn в сети RSK. В течение двух месяцев после запуска основной сети объем конвертаций в XUSD достиг $10 миллионов.

<h2 id="rsk-swap">RSK Swap</h2>

Децентрализованная биржа [RSK Swap](https://app.rskswap.com/swap) является форком протокола Uniswap и предназначена для обмена токенов экосистемы. В основе DEX лежит модель автоматического маркет-мейкера (АММ). Пользователи могут мгновенно обменивать активы стандарта ERC20, а также использовать или создавать пулы ликвидности для получения дохода с комиссий, уплачиваемых пользователями.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/CZZffCxnMw89fjPd_jD1uxsUI5PC1AvmXMm7xKqa5Eq6PuSJYUa73_sfMSoge04wUy9mgrmpkOpyMj-1ypma3MiUrcQIOxtkaEoFIGwBUsABigT749HGIsYIMGbP_G4bN7FS5rew6TTuMDBm6w"/></figure>

<h2 id="%D0%BC%D0%BE%D1%81%D1%82%D1%8B">Мосты</h2>

Для переноса активов в блокчейн RSK используются межсетевые мосты. Количество поддерживаемых сетей увеличивается, и на сегодняшний день интегрировано более 5 блокчейн-экосистем. Создание большего числа мостов упрощает перенос ценности, а также позволяет улучшить взаимодействие и переход пользователей в экосистему Биткоина.

<h3 id="bitcoin-rsk">Bitcoin-RSK</h3>

Для переноса BTC из основной сети в сайдчейн RSK [используется](https://2wp-app.rsk.co/) метод двойной фиксации. Данное решение находится в стадии beta-тестирования и имеет ограниченный функционал.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/dvK7GejpqiJsu3u3uFBa0EaOCLZcV7M4u8FqFy2UhLzAmWxLr2n8nXpUHn5z_Zr-Mjkx3QBcFxZpOJpn9A5bn78U-zaz_TsOlCJgS1paNPxxbGUfaB5UZL-7sxbHtpEc4iiuFMXsEQMfMEzgeA"/></figure>

Мост работает только в одну сторону и через него можно переносить BTC в сеть RSK. Для подключения доступны только аппаратные кошельки Trezor и Ledger. В скором времени обещают добавить обратный вывод активов и другие решения для хранения.

Для того чтобы перенести активы из сайдчейна в основную сеть необходимо воспользоваться функцией Peg-Out, которая на данный момент осуществляется пользователями вручную. Минимальная сумма для отправки должна составлять 0,004 RBTC и выше. Подробная инструкция по переводу RBTC в BTC описана [данном руководстве](https://wiki.sovryn.app/en/sovryn-dapp/rbtc-to-btc). 

<h3 id="rsk-tokenbridge">RSK Tokenbridge</h3>

При помощи [этого решения](https://tokenbridge.rsk.co/) можно переносить активы между сетями Ethereum и RSK. В основе функционирования моста лежат так называемые Side Tokens (боковые токены) стандарта ERC777, совместимые с ERC20 и обладающие аналогичными свойствами. Если мы переносим нативный токен сети Ethereum в RSK, то тикер преобразованного актива получает префикс “r”, если же нативный токен сети RSK в Ethereum - то префикc “e”.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/dy54vFkmZZshumekfqwaBs-occAroawwIEnUjRmNGFNn4pV_dwrgJsT5cE2IvD7_D5JdHE31xEmO7vlF-ZnYABLhW2mh03gAO-JMfD7YMsKj4rK-KYjicnlT724S3mltfxxxX35LBkH7nDSIlw"/></figure>

При переносе активов следует учитывать, что время подтверждения транзакции будет варьироваться в зависимости от переводимой суммы – чем она выше, тем дольше придется ждать подтверждения. &nbsp;

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/Dhk8pz5rxnTSoVKIBGHdZujh_B9D3BJjSe8K_nh7HFGhhwyAGG3OT2UTSWk1mw4OhjxSq7ZdpeeDtZslo6o0ZcKO2mAIK0u_UPs3BZZsjzLQQ2LjGS-YaGXMMQlylolx1DjLnNpFDkKn_lfPlA"/></figure>

Также имеют место дневные ограничения для переноса токенов. Ниже представлена таблица с поддерживаемыми активами, дневными лимитами и объемами.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh5.googleusercontent.com/cM5gXHvjhGPPHSdO27dZV77M_03kn9PDAoUY2tF1-23Y5PIGmAugiEVC97XNJ6F-jSqYwbaWiY4TUDEgbYuToG7V64Ftq1cZXWv4mgxRFBydvYwQWsl6-QY680QnIaCn_MaPJXIinr1BQ696cg"/></figure>

<h3 id="sovryn-bridge">Sovryn Bridge</h3>

[Мост](https://bridge.sovryn.app/) поддерживает перевод активов между тремя сетями: BSC, RSK и Ethereum. Доступна передача ETH, BNB и стейблкоинов. Важно, что при переводе USDT, USDC, DAI, BUSD в сеть RSK они конвертируются в стейблкоин XUSD за счет интеграции решения BabelFish. В обратном направлении XUSD конвертируется в любой из выбранных стейблкоинов.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/Q21S0ziqAmcKEcsn5FyNw4KPLMV_v_As4f0JrPBCY43RE5P0JVkjo8IdBfwnZcclZKxspmJ38YU8XBDa47d6rri8doJH-60gV20y8CzuMGr-P7qsMtMxRDTVyWr52EinaVByVrY65vY2tNukaQ"/></figure>

<h3 id="liquality-swap">Liquality Swap</h3>

[Liquality Swap](https://swap.liquality.io/) – это функция обмена токенов, доступная в кошельке[ Liquality Wallet](https://liquality.io/). При помощи данного решения можно обменивать токены между сетями RSK, Bitcoin, Ethereum, Near и Polygon. Стоит отметить, что не все сети и не все активы совместимы с RSK, а для некоторых пар может оказаться недостаточно ликвидности.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/h-B8LUohr1MDgqWv5gmgTbpIfL_KM3Ikkqf-szw9-zQlhcoLk3JLQugL43WCW1ONjizeY6OOQAq9pX81I6BvVx0ggLnS_ak_6STpndde1IeqKRfXFy7DoyMPyJyuz-3GGFI5bOE0T8KyjGzfFg"/></figure>

Более полную информацию о возможностях кроссчейн-обмена можно получить в [руководстве](https://liquality.io/blog/how-to-use-the-liquality-wallet-101/#q-which-token-pairs-can-i-swap-within-the-liquality-wallet) кошелька

<h2 id="%D0%BF%D0%BE%D0%BB%D0%B5%D0%B7%D0%BD%D1%8B%D0%B5-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B">Полезные инструменты</h2>

Чтобы получить доступ к данным о транзакциях, аккаунтах, токенах, состоянии блокчейна, статистике и другой информации можно использовать [обозреватель блоков RSK](https://explorer.rsk.co/) или [Blockscout](https://blockscout.com/rsk/mainnet/). Информацию о размерах комиссий в сети можно получить на [RSK Gasstation](https://rskgasstation.info/?AspxAutoDetectCookieSupport=1). Для получения более подробной информации о возможностях блокчейнах Rootstock обратитесь к [документации](https://developers.rsk.co/the-stack/).

<h1 id="%D0%B7%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5">Заключение</h1>

Сайдчейн RSK является ярким примером возможностей, доступных поверх Биткоина. Пространство свободных финансов расширяется, а количество заблокированных внутри экосистемы средств уже превышает $100 миллионов. 

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh3.googleusercontent.com/adbf5jhv3mBkc-260YJcX2CZE2KbZCw0tlwSFfE5oSd-XRyDFqQOLGV3_4qhfdOmvkC21NWaBfQdVgURIYsd9kSYnNerEQi4P8QYgaFn6AKdTcVD5dC1ZqnVPQYjrpI7oO8tQw1JdPiH-m5rvQ"/></figure>

RSK предлагает пользователям, разработчикам и компаниям финансовые инструменты на основе безопасных сетевых протоколов. Одним из ключевых направлений дальнейшего развития платформы является создание многообразия DeFi-приложений и налаживание связей с другими экосистемами. Таким образом ценность Биткоина будет увеличиваться, приковывая к себе внимание все большего числа участников криптосообщества.  