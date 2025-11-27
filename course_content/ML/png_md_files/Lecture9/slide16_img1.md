The image contains two sections representing different neural network structures. 

**Left Section: Linear Model with Bias**
- Title: "Linear model with bias" written above the diagram.
- Oval labeled "1" at the leftmost side with an arrow pointing right towards the central node.
- Four ovals labeled: \( x_{i1} \), \( x_{i2} \), \( x_{i3} \), followed by "...", \( x_{in} \), each having an upward arrow pointing towards the central oval.
- Central oval labeled \( y_i \) with arrows pointing back to each of the input ovals, indicating incoming connections. 
- All arrows in this section are black, except for one blue arrow originating from the "1" oval pointing directly to \( y_i \).

**Right Section: Multilayer Neural Network with Bias**
- Topmost row: An oval labeled \( y_i \) in the top center. Arrows are pointing to it from intermediate level nodes.
- Second row from the top: Five ovals labeled \( h(z_{i1}^{(2)}) \), \( h(z_{i2}^{(2)}) \), \( h(z_{i3}^{(2)}) \), continuing with "...", \( h(z_{ik}^{(2)}) \). Each has an upward arrow pointing to \( y_i \) and a downward arrow from the previous layer.
- Third row: Five ovals labeled \( z_{i1}^{(2)} \), \( z_{i2}^{(2)} \), \( z_{i3}^{(2)} \), continuing with "...", \( z_{ik}^{(2)} \). Arrows point to the intermediate layer above and originate from the layer below.
- Fourth row: Five ovals labeled \( h(z_{i1}^{(1)}) \), \( h(z_{i2}^{(1)}) \), \( h(z_{i3}^{(1)}) \), continuing with "...", \( h(z_{ik}^{(1)}) \). Each connects to the layer above and is connected to the values in the row below.
- Fifth row: Five ovals labeled \( z_{i1}^{(1)} \), \( z_{i2}^{(1)} \), \( z_{i3}^{(1)} \), continuing with "...", \( z_{ik}^{(1)} \). Arrows indicate connections to the intermediate layers above and are fed from bottom inputs.
- Bottommost row: Oval labeled "1" on the left. Five sequential ovals labeled \( x_{i1} \), \( x_{i2} \), \( x_{i3} \), continuing with "...", \( x_{id} \).
- Blue arrows originate from oval labeled "1" on the bottom left, connecting to the intermediate ovals in the first and second \( z \) layers.
- Black connections depict neural pathways across different layers moving from the bottommost input row up to the output labeled \( y_i \).