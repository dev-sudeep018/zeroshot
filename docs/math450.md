# Mathematics expansion to the 450-lesson curriculum

This batch adds 100 distinct runnable lessons, m60–m159: 80 beginner and 20 intermediate. Each has a documented input/output contract, three worked examples, two hints, an explanation, a starter, a reference implementation, and executable public tests. All 1,006 public cases pass natively, all 300 displayed examples match execution, and every starter fails its checks before implementation.

Beginner lessons cover calibrated sensor tables, masks, spatial grids, time-series summaries, robust statistics, coordinate geometry, finite probability, and counting. Intermediate lessons cover root-finding, integration, iterative solvers, and simple model diagnostics. These require reasoning about real numeric inputs and boundaries rather than printing output or recalling syntax.

## Provenance

The exercise prose, implementations, examples, and fixtures are original ZeroShot work (the project was formerly named Project Mastery). Package metadata includes conceptual reading links to the NumPy and Python documentation. Those links provide further reading; no lesson text or implementation was imported from another learning platform.

## Validation

`python -m unittest discover -s tests/python -p test_math450.py -v` passes 25 independent tests. They cover all 100 lesson IDs with conservation laws, exhaustive small enumerations, closed-form identities, geometric invariants, solver residuals, finite differences, and regressions for numerical boundary cases.

The targeted native content gate passes 100 packages and 1,006 public cases, including starter rejection, sample counts, and trivial wrong answers. The three publication checks from `test_catalog_450.py`, restricted to this batch, pass all displayed examples, sample/example correspondence, editor-size limits, and canned-answer rejection.

Specific hardening includes preserving empty (0, 2) output shapes in zero-crossing fixtures; comparing bisection signs directly to avoid underflow from products of tiny coefficients; computing the R² ratio with scaled deviations; and requiring exact large integer counts rather than tolerance-based acceptance of off-by-one answers.

Browser/Pyodide execution and whole-application CI remain integration gates. These native results do not claim either has passed.

| ID   | Lesson                                               | Difficulty   | Public cases |
| ---- | ---------------------------------------------------- | ------------ | -----------: |
| m60  | Calibrate and Limit Sensor Channels                  | beginner     |           10 |
| m61  | Summarize Only Observed Cells                        | beginner     |           10 |
| m62  | Aggregate a Grid into Partial Blocks                 | beginner     |           10 |
| m63  | Accumulate Repeated Grid Measurements                | beginner     |           10 |
| m64  | Pack a Symmetric Measurement Matrix                  | beginner     |           10 |
| m65  | Convert Counts into Conditional Rows                 | beginner     |           10 |
| m66  | Summarize a Matrix by Diagonal Offset                | beginner     |           10 |
| m67  | Answer Rectangular Sum Queries                       | beginner     |           10 |
| m68  | Locate Pixels inside Image Tiles                     | beginner     |           10 |
| m69  | Build an Independence Baseline for a Table           | beginner     |           10 |
| m70  | Measure Four-Connected Grid Regions                  | beginner     |           10 |
| m71  | Find Peaks without Double-Counting Plateaus          | beginner     |           10 |
| m72  | Measure Change on an Uneven Time Grid                | beginner     |           10 |
| m73  | Smooth a Signal at Its Boundaries                    | beginner     |           10 |
| m74  | Separate a Forecast from Its Update                  | beginner     |           10 |
| m75  | Remove and Restore a Seasonal Lag                    | beginner     |           10 |
| m76  | Compare a Signal with Its Delayed Self               | beginner     |           10 |
| m77  | Find Sign Changes through Exact Zeros                | beginner     |           10 |
| m78  | Accumulate Area on an Uneven Grid                    | beginner     |           10 |
| m79  | Resample between Known Measurements                  | beginner     |           10 |
| m80  | Reduce Outlier Influence by Trimming                 | beginner     |           10 |
| m81  | Flag Outliers Using Median Deviations                | beginner     |           10 |
| m82  | Explain Which Tail Contains an Outlier               | beginner     |           10 |
| m83  | Combine Multiplicative Growth Factors                | beginner     |           10 |
| m84  | Average Rates over Equal Distances                   | beginner     |           10 |
| m85  | Compare Typical and Peak Signal Size                 | beginner     |           10 |
| m86  | Compare Dispersion across Units                      | beginner     |           10 |
| m87  | Measure Asymmetry and Tail Shape                     | intermediate |           10 |
| m88  | Make Histogram Areas Sum to One                      | beginner     |           10 |
| m89  | Transfer Histogram Mass to New Bins                  | intermediate |           10 |
| m90  | Describe Concentration with a Lorenz Curve           | beginner     |           10 |
| m91  | Report Every Most Frequent Value                     | beginner     |           10 |
| m92  | Compute Every Leave-One-Out Mean                     | beginner     |           10 |
| m93  | Separate Within-Group Scatter from Group Means       | beginner     |           10 |
| m94  | Partition Variation between Groups                   | beginner     |           10 |
| m95  | Measure How Concentrated Weights Are                 | beginner     |           10 |
| m96  | Build a Bounded Interval for a Success Rate          | intermediate |           10 |
| m97  | Audit Relative Errors near Zero                      | beginner     |           10 |
| m98  | Compare Forecast Errors with a Naive Baseline        | beginner     |           10 |
| m99  | Keep Forecast Training before Validation             | beginner     |           10 |
| m100 | Find the Nearest Point on a Segment                  | beginner     |           10 |
| m101 | Measure Triangle Orientation and Size                | beginner     |           10 |
| m102 | Walk a Closed Polygon                                | beginner     |           10 |
| m103 | Measure Perpendicular Distance to a Line             | beginner     |           10 |
| m104 | Describe a Point Cloud with a Bounding Box           | beginner     |           10 |
| m105 | Rotate Points around a Chosen Pivot                  | beginner     |           10 |
| m106 | Convert Cartesian Positions to Canonical Polar Form  | beginner     |           10 |
| m107 | Locate a Point Relative to a Triangle                | intermediate |           10 |
| m108 | Intersect Two Nonparallel Segments                   | intermediate |           10 |
| m109 | Reflect Points across an Implicit Line               | beginner     |           10 |
| m110 | Clip a Segment to a Rectangle                        | intermediate |           10 |
| m111 | Sample a Path by Traveled Distance                   | beginner     |           10 |
| m112 | Split a Vector into Parallel and Perpendicular Parts | beginner     |           10 |
| m113 | Construct an Oriented Plane from Three Points        | intermediate |           10 |
| m114 | Rotate a 3D Vector around an Axis                    | intermediate |           10 |
| m115 | Classify Points against a Polygon Boundary           | beginner     |           10 |
| m116 | Recover a Triangle from Side Lengths                 | beginner     |           10 |
| m117 | Summarize a Planar Mass Distribution                 | intermediate |           10 |
| m118 | Measure Covered Length without Double Counting       | beginner     |           10 |
| m119 | Measure Overlap between Two Disks                    | intermediate |           10 |
| m120 | Combine Events in a Finite Sample Space              | beginner     |           10 |
| m121 | Combine Independent Discrete Measurements            | beginner     |           10 |
| m122 | Count Successes in a Sample without Replacement      | beginner     |           10 |
| m123 | Track the First Success before a Deadline            | beginner     |           10 |
| m124 | Count Events under a Poisson Model                   | beginner     |           10 |
| m125 | Turn Fixed Uniform Draws into Categories             | beginner     |           10 |
| m126 | Predict How Many Categories Will Be Seen             | beginner     |           10 |
| m127 | Find the Chance of a Repeated Label                  | beginner     |           10 |
| m128 | Combine Three Overlapping Events                     | intermediate |           10 |
| m129 | Condition a Joint Table on Selected Columns          | beginner     |           10 |
| m130 | Separate Within-Case and Between-Case Uncertainty    | beginner     |           10 |
| m131 | Move Probability through a Transition Table          | beginner     |           10 |
| m132 | Track Survival before an Absorbing State             | intermediate |           10 |
| m133 | Separate No Event, One Event and Several Events      | beginner     |           10 |
| m134 | Count Dice Outcomes before Normalizing               | beginner     |           11 |
| m135 | Decode a Combination from Its Lexicographic Rank     | intermediate |           10 |
| m136 | Measure Disorder in a Permutation                    | beginner     |           10 |
| m137 | Count Monotone Routes around Blocked Cells           | beginner     |           11 |
| m138 | Count Assignments with No Fixed Points               | beginner     |           11 |
| m139 | Estimate How Many Boxes Stay Empty                   | intermediate |           10 |
| m140 | Evaluate a Polynomial and Its Slope Together         | beginner     |           10 |
| m141 | Integrate a Polynomial between Bounds                | beginner     |           10 |
| m142 | Keep a Root inside a Shrinking Bracket               | intermediate |           12 |
| m143 | Trace Newton Updates toward a Square Root            | beginner     |           10 |
| m144 | Integrate Evenly Spaced Samples with Simpson Weights | beginner     |           10 |
| m145 | Recover a Quadratic through Three Samples            | beginner     |           10 |
| m146 | Step through a First-Order Cooling Model             | beginner     |           10 |
| m147 | Update a Root Estimate from Two Function Values      | intermediate |           10 |
| m148 | Update a Linear Solve without Reusing New Values     | intermediate |           10 |
| m149 | Solve a Small System with Partial Pivoting           | intermediate |           10 |
| m150 | Score Binary Features with Both Outcomes             | intermediate |           10 |
| m151 | Fit a Line and Explain Its Residuals                 | beginner     |           10 |
| m152 | Compare a Regressor with the Mean Baseline           | beginner     |           11 |
| m153 | Ignore Errors inside a Tolerance Band                | beginner     |           10 |
| m154 | Compare Agreement with Its Chance Baseline           | beginner     |           10 |
| m155 | Give Each Class Equal Total Training Weight          | beginner     |           10 |
| m156 | Classify by Learned Class Means                      | beginner     |           10 |
| m157 | Predict from Ordered Regression Bins                 | beginner     |           10 |
| m158 | Minimize One Ridge Coordinate Exactly                | intermediate |           10 |
| m159 | Find a Median under Unequal Observation Weights      | beginner     |           10 |
