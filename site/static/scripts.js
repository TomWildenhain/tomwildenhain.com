/*
Examples:
var valueOfNumberField = parseFloat(document.formName.fieldName.value);
Math.abs(number);
var myArray = new Array;
Text.charAt(i) = 'x';
timer1 = self.setInterval(function () { functionNume(); }, intervalInMSeconds);
document.getElementById("IdOfObject").style.styleName="newStyle";
window.addEventListener("keydown", function (e) { Tick1(); }, false);
thing.innerHTML = "Stuff";
*/

(function($){
  $(function(){

    $('.button-collapse').sideNav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function(){
  initialize();
});

function initialize(){
  $('.carousel').carousel();
  
  $('.table-of-contents').each(function() {
    var $this = $(this);
    var $target = $('#' + $(this).attr('data-target'));
    $this.pushpin({
      top: $target.offset().top,
      bottom: $target.offset().top + $target.outerHeight() - $this.height()
    });
  });
  
  $('.scrollspy').scrollSpy();
}