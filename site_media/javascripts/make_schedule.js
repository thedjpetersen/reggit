$(document).ready(function(){
  var days_ar = {"M":"Monday", "T":"Tuesday", "W":"Wednesday", "R":"Thursday", "F":"Friday"};
  $(".combination").hover(function(){
    combination = combinations[parseInt($(this).attr("id").substring(12))-0];
    first_time = 23;
    last_time = 0;
    $.each(combination, function(index, value){
        days = value["Times"]["Days"];
        times = value["Times"]["Time"];

        start_time = parseInt(times[0].substring(0,2), 10);
        end_time = parseInt(times[1].substring(0,2), 10);
        if(start_time < first_time){
          first_time = start_time;
        }
        if(end_time > last_time){
          last_time = end_time;
        }
        for (day in days){
          var i = 0;
          for(i=start_time;i<end_time+1;i++){
            day_selector = "." + days_ar[days[day]];
            time_selector = "#hour-" + i
            selector = time_selector + ">" + day_selector;
            half_selector = time_selector + "-half>" + day_selector;
            if(i==start_time){
              name = value['Dep'].toUpperCase() + " " + value['Num'] + " (" + value["Type"] +")"
              $(selector).text(name);
            }
            $(selector).addClass("selected");
            $(half_selector).addClass("selected");
            color = "hsl(" + (Math.round(360/combinations.length)-1)*(index+1) + ",100%,48%)";
            $(selector).css("background", color + " !important");
            $(half_selector).css("background", color + " !important");

          };
        }
      });
    for(i=first_time; i<last_time+1; i++){
      selector = "#hour-" + i;
      $(selector).css("display","table-row");
      selector=selector+"-half"
      $(selector).css("display","table-row");
    }

    },
    function(){
      $(".selected").text("")
      $(".selected").css("background","white !important");
      $(".selected").removeClass("selected");
      $(".hours").css("display","none");
    }
    );
});
