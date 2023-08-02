window.onload = () =>{

    document.getElementById('slider_0').style.backgroundColor = 'rgb(2, 128, 102)'
}

function price(data){
    let id = data.classList[0].replace('product_', '')
    console.log(id);
    document.getElementById(`total_price_${id}`).innerHTML = document.getElementById(`i_${id}`).value * document.getElementById(`price_${id}`).innerHTML + "руб."
}






function ban(){
    let sliders = document.getElementById('slider')
    let slider_array = [document.getElementById('slider__0'), document.getElementById('slider__1'), document.getElementById('slider__2')]
    let light_slider = [document.getElementById(`slider_0`), document.getElementById(`slider_1`), document.getElementById(`slider_2`)]
    

    if (light_slider[1].style.backgroundColor == 'rgb(2, 128, 102)')
    {
        slider_array[2].classList ='slider_img_d'
        slider_array[1].classList = 'slider_img_d'
        slider_array[2].classList ='slider_img animate'
        light_slider[0].style.backgroundColor = 'white'
        light_slider[2].style.backgroundColor = 'rgb(2, 128, 102)'
        light_slider[1].style.backgroundColor = 'white'
        setTimeout(sleep, 10000, slider_array[2])
    }else
    {
        if (light_slider[0].style.backgroundColor == 'rgb(2, 128, 102)'){
            slider_array[1].classList ='slider_img_d'
            slider_array[0].classList = 'slider_img_d'
            slider_array[1].classList ='slider_img animate'
            light_slider[2].style.backgroundColor = 'white'
            light_slider[1].style.backgroundColor = 'rgb(2, 128, 102)'
            light_slider[0].style.backgroundColor = 'white'
            setTimeout(sleep, 10000, slider_array[1])
        }
        else{
            if (light_slider[2].style.backgroundColor == 'rgb(2, 128, 102)'){
                slider_array[1].classList ='slider_img_d'
                slider_array[2].classList = 'slider_img_d'
                slider_array[0].classList ='slider_img animate'
                light_slider[0].style.backgroundColor = 'rgb(2, 128, 102)'
                light_slider[1].style.backgroundColor = 'white'
                light_slider[2].style.backgroundColor = 'white'
                setTimeout(sleep, 10000, slider_array[0])
                }
        }
    }
    sliders.classList.remove('imp')
}

function sleep (item){
    item.classList.remove('animate')
}

setInterval(ban, 10000)


function slider(i){
    let sliders = document.getElementById('slider')
    let slider_array = [document.getElementById('slider__0'), document.getElementById('slider__1'), document.getElementById('slider__2')]
    let light_slider = [document.getElementById(`slider_0`), document.getElementById(`slider_1`), document.getElementById(`slider_2`)]
    if (i==2){
        slider_array[1].classList ='slider_img_d'
        slider_array[0].classList = 'slider_img_d'
        slider_array[2].classList ='slider_img animate'
        light_slider[0].style.backgroundColor = 'white'
        light_slider[1].style.backgroundColor = 'white'
        light_slider[2].style.backgroundColor = 'rgb(2, 128, 102)'
        setTimeout(sleep, 10000, slider_array[2])
    }else{
        if (i==1){
        slider_array[2].classList ='slider_img_d'
        slider_array[0].classList = 'slider_img_d'
        slider_array[1].classList ='slider_img animate'
        light_slider[0].style.backgroundColor = 'white'
        light_slider[2].style.backgroundColor = 'white'
        light_slider[1].style.backgroundColor = 'rgb(2, 128, 102)'
        setTimeout(sleep, 10000, slider_array[1])
        }else{
        slider_array[1].classList ='slider_img_d'
        slider_array[2].classList = 'slider_img_d'
        slider_array[0].classList ='slider_img animate'
        light_slider[2].style.backgroundColor = 'white'
        light_slider[1].style.backgroundColor = 'white'
        light_slider[0].style.backgroundColor = 'rgb(2, 128, 102)'
        setTimeout(sleep, 10000, slider_array[0])
        }
    }
}

let i = 0
let slider_array = ["media/demo/kryto1.png", "media/demo/kryto2.png", "media/demo/kryto3.png"]







document.getElementById('open').onclick = navbar()









function navbar(){

    let center = document.getElementById('center')
    let right = document.getElementById('right')
    try {
        document.getElementById('cart').innerHTML = 'Корзина'
    } catch (error) {
        
    }
        

    if (center.classList == 'top'){
        center.classList.add('center')
        right.classList.add('right')

        center.classList.remove('top')
        right.classList.remove('bottom')
        document.getElementById('nav').style.padding = '0px'
    }
    else{
        center.classList.remove('center')
        right.classList.remove('right')

        document.getElementById('nav').style = 'padding-left: 20px;padding-right: 20px;padding-top: 20px;'
        center.classList.add('top')
        right.classList.add('bottom')
        document.getElementById('trait').remove()
    }
}




function add(data){
    let classes = data.classList
    let values = document.getElementById(`i_${classes[0]}`).value
    http://127.0.0.1:8000/caterogy/krosovki/add/cart/product=40&count=5
    return window.location = `/category/${classes[1]}/add/cart/product=${classes[0]}&count=${values}`
}


function update(data){
    let classes = data.classList
    let values = document.getElementById(`i_${classes[0]}`)
    return window.location = `/update/cart/product=${classes[0]}&count=${values.value}`
}