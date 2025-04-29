$(document).ready(function() {
    let inputCount = 1;

    $('#addInput').click(function() {
        $('#dynamicInputs').append(`<input type="text" name="input${inputCount}" placeholder="Введите значение">`);
        inputCount++;
    });

    var map = L.map('map').setView([53.9006, 27.5590], 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap'
    }).addTo(map);

    var drawnArea = [];

    function onMapClick(e) {
        drawnArea.push([e.latlng.lat, e.latlng.lng]);
        if (drawnArea.length > 1) {
            var polygon = L.polygon(drawnArea, {color: 'red'}).addTo(map);
            $('#areaInput').val(JSON.stringify(drawnArea));
        }
    }
    map.on('click', onMapClick);
});