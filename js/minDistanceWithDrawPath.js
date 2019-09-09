module.exports = {
  setup: function(api) {
    api.setSize(320,320);
    var curve = new api.Bezier([
      {x:x,y:y}
    ]);
    api.setCurve(curve);
    api._lut = curve.getLUT();
  },

  findClosest: function(LUT, p, dist) {
    var i,
        end = LUT.length,
        d,
        dd = dist(LUT[0],p),
        f = 0;
    for(i=1; i<end; i++) {
      d = dist(LUT[i],p);
      if(d<dd) {f = i;dd = d;}
    }
    return f/(end-1);
  },

  draw: function(api, curve) {
    api.reset();
    api.drawSkeleton(curve);
    api.drawCurve(curve);
    if (api.mousePt) {
      api.setColor("red");
      api.setFill("red");
      api.drawCircle(api.mousePt, 3);
      // naive t value
      var t = this.findClosest(api._lut, api.mousePt, api.utils.dist);
      // no real point in refining for illustration purposes
      var p = curve.get(t);
      api.drawLine(p, api.mousePt);
      api.drawCircle(p, 3);
      api.text("t = "+api.utils.round(t,2), p, {x:10, y:3});
    }
  },

  onMouseMove: function(evt, api) {
    api.mousePt = {x: evt.offsetX, y: evt.offsetY };
    api._lut = api.curve.getLUT();
  }
};