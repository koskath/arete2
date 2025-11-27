The image contains both textual equations and a neural network diagram with annotations:

1. **Top Left - Equations:**
   - **Linear Model:**
     - The equation is written as:
       \[
       \hat{y}_i = w^T x_i
       \]
   
   - **Neural Network with 1 Hidden Layer:**
     - The equation is:
       \[
       \hat{y}_i = v^T h(Wx_i)
       \]
     - A blue bracket below denotes \( z_i \).
   
   - **Neural Network with 2 Hidden Layers:**
     - The equation is:
       \[
       \hat{y}_i = v^T h(W^{(2)} h(W^{(1)} x_i))
       \]
     - Blue brackets are below \( z_i^{(1)} \) and \( z_i^{(2)} \).
   
   - **Neural Network with 3 Hidden Layers:**
     - The equation is:
       \[
       \hat{y}_i = v^T h(W^{(3)} h(W^{(2)} h(W^{(1)} x_i)))
       \]
     - Blue brackets are below \( z_i^{(1)} \), \( z_i^{(2)} \), and \( z_i^{(3)} \).

2. **Right Side - Neural Network Diagram:**
   - Topmost node: \( y_i \), with three arrows pointing to it.
   - Below it, a second layer of circles labeled as \( h(z_{i1}^{(2)}) \), \( h(z_{i2}^{(2)}) \), \( h(z_{i3}^{(2)}) \), and \( h(z_{ik}^{(2)}) \). These have arrows pointing upwards towards \( y_i \).
   - The circles connect to circles in a lower layer labeled as \( z_{i1}^{(2)} \), \( z_{i2}^{(2)} \), \( z_{i3}^{(2)} \), \( z_{ik}^{(2)} \).
   - Annotated in green: "Second 'layer' of latent features" on the left, with an arrow pointing to this layer.
   - Below, the first hidden layer consisting of circles labeled \( h(z_{i1}^{(1)}) \), \( h(z_{i2}^{(1)}) \), \( h(z_{i3}^{(1)}) \), \( h(z_{ik}^{(1)}) \), connecting below to \( z_{i1}^{(1)} \), \( z_{i2}^{(1)} \), \( z_{i3}^{(1)} \), and \( z_{ik}^{(1)} \).
   - Connections through lines between circles illustrate layer dependencies. Black lines connect the first hidden layer to the input nodes, while blue lines connect higher layers.
   - Input layer nodes labeled \( x_{i1} \), \( x_{i2} \), \( x_{i3} \), ..., and \( x_{id} \).
   - Annotated in green: "You can add more 'layers' to go 'deeper'" with an arrow pointing upwards toward higher layers.

These various components depict a deep learning network architecture, illustrating increasing complexity with added layers.