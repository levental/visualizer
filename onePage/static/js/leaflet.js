/**
 * Created by simlev81 on 12/4/14.
 */

var layer = L.geoJson();
map.addLayer(layer);
$.getJSON("{% http://api.civicapps.org/parks/near/-122.693148,45.557742?count=2 'schoolsPDX' %}", function (schoolsPDX) {
    layer.addData(data);
});
