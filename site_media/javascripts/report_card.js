 $(document).ready(function() {
   // put all your jQuery goodness in here.
  var pathname = window.location.pathname;
  if(window.location.hash){
    $(window.location.hash).css("display", "block")
  }
  else{
    $("#report-card").css("display", "block")
  }

  $(".report-navigation > a").click(function(event)  {
    event.preventDefault();
    var target_div = $(this).attr("href");
    $(".report-section").css("display", "none");
    $(target_div).css("display", "block");
  });

});
