$(document).ready(function () {
  $('input#btn_translate').click(function () {
    translate();
  });

  $('input#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });

  function translate () {
    const val = $('input#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${val}`, function (data) {
      $('div#hello').html(data.hello);
    }, 'json');
  }
});
