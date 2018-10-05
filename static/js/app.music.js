$(document).ready(function(){
  var playlist = [
    {
      title:"DeliveryGo",
      artist:"deliverygo.ga",
      mp3:"http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
      poster: "images/2.jpg"
    },
    {
      title:"旅行的意义",
      artist:"Jingtao Liu",
      mp3:"../static/videos/travel.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"DeliveryGo",
      artist:"deliverygo.ga",
      mp3:"http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
      poster: "images/2.jpg"
    },
    {
      title:"旅行的意义",
      artist:"Jingtao Liu",
      mp3:"../static/videos/travel.mp3",
      poster: "../static/images/jing.jpg"
    },
  ];
  
  var cssSelector = {
    jPlayer: "#jquery_jplayer",
    cssSelectorAncestor: ".music-player"
  };
  
  var options = {
    swfPath: "Jplayer.swf",
    supplied: "ogv, m4v, oga, mp3"
  };
  
  var myPlaylist = new jPlayerPlaylist(cssSelector, playlist, options);
  
});