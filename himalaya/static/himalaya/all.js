"use strict";
const parentMarquee = document.querySelector(".marquee-wrapper");
const childMarquee = document.querySelector(".marquee-content");
const adChildMarquee = document.querySelector(".marquee-content").cloneNode(true);
parentMarquee.appendChild(adChildMarquee); 
const ulParentListContainer = document.querySelector('.marquee-wrapper');
let isDragging = false;
const dragStart = (e) => {
    if (!isDragging)
        return;
    ulParentListContainer.scrollLeft -= e.movementX;
};
const stopDragging = () => {
    isDragging = false;
};
ulParentListContainer.addEventListener('mousedown', () => isDragging = true)
ulParentListContainer.addEventListener('mousemove', dragStart);
window.addEventListener('mouseup', stopDragging);

const popupButton1= document.getElementById('ad1');
const popupDiv1= document.getElementById('popup1');
const closeButton1= document.getElementById('closeButton1');

popupButton1.addEventListener('click', () => {
    popupDiv1.style.display = 'block';
});

closeButton1.addEventListener('click', () => {
    popupDiv1.style.display = 'none';
});

const popupButton2= document.getElementById('ad2');
const popupDiv2= document.getElementById('popup2');
const closeButton2= document.getElementById('closeButton2');

popupButton2.addEventListener('click', () => {
    popupDiv2.style.display = 'block';
});

closeButton2.addEventListener('click', () => {
    popupDiv2.style.display = 'none';
});

const popupButton3= document.getElementById('ad3');
const popupDiv3= document.getElementById('popup3');
const closeButton3= document.getElementById('closeButton3');

popupButton3.addEventListener('click', () => {
    popupDiv3.style.display = 'block';
});

closeButton3.addEventListener('click', () => {
    popupDiv3.style.display = 'none';
});