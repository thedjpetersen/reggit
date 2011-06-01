$(document).ready(function(){
  var days_ar = {"M":"Monday", "T":"Tuesday", "W":"Wednesday", "R":"Thursday", "F":"Friday"};
  $(".combination").hover(
    //This is hour entry function for when we our hovering
    function(){
    //Get the id of the combination that the mouse is hovering over
    combination_id = parseInt($(this).attr("id").substring(12))
    combination = combinations[combination_id-1];
    
    //Initialize our max and min times(used for sizing the table)
    first_time = 23;
    last_time = 0;

    //We will loop through every class in the combination
    $.each(combination, function(index, value){
        days = value["days"];
        times = value["times"];

        //Get the beginning and end of the class
        start_time = parseInt(times[0].substring(0,2), 10);
        end_time = parseInt(times[1].substring(0,2), 10);
        
        //If the beginning or end is greater than our max or min times
        //Assign the max or min times to the value
        if(start_time < first_time){
          first_time = start_time;
        }
        if(end_time > last_time){
          last_time = end_time;
        }

        //Loop through each day that the class is held
        for (day in days){
          var i = 0;
          //Loop through the time between the start and end
          //e.g. if our start and finish time is 2 and 4
          //This loop will loop i through [2,3,4]
          for(i=start_time;i<end_time+1;i++){
            //Set up our day and time selector
            day_selector = "." + days_ar[days[day]];
            time_selector = "#hour-" + i           
            
            //Use our day and time selector to select specific cell
            //from table
            selector = time_selector + ">" + day_selector;
            half_selector = time_selector + "-half>" + day_selector;
            
            //If we are the first iteration through we will set the table to the title
            if(i==start_time){
              name = value['department'].toUpperCase() + " " + value['number']
              $(selector).text(name);
            }

            //We will set this cell to have a color
            $(selector).addClass("selected");
            $(half_selector).addClass("selected");
            color = "hsl(" + (Math.round(360/10)-1)*(index+1) + ",100%,48%)";
            $(selector).css("background", color + " !important");
            $(half_selector).css("background", color + " !important");

            colorbox = "#combination-" + combination_id + " ." + value['crn']

            $(colorbox).css("display", "inline-block");
            $(colorbox).css("background", color + " !important");

          };
        }
      });

    //Cycle through rows that are inbetween our beginning and end time and set them
    //to visible
    for(i=first_time; i<last_time+1; i++){
      selector = "#hour-" + i;
      $(selector).css("display","table-row");
      selector=selector+"-half"
      $(selector).css("display","table-row");
    }

    },
    //This is our exit function for when the user moves their mouse out of the area
    function(){
      $(".selected").text("")
      $(".selected").css("background","white !important");
      $(".colorbox").css("display", "none");
      $(".selected").removeClass("selected");
      $(".hours").css("display","none");
    }
    );
});
