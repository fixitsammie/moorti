var copyTextareaBtn = document.querySelector('.js-copybtn');

copyTextareaBtn.addEventListener('click', function(event) {
  var copyTextarea = document.querySelector(".campaign-link");
  copyTextarea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
 
  } catch (err) {
  
  }
});