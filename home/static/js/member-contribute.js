$(window).on('load',function(){

	// fade-in
    $(window).scroll(function (){
        $('.fade-in').each(function(){
            var POS = $(this).offset().top;  //fade-inがついている要素の位置
            var scroll = $(window).scrollTop();  //スクロール一
            var windowHeight = $(window).height();  //ウィンドウの高さ

            if (scroll > POS - windowHeight + windowHeight/8){
                $(this).css("opacity","1" );
            } else {
                $(this).css("opacity","0" );
            }
        });
    });
});




$(function() {

  $('#works').click(function() {

    $('.news').fadeOut(500);
    $('.works').fadeIn(500);
    $('.works-btn').css('background-color','SkyBlue');

    $('.works-btn p').css('color','Black');
    $('.news-btn').css('background-color','PowderBlue');
    $('.news-btn p').css('color','White');
  });

  $('#news').click(function() {

    $('.news').fadeIn(500);
    $('.works').fadeOut(500);
    $('.news-btn').css('background-color','SkyBlue');
    $('.news-btn p').css('color','Black');
    $('.works-btn').css('background-color','PowderBlue');
    $('.works-btn p').css('color','White');

  });


});


$(function(){
  //画像ファイルプレビュー表示
  $('form').on('change', 'input[type="file"]', function(e) {
    var file = e.target.files[0],
        reader = new FileReader(),
        $preview = $(".preview");
        t = this;

    // 画像ファイル以外の場合は何もしない
    if(file.type.indexOf("image") < 0){
      return false;
    }

    reader.onload = (function(file) {
      return function(e) {
        $preview.empty();
        $preview.append($('<img>').attr({
                  src: e.target.result,
                  width: "30%",
                   class: "preview",
                  title: file.name
              }));
      };
    })(file);

    reader.readAsDataURL(file);
  });
});


$(function(){
  $('.js-selectFile').on('click', 'button', function () {
    $('.js-upload').click();
    return false;
});

$('.js-upload').on('change', function() {
    //選択したファイル情報を取得し変数に格納
    var file = $(this).prop('files')[0];
    //アイコンを選択中に変更
    $('.js-selectFile').find('.icon').addClass('js-select').html('選択中');
    //未選択→選択の場合（.filenameが存在しない場合）はファイル名表示用の<div>タグを追加
    if(!($('.filename').length)){
        $('.js-selectFile').append('<div class="filename"></div>');
    };
    //ファイル名を表示
    $('.filename').html('ファイル名：' + file.name);
});

})
