const mountainLeft = document.querySelector('#mountain_left');
const mountainRight = document.querySelector('#mountain_right');
const cloud1 = document.querySelector('#clouds_1');
const cloud2 = document.querySelector('#clouds_2');
// const cloud3 = document.querySelector('#clouds_3');
// const cloud4 = document.querySelector('#clouds_4');
const text = document.querySelector('#text');
const man = document.querySelector('#man');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    mountainLeft.style.left = `-${value}px`
    cloud1.style.left = `${value*2}px`
    cloud2.style.left = `-${value*2}px`
    mountainRight.style.left = `${value}px`
    // cloud3.style.left = `${value*2}px`
    // cloud4.style.left = `${value*2}px`
    text.style.bottom = `${value}px`;
    man.style.height = `${window.innerHeight - value}px`
})