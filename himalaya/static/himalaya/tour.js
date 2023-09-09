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

