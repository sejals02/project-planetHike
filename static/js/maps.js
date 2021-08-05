function initMap(){  

  //get p calss loc data
  const loc  = document.querySelectorAll('.loc');

  //split the string by space and store in an array
  const locArry = loc[0].textContent.split(" ");

  //access the lat and lng indices
  const lat = locArry[2];
  const lng = locArry[4];

  //convert lat and lang to float for trailCoords usage
  const newlat = parseFloat(lat.substring(0,lat.length-1))
  //console.log (newlat)  

  const newlng = parseFloat(lng.substring(0,lng.length-1))
  //console.log (newlng)
  
  const trailCoords = {
    lat: newlat,
    lng: newlng
  };
  
  const basicMap = new google.maps.Map(
    document.querySelector('#map'),
    {
      center: trailCoords,
      zoom: 11
    }
  );

  const trailMarker = new google.maps.Marker({
    position: trailCoords,
    title: 'Trail',
    icon: {
      url: '/static/images/girl_hiker.svg',
      size: new google. maps. Size(50, 50),
      scaledSize: new google. maps. Size(75, 50)
    },
    map: basicMap
  });
  
  trailMarker.addListener('click', () => {
    alert('Enjoy your hike!');
  });

  const trailInfo = new google.maps.InfoWindow({
    content: '<h3>Trail</h3>'
  });

  trailInfo.open(basicMap, trailMarker);
  
 }  