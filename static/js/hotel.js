function update_cost(){
    console.log("Total:" + String(
            parseInt(adults.value) * 65
            + parseInt(children.value) * 35
            + parseInt(oaps.value) * 45
        ))
}




let adults = document.getElementById("id_hotel_booking_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_booking_children");
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_hotel_booking_oap");
oaps.addEventListener("change", update_cost)