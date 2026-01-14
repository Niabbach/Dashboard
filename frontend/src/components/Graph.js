export class Graph {
  constructor(container, name, time, data){
    this.name = name;
    this.time = time;
    this.data = data;
    this.svg = d3.select(container)
      .append("svg")
      .attr("width",500)
      .attr("height",300);
  }

  render(i){
    this.svg.selectAll("*").remove();

    const x = d3.scaleLinear().domain([0,this.time.length-1]).range([50,470]);
    const y = d3.scaleLinear()
      .domain(d3.extent(this.data))
      .range([250,50]);

    const line = d3.line()
      .x((d,i)=>x(i))
      .y(d=>y(d));

    this.svg.append("path")
      .datum(this.data)
      .attr("fill","none")
      .attr("stroke","#00f6ff")
      .attr("stroke-width",2)
      .attr("d",line);

    this.svg.append("circle")
      .attr("cx",x(i))
      .attr("cy",y(this.data[i]))
      .attr("r",6)
      .attr("fill","red");

    this.svg.append("text")
      .attr("x",10)
      .attr("y",20)
      .attr("fill","white")
      .text(`${this.name} @ t=${this.time[i].toFixed(2)}`);
  }
}
