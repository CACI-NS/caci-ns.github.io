// Picnic CSS Transparent Navigation Bar
var nav = document.querySelector('nav');
function navScroll(){
 var className = 'transparent';
 var top = window.scrollY ? window.scrollY : document.documentElement.scrollTop;
 if (top > 0) {
  nav.classList.remove(className);
  [].forEach.call(document.querySelectorAll('[data-src]'), function(iframe){
   iframe.setAttribute('src', iframe.getAttribute('data-src'));
   iframe.removeAttribute('data-src');
  });
  $('svg .scroll-fill').each(function(){
   $(this).attr('fill', '#000000');
  });
 } else {
  nav.classList.add('transparent');
  nav.classList.add(className);
  $('svg .scroll-fill').each(function(){
   $(this).attr('fill', '#ffffff');
  });
 }
};
window.onscroll = navScroll;
navScroll();
setTimeout(function(){ nav.classList.remove('loading'); }, 10);

// Open External Links in new browser window
$(document.links).filter(function() {
 return this.hostname != window.location.hostname;
}).attr('target', '_blank');