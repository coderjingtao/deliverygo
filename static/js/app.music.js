$(document).ready(function(){
  var playlist = [
    {
      title:"旅行的意义",
      artist:"Jingtao Liu",
      mp3:"../static/videos/travel.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"蝴蝶花",
      artist:"Jingtao Liu",
      mp3:"../static/videos/bufferfly.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"微幸福",
      artist:"Jingtao Liu",
      mp3:"../static/videos/happiness.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"七月",
      artist:"Jingtao Liu",
      mp3:"../static/videos/july.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"啦啦歌",
      artist:"Jingtao Liu",
      mp3:"../static/videos/lala.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"下一个天亮",
      artist:"Jingtao Liu",
      mp3:"../static/videos/nextdawn.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"爱的废墟",
      artist:"Jingtao Liu",
      mp3:"../static/videos/loveruin.mp3",
      poster: "../static/images/jing.jpg"
    },
    {
      title:"hello world",
      artist:"deliverygo.ga",
      mp3:"http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
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