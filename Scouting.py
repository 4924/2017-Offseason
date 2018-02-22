<html ng-app>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.7/angular.min.js"></script>
  </head>
<div id="team"><h1></h1></div>
<div id="auto"><h1>Autonomous</h1>
<h1 id="line">Line: </h1>
<h1 id="switch">Switch: </h1>
<h1 id="scale">Scale: </h1>
</div>

<div id="tele"><h1>Tele-operated</h1>
<h1 id="tSwitch">Switch: </h1>
<h1 id="tScale">Scale: </h1>
<h1 id="vault">Vault: </h1>
<h1 id="climb">Climb: </h1>
</div>

<style>
#team {
  text-align: center;
  position: absolute; top: 2%; right: 39%;
  background-color: #FCFEFA;
  border-top: ridge 1em white;
  border-bottom: ridge 1em black;
  border-left: ridge 1em white;
  border-right: ridge 1em black;
  width: 20%;
  height: 10%;
}
body{
background-color: #008080;
font-family: "Comic Sans MS", "Comic Sans", cursive; 
}
/*percents*/
#auto {
  text-align: center;
  background-color: #FCFEFA;
  position: absolute; left: 2%; top: 15%;
  border-top: ridge 1em white;
  border-bottom: ridge 1em black;
  border-left: ridge 1em white;
  border-right: ridge 1em black;
  width: 30%;
  height: 40%;
}
#line {
  position: inherit; left: 2%; top: 10%;
  height: 11%;
}
#Switch {
  position: inherit; left: 2%; top: 30%;
  height: 11%;
}
#scale{
  position: inherit; left: 2%; top: 50%;
height: 11%;
}
#tele {
  text-align: center;
  background-color: #FCFEFA;
  position: absolute; right: 2%; top: 15%;
  border-top: ridge 1em white;
  border-bottom: ridge 1em black;
  border-left: ridge 1em white;
  border-right: ridge 1em black;
  width: 30%;
  height: 40%;
}
#tSwitch{
 position: inherit; left: 2%; top: 10%; 
}
#tScale {
 position: inherit; left: 2%; top: 30%;
  height: 11%;
}
#vault {
 position: inherit; left: 2%; top: 50%;;
  height: 11%;
}
#climb{
  position: inherit; left: 2%; top: 70%;
  height: 11%;
}
#low-ball-score{
  position: inherit; left: 68%; top: 23%;
}
#pvault {
  position: inherit; left: 81%; top: 30%;
  width: 6%;
  height: 11%;
}
#mvault {
  position: inherit; left: 69%; top: 30%;
  width: 6%;
  height: 11%;
}
#ground{
  position: inherit; left: 19%; bottom: 30%;
}
#groundcube{
  position: inherit; left: 12%; bottom: 7%;
}
#pground{
  position: inherit; left: 25%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#mground{
  position: inherit; left: 13%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#portal{
  position: inherit; left: 47.5%; bottom: 30%;
}
#portalcube{
  position: inherit; left: 40%; bottom: 7%;
}
#pportal{
  position: inherit; left: 53%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#mportal{
  position: inherit; left: 41%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#pile{
  position: inherit; left: 76.5%; bottom: 30%;
}
#pilecube{
  position: inherit; left: 68%; bottom: 7%;
}
#ppile{
  position: inherit; left: 81%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#mpile{
  position: inherit; left: 69%; bottom: 16%;
  width: 6%;
  height: 11%;
}
#autoswitch {
  width: 25%;
  height: 20%;
  font-size: 1.3em;
  position: inherit;; left: 10%; top: 15%;
  border: 0px;
}
#auto-switch-score {
  position: inherit;; left: 12.5%; top: 35%;
}
#paswitch{
 width: 8%;
 height: 15%;
 position: inherit;; left: 26%; top: 43%;
}
#maswitch{
 width: 8%;
 height: 15%;
 position: inherit;; left: 11%; top: 43%;
}
#autoscale {
  width: 25%;
  height: 20%;
  font-size: 1.3em;
  position: inherit;; right: 10%; top: 15%;
  border: 0px;
}
#auto-scale-score {
  position: inherit;; right: 12.5%; top: 35%;
}
#pascale {
 width: 8%;
 height: 15%;
 position: inherit;; right: 11%; top: 43%;
}
#mascale {
 width: 8%;
 height: 15%;
 position: inherit;; right: 26%; top: 43%;
}
#autoline {
  width: 20%;
  height: 45%;
  font-size: 1em;
  position: inherit;; left: 40%; top: 15%;
}
#aleft {
  position: inherit;; left: 15%; bottom: 10%;
}
#aright {
  position: inherit;; left: 65%; bottom: 10%;
}
#amiddle {
  position: inherit;; left: 40%; bottom: 10%;  
}
#lock {
  width: 15%;
  height: 15%;
  border: 2px solid black;
  font-size: 5em;
  -webkit-text-stroke: 2.0px #000000;
  position: absolute; right: 2%; bottom: 3%;
  color: white;
  text-shadow: 0px 15px 5px rgba(0,0,0,0.1),
  10px 20px 5px rgba(0,0,0,0.05),
 -10px 20px 5px rgba(0,0,0,0.05);
  background-color: white;
  font-weight: 900;
}
#mechanum {
  width: 20%;
  height: 24%;
  font-size: 1.3em;
  position: inherit; left: 4%; top: 30%;
  border: 0px;
}
#foul {
position: inherit; left: 4%; top: 50%;
}
#pfoul {
position: inherit; bottom: 22%; left: 17%;
width: 6%;
height: 11%;
}
#mfoul {
position: inherit; bottom: 22%; left: 5%;
width: 6%;
height: 11%;
}
#tfoul {
position: inherit; left: 28%; top: 50%;
}
#ptfoul {
position: inherit; bottom: 22%; left: 41%;
width: 6%;
height: 11%;
}
#mtfoul {
position: inherit; bottom: 22%; left: 29%;
width: 6%;
height: 11%;
}
#ycard {
position: inherit; left: 52%; top: 50%;
}
#pycard {
position: inherit; bottom: 22%; right: 29%;
width: 6%;
height: 11%;
}
#mycard {
position: inherit; bottom: 22%; right: 41%;
width: 6%;
height: 11%;
}
#rcard {
position: inherit; left: 76%; top: 50%;
}
#prcard {
position: inherit; bottom: 22%; right: 5%;
width: 6%;
height: 11%;
}
#mrcard {
position: inherit; bottom: 22%; right: 17%;
width: 6%;
height: 11%;
}
#ramp {
 width: 20%;
 height: 20%;
 font-size: 1em;
 position: inherit; left: 12%; top: 73%;
 border: 1px;
}
#bar{
 width: 20%;
 height: 20%;
 font-size: 1em;
 position: inherit; left: 40%; top: 73%;
 border: 1px;
}
#baryes{
 width: 20%;
 height: 14%;
 font-size: 1em;
 position: inherit; left: 40%; top: 15%;
}
#barno{
 width: 20%;
 height: 14%;
 font-size: 1em;
 position: inherit; left: 40%; top: 35%;
}
#baryesb{
 width: 20%;
 height: 14%;
 font-size: 1em;
 position: inherit; left: 40%; top: 55%;
}
#pleb{
 width: 20%;
 height: 20%;
 font-size: 1em;
 position: inherit; right:  12%; top: 73%;
 border: 1px;
}
#groundball {
  width: 20%;
  height: 24%;
  font-size: 1.3em;
  position: inherit; left: 28%; top: 30%;
  border: 0px;
}
#hopper{
  width: 20%;
  height: 24%;
  font-size: 1.3em;
  position: inherit; left: 52%; top: 30%;
  border: 0px;
}
#macrogear{
  width: 20%;
  height: 24%;
  font-size: 1.3em;
  position: inherit; left: 76%; top: 30%;
  border: 0px;
}
.elias{
  width: 20%;
  height: 20%;
  font-size: 1em;
  border: none;
  background-color: Transparent;
  background-image: none; 
  cursor:pointer;
  background-repeat:no-repeat;
  overflow: hidden;
  outline:none;
}
.aposition{
  width: 20%;
  height: 20%;
  font-size: 1em;
}
.score{
  width: 20%;
  height: 20%;
  border: 0px solid black;
  padding-top: 10px;
}
.selected{
  border: 2px solid black;
  padding: 0;
  outline: 0;
}
.selected:hover{
  border: 2px solid black;
  padding: 0;
  outline: 0;
}
.selected:active{
  border: 2px solid black;
  padding: 0;
  outline: 0;
}
.selected:focus{
  border: 2px solid black;
  padding: 0;
  outline: 0;
}
button{
  padding: 0px;
}
input {
  font-size: 2.4em;
  background-color: transparent;
  text-align: center;
  border-width: 0;
  width: 100%;
  margin: 0 0 .1em 0;
  color: #fff;
}
label {
  display: block;
  font-size: .8em;
}
button {
  /* basics */
  color: #0;
  background-color: #ffffff;
}
.box {
  /* basics */
  background-color: #444;
  color: #ffffff;
    text-align: center;
  /* rounded corners */
</style>           