$(function(){

    // サイトアクセス時に非表示にしてから、フェードインさせる
    $('#content').hide();
    $('#content').fadeIn(2000);

    // リンククリック時にフェードアウトしてから、画面遷移する

});



$(document).ready(function() {
  $(".drawer").drawer();
});
$(function() {
	// 初期位置へ移動
	$('.navi span').css({
		width: $('.navi .current').outerWidth(),
		left: $('.navi .current').position().left
	});
	// マウスオーバーでアニメーション
	$('.navi a').mouseover(function(){
		$('.navi span').stop().animate({
			width: $(this).outerWidth(),
			left: $(this).position().left}
		,'fast');
	});


	});
