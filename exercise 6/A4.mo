model A4
  import SI = Modelica.SIunits;
  parameter SI.Time T_p = 5e-3;
  parameter SI.Frequency f = 50;
  parameter SI.Voltage u_dach = 200;
  Modelica.Electrical.Analog.Basic.Inductor inductor1(i(fixed = true, start = 20)) annotation(
    Placement(visible = true, transformation(origin = {66, 30}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor resistor1 annotation(
    Placement(visible = true, transformation(origin = {24, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-80, -12}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.ConstantVoltage constantVoltage1(V = 300) annotation(
    Placement(visible = true, transformation(origin = {-80, 30}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  ModSimBib.vierqst vierqst1(T_p = 1e-3) annotation(
    Placement(visible = true, transformation(origin = {-4, 30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Cosine cosine(amplitude = 200, freqHz = 50)  annotation(
    Placement(visible = true, transformation(origin = {-62, 64}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(ground1.p, constantVoltage1.n) annotation(
    Line(points = {{-80, -2}, {-80, 20}}, color = {0, 0, 255}));
  connect(resistor1.n, inductor1.p) annotation(
    Line(points = {{34, 40}, {66, 40}, {66, 40}, {66, 40}}, color = {0, 0, 255}));
  connect(resistor1.p, vierqst1.p2) annotation(
    Line(points = {{14, 40}, {6, 40}}, color = {0, 0, 255}));
  connect(vierqst1.p1, constantVoltage1.p) annotation(
    Line(points = {{-14, 40}, {-80, 40}}, color = {0, 0, 255}));
  connect(constantVoltage1.n, vierqst1.n1) annotation(
    Line(points = {{-80, 20}, {-14, 20}}, color = {0, 0, 255}));
  connect(vierqst1.n2, inductor1.n) annotation(
    Line(points = {{6, 20}, {66, 20}}, color = {0, 0, 255}));
  connect(vierqst1.u_e, cosine.y) annotation(
    Line(points = {{-16, 30}, {-14.5, 30}, {-14.5, 64}, {-51, 64}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "3.2.2")),
    experiment(StartTime = 0, StopTime = 15e-3, Tolerance = 1e-06, Interval = 3.75e-05),
    Diagram(coordinateSystem(initialScale = 0.1)));
end A4;
