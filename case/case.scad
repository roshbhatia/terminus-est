// Keyboard plate dimensions (from measurement)
plate_length = 443.86;
plate_width = 134.30;
bend_height = 15.00;

// Centering offset from measurement
plate_offset_x = -202.41;
plate_offset_y = 57.15;
plate_offset_z = 6.00;
bottom_of_plate = -7.50;
top_of_plate = 7.50;

// Case parameters
wall_thickness = 4;
bottom_thickness = 4;
tolerance = 0.3;

// Guide ridge parameters
ridge_thickness = 2;
ridge_height = 10;
ridge_inset = 2.55;

// Front and back wall parameters
fb_wall_top_clearance = -2.5;

// Side wall parameters
side_wall_offset = 0;
side_wall_bottom_z = -7.5;
side_wall_top_z = 10;
side_wall_lip_width = 3;
side_wall_lip_height = 2.5;
side_wall_lip_start_z = 7.5;
side_wall_lip_inset = 1;

// USB cutout parameters
usb_cutout_x = 0;
usb_cutout_width = 14;
usb_cutout_z_bottom = -12;
usb_cutout_height = 300;
usb_cutout_depth = 600; // Long cutout extending through case

// Rounding parameters
corner_radius = 3;

// Plate STL file
plate_stl_file = "../plate/v1/plate.stl";

// Small overlap to prevent gaps in union
overlap = 0.01;

module complete_case() {
  // Calculate shared dimensions
  case_outer_length = plate_length + 2 * wall_thickness + 2 * tolerance;
  case_outer_width = plate_width + 2 * wall_thickness + 2 * tolerance;
  bottom_z = bottom_of_plate - bottom_thickness - tolerance;

  fb_wall_height = (top_of_plate - fb_wall_top_clearance) - bottom_z;
  fb_wall_center_z = (bottom_z + top_of_plate - fb_wall_top_clearance) / 2;

  difference() {
    union() {
      // Bottom plate
      translate([0, 0, bottom_z + bottom_thickness / 2])
        cube([case_outer_length, case_outer_width, bottom_thickness + overlap], center=true);

      // Front wall
      translate([0, -(plate_width / 2 + wall_thickness / 2 + tolerance), (bottom_z + top_of_plate - fb_wall_top_clearance) / 2])
        cube(
          [
            case_outer_length + overlap,
            wall_thickness,
            fb_wall_height + overlap,
          ], center=true
        );

      // Back wall
      translate([0, (plate_width / 2 + wall_thickness / 2 + tolerance), (bottom_z + top_of_plate - fb_wall_top_clearance) / 2])
        cube(
          [
            case_outer_length + overlap,
            wall_thickness,
            fb_wall_height + overlap,
          ], center=true
        );

      // Side walls
      for (side = [-1, 1]) {
        translate(
          [
            side * (plate_length / 2 + wall_thickness / 2 + tolerance + side_wall_offset),
            0,
            (bottom_z + side_wall_top_z) / 2,
          ]
        )
          cube(
            [
              wall_thickness,
              plate_width + 2 * tolerance + overlap,
              side_wall_top_z - bottom_z + overlap,
            ], center=true
          );

        // Inward retention lip
        translate(
          [
            side * (plate_length / 2 + side_wall_offset + side_wall_lip_inset - side_wall_lip_width / 2),
            0,
            side_wall_lip_start_z + side_wall_lip_height / 2,
          ]
        )
          cube(
            [
              side_wall_lip_width + overlap,
              plate_width - 2 * tolerance,
              side_wall_lip_height,
            ], center=true
          );
      }

      // Front ridge
      translate([0, -(plate_width / 2 - ridge_inset), bottom_z + ridge_height / 2])
        cube(
          [
            plate_length - 2 * tolerance,
            ridge_thickness,
            ridge_height + overlap,
          ], center=true
        );

      // Back ridge
      translate([0, (plate_width / 2 - ridge_inset), bottom_z + ridge_height / 2])
        cube(
          [
            plate_length - 2 * tolerance,
            ridge_thickness,
            ridge_height + overlap,
          ], center=true
        );
    }

    // USB cutout - extends deep into case
    translate([usb_cutout_x, (plate_width / 2 + wall_thickness + tolerance - usb_cutout_depth / 2), usb_cutout_z_bottom + usb_cutout_height / 2])
      cube([usb_cutout_width, usb_cutout_depth, usb_cutout_height], center=true);
  }
}

color("dimgray")
  complete_case();

color("silver")
  translate([plate_offset_x, plate_offset_y, plate_offset_z])
    import(plate_stl_file);

