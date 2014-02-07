// JavaScript Document
//Physical Engine
//Acceleration

Vector = function(x, y) { this.x = x; this.y = y; };
 
Vector.prototype = {
    copy: function() { return new Vector(this.x, this.y); },
    length: function() { return Math.sqrt(this.x * this.x + this.y * this.y); },
    sqrLength: function() { return this.x * this.x + this.y * this.y; },
    normalize: function() { var inv = 1 / this.length(); return new Vector(this.x * inv, this.y * inv); },
    negate: function() { return new Vector(-this.x, -this.y); },
    add: function(v) { return new Vector(this.x + v.x, this.y + v.y); },
    subtract: function(v) {return new Vector(this.x - v.x, this.y - v.y); },
    multiply: function(f) { return new Vector(this.x * f, this.y * f); },
    divide: function(f) { var invf = 1 / f; return new Vector(this.x * invf, this.y * invf); },
    dot: function(v) { return this.x * v.x + this.y * v.y; }
};

function move_acc(block,startpoint,endpoint,time){
	var counter=0;
	var startpoint=new Vector(startpoint[0],startpoint[1]);
	var position=startpoint;
	var endpoint=new Vector(endpoint[0],endpoint[1]);
	var distance=endpoint.subtract(startpoint);
	var acc=distance.multiply(2/time/time);
	var v=acc.multiply(time);
	var driver=setInterval(function(){
		counter=counter+1;
		position=position.add(v.multiply(2));
		$('#'+block).css("left",position.x);
		$('#'+block).css("top",position.y);
		v=v.subtract(acc.multiply(2));
		if((position.subtract(endpoint)).sqrLength()<5||counter>1000){
			clearInterval(driver);
		}
	},2);
}

//Viscosity
function move_vis(block,startpoint,endpoint,time){
	var counter=0;
	var startpoint=new Vector(startpoint[0],startpoint[1]);
	var position=startpoint;
	var endpoint=new Vector(endpoint[0],endpoint[1]);
	var distance=endpoint.subtract(startpoint);
	var vis=1/time;
	var v=distance.multiply(vis);
	var driver=setInterval(function(){
		counter=counter+1;
		position=position.add(v.multiply(2));
		$('#'+block).css("left",position.x);
		$('#'+block).css("top",position.y);
		v=v.subtract(v.multiply(vis*2));
		if((position.subtract(endpoint)).sqrLength()<5||counter>1000){
			clearInterval(driver);
		}
	},2);
}