$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const val = $('input#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${val}`, function (data) {
      $('div#hello').html(data.hello);
    }, 'json');
  });
});
