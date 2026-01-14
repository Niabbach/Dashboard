import { Graph } from "./components/Graph.js";
import { CockpitUI } from "./ui.js";

fetch("..data/Comparison_timeseries.json").then(r=>r.json()).then(json=>{

  const groups = {};
  Object.keys(json.signals).forEach(n=>{
    const root = n.split(".")[0];
    if(!groups[root]) groups[root] = [];
    groups[root].push(n);
  });

  let graph = null;

  const onSignalChange = signal=>{
    document.getElementById("graph").innerHTML="";
    graph = new Graph("#graph", signal, json.time, json.signals[signal]);
    graph.render(0);
  };

  const onTimeChange = i=>{
    graph?.render(i);
  };

  new CockpitUI(groups, json.time, onSignalChange, onTimeChange);
});
