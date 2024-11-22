function update_cost(){
    // Inform the user of the cost of choice
   
    // get dates
    let arrive = document.getElementById('id_zoo_booking_date_arrive').value
    let leave = document.getElementById('id_zoo_booking_date_leave').value

    // Calculate number of days
    arrive = new Date(arrive)
    leave = new Date(leave)
    diff = leave.getTime() - arrive.getTime();
    days = Math.round(Math.abs(diff/(1000*60*60*24)));

    // check the days is valid
    if (String(days) == "NaN"){
        let price = document.getElementById('zoo_output')
        price.innerHTML = "Zoo cost: Dates Not Chosen"
    }else{

        // calculate costs
        let total = parseInt(adults.value) * 12
                    + parseInt(children.value) * 8
                    + parseInt(oaps.value) * 9

        // multiply by number of nights booked
        total = total * days

       
        // console.log("Total:" + String(total))

        // update the display for the user
        let price = document.getElementById('zoo_output')
        price.innerHTML = "Zoo cost: £" + String(total)
    }
}


// get html elements
let adults = document.getElementById("id_zoo_booking_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_zoo_booking_children");
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_zoo_booking_oap");
oaps.addEventListener("change", update_cost)

// TO DO: add the same updates for the date fields
