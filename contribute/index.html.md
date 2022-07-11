 

Мы не имеем ввиду сугубо материальную помощь (хотя это можно с легкостью сделать благодаря BTCPayServer):

<!--kg-card-begin: html-->

<style type="text/css"> .btcpay-form { display: inline-flex; align-items: center; justify-content: center; } .btcpay-form--inline { flex-direction: row; } .btcpay-form--block { flex-direction: column; } .btcpay-form--inline .submit { margin-left: 15px; } .btcpay-form--block select { margin-bottom: 10px; } .btcpay-form .btcpay-custom-container{ text-align: center; }.btcpay-custom { display: flex; align-items: center; justify-content: center; } .btcpay-form .plus-minus { cursor:pointer; font-size:25px; line-height: 25px; background: #DFE0E1; height: 30px; width: 45px; border:none; border-radius: 60px; margin: auto 5px; display: inline-flex; justify-content: center; } .btcpay-form select { -moz-appearance: none; -webkit-appearance: none; appearance: none; color: currentColor; background: transparent; border:1px solid transparent; display: block; padding: 1px; margin-left: auto; margin-right: auto; font-size: 11px; cursor: pointer; } .btcpay-form select:hover { border-color: #ccc; } #btcpay-input-price { -moz-appearance: none; -webkit-appearance: none; border: none; box-shadow: none; text-align: center; font-size: 25px; margin: auto; border-radius: 5px; line-height: 35px; background: #fff; } </style>

<style type="text/css"> input[type=range].btcpay-input-range { -webkit-appearance:none; width:100%; background: transparent; } input[type=range].btcpay-input-range:focus { outline:0; } input[type=range].btcpay-input-range::-webkit-slider-runnable-track { width:100%; height:3.1px; cursor:pointer; box-shadow:0 0 1.7px #020,0 0 0 #003c00; background:#f3f3f3; border-radius:1px; border:0; } input[type=range].btcpay-input-range::-webkit-slider-thumb { box-shadow:none; border:2.5px solid #cedc21; height:22px; width:22px; border-radius:50%; background:#0f3723; cursor:pointer; -webkit-appearance:none; margin-top:-9.45px } input[type=range].btcpay-input-range:focus::-webkit-slider-runnable-track { background:#fff; } input[type=range].btcpay-input-range::-moz-range-track { width:100%; height:3.1px; cursor:pointer; box-shadow:0 0 1.7px #020,0 0 0 #003c00; background:#f3f3f3; border-radius:1px; border:0; } input[type=range].btcpay-input-range::-moz-range-thumb { box-shadow:none; border:2.5px solid #cedc21; height:22px; width:22px; border-radius:50%; background:#0f3723; cursor:pointer; } input[type=range].btcpay-input-range::-ms-track { width:100%; height:3.1px; cursor:pointer; background:0 0; border-color:transparent; color:transparent; } input[type=range].btcpay-input-range::-ms-fill-lower { background:#e6e6e6; border:0; border-radius:2px; box-shadow:0 0 1.7px #020,0 0 0 #003c00; } input[type=range].btcpay-input-range::-ms-fill-upper { background:#f3f3f3; border:0; border-radius:2px; box-shadow:0 0 1.7px #020,0 0 0 #003c00; } input[type=range].btcpay-input-range::-ms-thumb { box-shadow:none; border:2.5px solid #cedc21; height:22px; width:22px; border-radius:50%; background:#0f3723; cursor:pointer; height:3.1px; } input[type=range].btcpay-input-range:focus::-ms-fill-lower { background:#f3f3f3; } input[type=range].btcpay-input-range:focus::-ms-fill-upper { background:#fff; } </style>

<form action="https://mainnet.demo.btcpayserver.org/api/v1/invoices" class="btcpay-form btcpay-form--block" method="POST">
<input name="storeId" type="hidden" value="2hKTKtrEmcVQytKAvBAB1TBLUxq9RjTXDDLny3FWPS4E"/>
<div class="btcpay-custom-container">
<input id="btcpay-input-price" max="none" min="0" name="price" onchange="document.querySelector('#btcpay-input-range').value = document.querySelector('#btcpay-input-price').value" oninput="event.preventDefault();isNaN(event.target.value) || event.target.value &lt;= 0 ? document.querySelector('#btcpay-input-price').value = 10 : event.target.value" step="any" style="width: 209px;" type="text" value="10"/>
<select name="currency">
<option selected="" value="USD">USD</option>
<option value="GBP">GBP</option>
<option value="EUR">EUR</option>
<option value="BTC">BTC</option>
</select>
<input class="btcpay-input-range" id="btcpay-input-range" max="1000" min="1" oninput="document.querySelector('#btcpay-input-price').value = document.querySelector('#btcpay-input-range').value" step="1" style="width:209px;margin-bottom:15px;" type="range" value="10"/>
</div>
<input alt="Pay with BtcPay, Self-Hosted Bitcoin Payment Processor" class="submit" name="submit" src="https://mainnet.demo.btcpayserver.org/img/paybutton/pay.svg" style="width:209px" type="image"/>
</form>

<!--kg-card-end: html-->

... через сеть Lightning (благодаря @lntxbot в Telegram):

<figure class="kg-card kg-image-card"><img alt="" class="kg-image" height="500" loading="lazy" sizes="(min-width: 720px) 720px" src="https://www.21ideas.org/content/images/2021/12/ln-tips-narrow.png" srcset="https://www.21ideas.org/content/images/size/w600/2021/12/ln-tips-narrow.png 600w, https://www.21ideas.org/content/images/2021/12/ln-tips-narrow.png 1000w" width="1000"/></figure>

... или через ряд биткоин-сетей (благодаря COINOS): 

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://coinos.io/Tony_Lightning"><div class="kg-bookmark-content"><div class="kg-bookmark-title">coinos</div><div class="kg-bookmark-description">Bitcoin Wallet</div><div class="kg-bookmark-metadata"><img alt="" class="kg-bookmark-icon" src="https://coinos.io/apple-touch-icon.png"/></div></div><div class="kg-bookmark-thumbnail"><img alt="" src="https://coinos.io/coinos-logo.jpg"/></div></a></figure>

<h2 id="%D0%B8%D0%B4%D0%B5%D0%B8-%D0%B8-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0">Идеи и предложения сотрудничества</h2>

Если у тебя есть идеи по улучшению проекта или предложения сотрудничества, пиши в телеграм: [@Tony\_Crusoe](https://t.me/Tony_Crusoe) 

<h2 id="%D0%BF%D0%BE%D0%BA%D1%83%D0%BF%D0%BA%D0%B0%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0-%D0%B1%D0%B5%D0%B7-kyc">Покупка/продажа биткоина без KYC*</h2>

Вы &nbsp;можете помочь переходом по реферальной ссылке: <a href="https://hodlhodl.com/join/TONYB" rel="noopener noreferrer">https://hodlhodl.com/join/TONYB</a> для покупки биткоинов (вы также получите скидку на комиссию с каждой сделки). А если вы надумали приобрести биткоин (_или его часть_), мы советуем поставить приватность во главу угла и пользоваться ТОЛЬКО non-KYC/AML платформой!

<h2 id="%D0%BF%D0%BE%D0%BA%D1%83%D0%BF%D0%BA%D0%B0%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0-%D0%BD%D0%B0-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9-%D0%B1%D0%B8%D1%80%D0%B6%D0%B5">Покупка/продажа биткоина на централизованной бирже</h2>

Если вы все же по тем или иным причинам решили использовать централизованную биржу, можете поддержать проект, зарегестрировавшись на одной из лидирующих бирже OKX по этой реферальной ссылке: <a href="https://www.youtube.com/redirect?event=video_description&amp;redir_token=QUFFLUhqa3gyaXNRcUowWDRFSHBoeW5NVzBkalpIRG93d3xBQ3Jtc0tuQ05TWWRsaUxSbExIRktjbE9qNWVnUVU2ZVRtdy1jeFdLNUY3YWM3VE9INU5OR09BbXYxZVJPY2JpVW0yN2FyYWE1eHJNbEhqLVJYWXY1MUJBOVJCbWFRV1ZiVVJPTDM3V0pwMjR1bDFxSHJaSWZ2WQ&amp;q=https%3A%2F%2Fwww.okex.com%2Fjoin%2F12452712&amp;v=o7CwrxMFsG0" rel="nofollow">https://www.okex.com/join/12452712</a>

<h2 id="%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0">Хранение биткоина</h2>

Не забывайте, что благодаря Биткоину у всех нас появилась возможность выступать в роли собственного банка! Переоценить значимость самостоятельного хранения ключей невозможно, а для безопасного хранения приватных ключей без аппаратного кошелька не обойтись. Если вы решили самостоятельно хранить собственные сбережения, убедитесь, что используете только самое безопасное оборудование. При выборе аппаратного кошелька мы советуем обратить внимание на продукты Coinkite. Осуществляя покупку по <a href="https://store.coinkite.com/promo/970E08C1C7383C967C7B" rel="noopener noreferrer">этой ссылке</a> вы не только получаете лучшее Битокин-онли решение на рынке, но и поддерживаете проект BITCOIN TRANSLATED!

---

 \* Подробнее о том, что такое KYC и почему оно вредно в этой статье: <https://www.21ideas.org/privacy-no-kyc/>