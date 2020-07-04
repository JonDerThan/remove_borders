Python script to remove black borders from images.

# Usage
The in- and output directorys are specified through variables.
`dir0` is the input directory (std: `./data/`), `outdir0` is the output directory (std: `./out/`).

If a part of the image gets removed or the border is not removed completely, change the `max_color` variable.
If too much of the image gets removed decrease the three values; if the border is not removed completely increase the three values.

```
max_color = [0, 0, 0]

# Only removes borders that are 100% black (hex: #000000).
```
```
max_color = [20, 20, 20]

# Removes borders that only contain color between completely black (hex: #000000) and a dark gray (hex: #141414)
```
