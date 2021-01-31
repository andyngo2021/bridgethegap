var mymap = L.map('mapid').setView([33.7760, -118.260], 13);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
    }).addTo(mymap);


let address_bar = document.getElementById("address-form");
function check()
{
    let zip = address_bar.value;
    let btn = document.getElementById("submit-btn");
    if (zip.length == 5 && isNumeric(zip))
    {
        btn.disabled = false;
    }
    else
    {
        btn.disabled = true;
    }
}

function isNumeric(value)
{
    // regex!??! POG!?!?
    return /^-?\d+$/.test(value);
}