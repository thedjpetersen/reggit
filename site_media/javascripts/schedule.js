$(document).ready(function(){

    var days_ar = {"M":"Monday", "T":"Tuesday", "W":"Wednesday", "R":"Thursday", "F":"Friday"};

    // For sizing the table
    first_time = 23;
    last_time = 0;
    
    $.each(schedule, function(index, course){
        days = course["days"];
        times = course["times"];

        // See if class changes the table sizing
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
                    
                // Use selectors to select specific cell from table
                selector = time_selector + ">" + day_selector;
                half_selector = time_selector + "-half" + day_selector;

                // Set table to title
                if(i==start_time){
                    name = course['department'].toUpperCase() + " " + course['number']
                    $(selector).text(name);
                }

                // Color cell
                $(selector).addClass("selected");
                $(half_selector).addClass("selected");
                color = "hsl(" + (Math.round(360/10)-1)*(index+1) + ",100%,48%)";
                $(selector).css("background", color + " !important");
            }
        }
    });
     
    // Cycle through rows and make them visible   
    for(i=first_time; i<last_time+1; i++){
        selector = "#hour-" + i;
        $(selector).css("display", "table-row");
        selector = selector + "-half"
        $(selector).css("display", "table-row");
    }    
});
