 

<h2 id="%D1%83%D1%80%D0%BE%D0%BA%D0%B8-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8-%D1%83%D0%B7%D0%BB%D0%BE%D0%BC-%D0%BC%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D1%81%D0%B5%D1%82%D0%B8-lightning">Уроки, полученные при управлении узлом маршрутизации в сети Lightning.</h2>

_Оригинал: _

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://blog.lopp.net/lightning-network-liquidity-management-guide/"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Lightning Liquidity Management Guide</div><div class="kg-bookmark-description">Lessons learned from running a routing node on the Lightning Network.</div><div class="kg-bookmark-metadata"><img alt="" class="kg-bookmark-icon" src="https://blog.lopp.net/favicon.ico"/><span class="kg-bookmark-author">Cypherpunk Cogitations</span><span class="kg-bookmark-publisher">Jameson Lopp</span></div></div><div class="kg-bookmark-thumbnail"><img alt="" src="https://blog.lopp.net/content/images/2021/08/Lightning-network.jpg"/></div></a></figure>

С тех пор как люди начали запускать узлы Lightning в mainnet в начале 2018 года, некоторые задавались вопросом: какую реальную прибыль можно ожидать от размещения капитала в маршрутизационной ноде? Ник Бхатия подробно описал свою теорию возможных вариантов развития событий: 

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://timevalueofbtc.medium.com/the-time-value-of-bitcoin-and-lnrr-e0c435931bd8"><div class="kg-bookmark-content"><div class="kg-bookmark-title">The Time Value of Bitcoin and LNRR</div><div class="kg-bookmark-description">A Journey from Lightning to Reserve Currency Status</div><div class="kg-bookmark-metadata"><img alt="" class="kg-bookmark-icon" src="https://cdn-static-1.medium.com/_/fp/icons/Medium-Avatar-500x500.svg"/><span class="kg-bookmark-author">Medium</span><span class="kg-bookmark-publisher">Nik Bhatia</span></div></div><div class="kg-bookmark-thumbnail"><img alt="" src="https://miro.medium.com/max/1200/1*WTmxyhDyPckyyx1aNTWBJA.jpeg"/></div></a></figure>

Но, как мы узнали за эти годы, ROI (возврат инвестиций/прибыль от инвестиций) включает в себя гораздо больше, чем просто вложение капитала в каналы Lightning.

<!--kg-card-begin: html-->

<blockquote class="twitter-tweet tw-align-center"><p dir="ltr" lang="en">Lightning routing is a multi-faceted competitive system. It’s not just about capital, a brute force deployment of capital will cripple ROI. The system models a distributed predictive cache. Available capital is a factor but so is intelligent capital placement, reliability, speed.</p>— Alex Bosworth (@alexbosworth) <a href="https://twitter.com/alexbosworth/status/994603452310278144?ref_src=twsrc%5Etfw">May 10, 2018</a></blockquote>

 

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

<!--kg-card-end: html-->

В начале 2021 года я решил попытаться определить, насколько хорошо я смогу управлять узлом с целью получения прибыли за счет маршрутизации средств.

Я следовал процессу, описанному в моем предыдущем блог посте, поясняющем как создать свой узел, функционирующий исключительно через Tor:

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://blog.lopp.net/tor-only-bitcoin-lightning-guide/"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Tor-Only Bitcoin &amp; Lightning Guide</div><div class="kg-bookmark-description">A detailed guide to improving your privacy as a Lightning Network user.</div><div class="kg-bookmark-metadata"><img alt="" class="kg-bookmark-icon" src="https://blog.lopp.net/favicon.ico"/><span class="kg-bookmark-author">Cypherpunk Cogitations</span><span class="kg-bookmark-publisher">Jameson Lopp</span></div></div><div class="kg-bookmark-thumbnail"><img alt="" src="https://blog.lopp.net/content/images/2021/05/network.png"/></div></a></figure>

Запустить программное обеспечение было проще простого. Далее мне нужно было понять, как наиболее эффективно разместить свой капитал.

<h1 id="%D0%B2%D0%B0%D1%88%D0%B0-%D0%BF%D1%80%D0%B8%D0%B1%D1%8B%D0%BB%D1%8C-%D0%BC%D0%BE%D0%B6%D0%B5%D1%82-%D0%B2%D0%B0%D1%80%D1%8C%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F">Ваша прибыль может варьироваться</h1>

К сожалению, невозможно написать руководство, которое предоставило бы простые инструкции в стиле: "Подключитесь к этим узлам и получайте комиссионные". Необходимо рассматривать Lightning Network как конкурентный рынок, предлагающий эффективное передвижение капитала. Как и в случае с определенной торговой стратегией, если все начнут прибегать к одним и тем же техникам, все преимущества, присущие этой стратегии, исчезнут, и это создаст возможности для других участников торговать против нее. Если все будут строить одни и те же мосты для перемещения капитала, это превратится в гонку на износ в конкуренции за комиссионные, и для других операторов будет разумнее "противодействовать" этой стратегии, строя мосты в другом месте.

<h1 id="%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85">Множество переменных</h1>

Вы, наверное, заметили, что эта статья получилась очень длинной. Причина тому — наличие множества различных вопросов, которые необходимо учитывать при эксплуатации узла Lightning Network с целью максимизации маршрутизации. К ним относятся:

*   Размещение капитала
*   Комиссии за маршрутизацию
*   Минимизация ончейн-комиссий
*   Ваша общая входящая/исходящая емкость
*   Поддержание пропускной способности маршрутизации (ребалансировка / Submarine Swaps)
*   Входящая / исходящая емкость пользователей
*   Безотказность / время работы / здоровье узлов
*   Безотказность / нагрузка / сетевое подключение вашего узла

<h1 id="%D0%BF%D1%80%D0%B8%D0%BD%D1%8F%D1%82%D0%B8%D0%B5-%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8E-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%BE%D0%B2">Принятие решения по открытию каналов</h1>

Алекс Босворт предоставляет подробное руководство [в этом документе](https://github.com/alexbosworth/run-lnd/blob/master/LIQUIDITY.md).

Открыть каналы Lightning очень просто — подавляющее большинство узлов в сети примут входящий канал практически любой емкости. Таким образом, есть опасность заблокировать капитал у плохо функционирующего узла, который не обрабатывает значительного количества платежей. А если ваш _пир_ (держатель узла, с которым вы открыли канал) перестает отвечать, закрытие канала может привести к тому, что ваш капитал окажется в бездействии на несколько недель.

В ходе моих первоначальных экспериментов я обнаружил, что некоторые узлы просто не маршрутизируются, возможно, потому, что у них недостаточно ликвидности, направленной другим узлами. Довольно сложно сказать, каков будет статус пиров, не исследуя различные маршруты, проходящие через них, что изначально требует открытия канала. Я ожидаю, что в будущем появятся сервисы, которые помогут решить эту проблему и дадут больше информации о состоянии ликвидности того или иного узла.

Что бы вы ни делали, __избегайте использования автопилота lnd__; он просто подключается к крупным популярным узлам. Аналогично, похоже, что многие просто заходят на Lightning Terminal или 1ML и подключаются к узлам с самым высоким рейтингом. Это может звучать нелогично, но такая стратегия не является выигрышной, если вы хотите, чтобы ваш узел направлял большое количество платежей. Скорее, __вы должны стремиться к созданию новых мостов__, связывая между собой узлы, которым в противном случае пришлось бы совершить много _хопов_ (перенаправлений/прыжков) для маршрутизации друг к другу.

Еще одна проблема, с которой я сталкивался, — это использование оценки BOS для решения с какими узлами открывать каналы. Алекс Босворт, который написал алгоритм подсчета баллов, сказал мне, что он не был задуман как система подбора узлов маршрутизации/оценки качества.

Я использовал инструмент подбора узлов ([node match tool](https://moneni.com/nodematch)), чтобы выяснить, какие узлы больше всего повысят мою центрированность. Однако я бы еще раз предостерег от слепого открытия каналов с узлами, получившими наивысший рейтинг. Прежде чем открыть канал с одним из рекомендованных узлов, я проверяю его на [Lightning Terminal](https://terminal.lightning.engineering/), чтобы убедиться в его стабильности. Затем я проверяю его на [1ML](https://1ml.com/), чтобы убедиться, что они устанавливают разумную политику комиссионных сборов.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/WPvzgsJ-triF-zFmbTXT8QgjUJE2Dp69Blgdb-n0R7bTjK6AcoTBgLC311V1Y0bdCTV47NFvdfyZ5E-tPGIL3J2kNj1YvgFagsMOjxZJCEi-074hMMu1vQSpQrovmb6D4X2TCGIK=s0"/></figure>

Чтобы получить альтернативный взгляд на то, как повысить центрированность узла, я использовал скрипт Gridflare "[improve centrality](https://github.com/Gridflare/lndpytools/blob/main/improvecentrality.py)" от [lndpytools](https://github.com/Gridflare/lndpytools). Он, конечно, не так удобен в использовании, как другие веб-инструменты, так как требует получения полного дампа сетевого графа с вашего узла, переноса его на настольный компьютер / ноутбук, а затем запуска анализа на этом json-файле.

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" loading="lazy" src="https://lh4.googleusercontent.com/zVunKHEINDV8WRcehZ_IPhMfTGtbPrPUPTi5F4b_pLt-nwM-fozkycMMrbHfWwNeHjokSnF8HmBS4Bu8d2XXlDAEvYoz6CBZqQrh1jDW2EBNsSfACH2zSrowrGXJXOofPsKhR_cU=s0"/></figure>

Мой опыт подсказывает, что большинство "высокосвязанных" узлов с 500+ каналами, как правило, нестабильны и поэтому не направляют много платежей. Я подозреваю, что они слишком сильно нагружают свое оборудование. Однако другие пользователи сообщают о другом опыте — ваша прибыль может варьироваться!

Если вы можете себе это позволить, не создавайте каналы размером менее 10M (миллионов) сат. Имейте в виду, что максимальный размер платежа по умолчанию составляет чуть более 4M сат. Поэтому, если вы хотите иметь возможность поддерживать каналы, которые могут маршрутизировать максимальный размер платежа в любом направлении, вам нужно, по крайней мере, удвоить этот объем, а лучше еще сильнее его увеличить, поскольку довольно сложно иметь достаточно входящей ликвидности и достаточно исходящей ликвидности на обеих сторонах канала. Если вы не пытаетесь управлять узлом маршрутизации, это не так важно. Также можно быть узлом маршрутизации больших объемов платежей с меньшими каналами — скорее всего, вам придется делать больше ребалансировок — но все же желательно, чтобы пропускная способность вашего канала была как можно выше.

Если вы не можете позволить себе каналы в 10М сат, я бы посоветовал минимум 1М сат. Моя нода переслала 400 платежей за последние несколько месяцев, и средняя сумма пересылки составила 420,000 сат — около $150. Таким образом, вам потребуется почти идеально сбалансированный канал в 1М сат, чтобы иметь возможность переслать один средний платеж. Надеюсь, динамика изменится, когда все больше и больше кошельков начнут использовать [многоходовые](https://t.me/bitcoin_translated/1427) (multi-path) платежи.

В lnd вы можете предотвратить входящие каналы меньше определенного размера, введя следующую строку в lnd.conf:

<!--kg-card-begin: markdown-->

minchansize=1000000
