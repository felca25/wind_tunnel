# Wind Tunnel

This is a repository that is an OpenFOAM case for running turbine rotor geometries. It uses SnappyHexMesh to create the mesh from the rotor STL geometry.
Then the user can copy the geometry from `mesh/constant/polyMesh` to the steady directory.
The steady directory runs a steady simulation using the Multiple Frame of Reference (MRF) approach with the k-omega SST turbulence model, this creates a steady state result, 
that can be used to initialize unsteady simulations so that they run quicker.

## Usage
1. Clone Repository in a directory
```bash
  git clone https://github.com/felca25/wind_tunnel/
```
3. Go to the mesh directory;
```bash
cd mesh
```
4. Load the geometry to `mesh/constant/geometry`;
```bash
cp <path to your STL geometry> ./constant/geometry
```
5. Run AllMesh from Terminal;
```bash
./Allrun
```
6. Check Results;
```bash
checkMesh
```
7. Copy `constant/polyMesh` directory with the most current mesh to `steady/constant/`;
```bash
cp -r ./constant/polyMesh ../steady/constant/
```
8. Ajust `controlDict`;
9. Run steady state simulation;
