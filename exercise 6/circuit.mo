model Circuit
  Modelica.Electrical.Analog.Sources.SupplyVoltage supplyVoltage(Vns = 0, Vps = 10) annotation(
    Placement(visible = true, transformation(origin = {-50, 10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor resistor(R = 10) annotation(
    Placement(visible = true, transformation(origin = {10, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Inductor inductor(L = 1) annotation(
    Placement(visible = true, transformation(origin = {70, 10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Ideal.IdealDiode diode annotation(
    Placement(visible = true, transformation(origin = {30, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-50, -52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(diode.n, resistor.n) annotation(
    Line(points = {{30, 20}, {30, 50}, {20, 50}}, color = {0, 0, 255}));
  connect(ground.p, supplyVoltage.pin_n) annotation(
    Line(points = {{-50, -42}, {-50, 0}}, color = {0, 0, 255}));
  connect(diode.p, supplyVoltage.pin_n) annotation(
    Line(points = {{30, 0}, {30, -20}, {-50, -20}, {-50, 0}}, color = {0, 0, 255}));
//uses(Modelica(version = "4.0.0"))
  connect(inductor.p, resistor.n) annotation(
    Line(points = {{70, 20}, {70, 50}, {20, 50}}, color = {0, 0, 255}));
  connect(inductor.n, supplyVoltage.pin_n) annotation(
    Line(points = {{70, 0}, {70, -20}, {-50, -20}, {-50, 0}}, color = {0, 0, 255}));
  connect(supplyVoltage.pin_p, resistor.p) annotation(
    Line(points = {{-50, 20}, {-50, 50}, {0, 50}}, color = {0, 0, 255}));
  annotation(
    Diagram,
    uses(Modelica(version = "4.0.0")));
end Circuit;
