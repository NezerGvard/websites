window.onload = function(){
function translit(word){
    var answer = '';
    var converter = {
        'а': 'a',    'б': 'b',    'в': 'v',    'г': 'g',    'д': 'd',
        'е': 'e',    'ё': 'e',    'ж': 'zh',   'з': 'z',    'и': 'i',
        'й': 'y',    'к': 'k',    'л': 'l',    'м': 'm',    'н': 'n',
        'о': 'o',    'п': 'p',    'р': 'r',    'с': 's',    'т': 't',
        'у': 'u',    'ф': 'f',    'х': 'h',    'ц': 'c',    'ч': 'ch',
        'ш': 'sh',   'щ': 'sch',  'ь': '',     'ы': 'y',    'ъ': '',
        'э': 'e',    'ю': 'yu',   'я': 'ya',
    
        'А': 'A',    'Б': 'B',    'В': 'V',    'Г': 'G',    'Д': 'D',
        'Е': 'E',    'Ё': 'E',    'Ж': 'Zh',   'З': 'Z',    'И': 'I',
        'Й': 'Y',    'К': 'K',    'Л': 'L',    'М': 'M',    'Н': 'N',
        'О': 'O',    'П': 'P',    'Р': 'R',    'С': 'S',    'Т': 'T',
        'У': 'U',    'Ф': 'F',    'Х': 'H',    'Ц': 'C',    'Ч': 'Ch',
        'Ш': 'Sh',   'Щ': 'Sch',  'Ь': '',     'Ы': 'Y',    'Ъ': '',
        'Э': 'E',    'Ю': 'Yu',   'Я': 'Ya'
    };
    
    for (var i = 0; i < word.length; ++i ) {
        if (converter[word[i]] == undefined){
            answer += word[i];
        } else {
            answer += converter[word[i]];
        }
    }
    
    return answer;
}

let tg = window.Telegram.WebApp; //получаем объект webapp телеграма 

   tg.expand(); //расширяем на все окно  

   tg.MainButton.text = "Changed Text"; //изменяем текст кнопки 
   tg.MainButton.setText("Changed Text1"); //изменяем текст кнопки иначе
   tg.MainButton.textColor = "#F55353"; //изменяем цвет текста кнопки
   tg.MainButton.color = "#143F6B"; //изменяем цвет бэкграунда кнопки
   tg.MainButton.setParams({"color": "#143F6B"}); //так изменяются все параметры




let url = '/prototype/register'

let username = document.getElementById('id_username').value
let email = document.getElementById('id_email').value
let password1 = document.getElementById('id_password1').value
let password2 = document.getElementById('id_password2').value

let xml = new XMLHttpRequest()
xml.open('POST', url, false)
xml.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')

xml.onreadystatechange = () =>{
    console.log(xml.readyState, xml.status);
    if(xml.readyState ===4 && xml.status === 201){
        let serverResponse = JSON.parse(xml.response)
        console.log(serverResponse);
    }
}

console.log(document.getElementById('testForm').object);
console.log(document.getElementById('testForm'));

username = 'ktoktokto'
email = 'dasaz.dazpsa'+'@gmail.com'
password1 = 'adsazdooqmda'
password2 = 'adsazdooqmda'

// username = 'azda'+g.initDataUnsafe.user.id
// email = translit(tg.initDataUnsafe.user.first_name+tg.initDataUnsafe.user.last_name)+'@gmail.com'
// password1 = tg.initDataUnsafe.user.username
// password2 = tg.initDataUnsafe.user.username
let body = JSON.stringify({username: username, email: email, password1: password1, password2: password2})
console.log(body);
xml.send(body)
  
function sendData( data ) {
    const XHR = new XMLHttpRequest(),
          FD  = new FormData();
          console.log(FD);
  
    // Push our data into our FormData object
    for( name1 in data ) {
      FD.append( name1, data[ name1 ] );
    }
  
    // Define what happens on successful data submission
    XHR.addEventListener( 'load', function( event ) {
      alert( 'Yeah! Data sent and response loaded.' );
    } );
  
    // Define what happens in case of error
    XHR.addEventListener(' error', function( event ) {
      alert( 'Oops! Something went wrong.' );
    } );
  
    // Set up our request
    XHR.open( 'POST', '/prototype/register' );
  
    // Send our FormData object; HTTP headers are set automatically
    XHR.send( FD );
  }

  sendData(body)







   let btn = document.getElementById("btn"); //получаем кнопку скрыть/показать 

   btn.addEventListener('click', function(){ //вешаем событие на нажатие html-кнопки
      if (tg.MainButton.isVisible){ //если кнопка показана 
         tg.MainButton.hide() //скрываем кнопку 
      }
      else{ //иначе
         tg.MainButton.show() //показываем 
      }
   });

   let btnED = document.getElementById("btnED"); //получаем кнопку активировать/деактивировать
   btnED.addEventListener('click', function(){ //вешаем событие на нажатие html-кнопки
      if (tg.MainButton.isActive){ //если кнопка показана 
         tg.MainButton.setParams({"color": "#E0FFFF"}); //меняем цвет
         tg.MainButton.disable() //скрываем кнопку 
      }
      else{ //иначе
         tg.MainButton.setParams({"color": "#143F6B"}); //меняем цвет
         tg.MainButton.enable() //показываем 
      }
   });

   Telegram.WebApp.onEvent('mainButtonClicked', function(){
      tg.sendData("some string that we need to send"); 
      //при клике на основную кнопку отправляем данные в строковом виде
   });


   let usercard = document.getElementById("usercard"); //получаем блок usercard 

   let profName = document.createElement('p'); //создаем параграф
   profName.innerText = `${tg.initDataUnsafe.user.first_name}
   ${tg.initDataUnsafe.user.last_name}
   ${tg.initDataUnsafe.user.username} (${tg.initDataUnsafe.user.language_code})`;
   //выдем имя, "фамилию", через тире username и код языка
   usercard.appendChild(profName); //добавляем 

   let userid = document.createElement('p'); //создаем еще параграф 
   userid.innerText = `${tg.initDataUnsafe.user.id}`; //показываем user_id
   usercard.appendChild(userid); //добавляем
}

   //работает только в attachment menu
   // let pic = document.createElement('img'); //создаем img
   // pic.src = tg.initDataUnsafe.user.photo_url; //задаём src 
   // usercard.appendChild(pic); //добавляем элемент в карточку 