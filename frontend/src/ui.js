export class CockpitUI {
  constructor(groups, time, onSignalChange, onTimeChange){
    this.groups = groups;
    this.time   = time;
    this.onSignalChange = onSignalChange;
    this.onTimeChange   = onTimeChange;

    this.compSel = document.getElementById("component");
    this.sigSel  = document.getElementById("signal");
    this.slider  = document.getElementById("time");

    this.init();
  }

  init(){
    Object.keys(this.groups).forEach(c=>{
      this.compSel.innerHTML += `<option value="${c}">${c}</option>`;
    });

    this.compSel.onchange = ()=>this.loadSignals();
    this.sigSel.onchange  = ()=>this.onSignalChange(this.sigSel.value);

    this.slider.max = this.time.length - 1;
    this.slider.oninput = e => this.onTimeChange(+e.target.value);

    this.loadSignals();
  }

  loadSignals(){
    const c = this.compSel.value;
    this.sigSel.innerHTML = "";

    this.groups[c].forEach(s=>{
      this.sigSel.innerHTML += `<option value="${s}">${s}</option>`;
    });

    this.onSignalChange(this.sigSel.value);
  }
}
