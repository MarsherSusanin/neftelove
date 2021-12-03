import SATELLITES from './satellites'

export default {
  LAND: {
    name_sputnik: SATELLITES.SENTINEL_2,
    contour_line_width: 2,
    sensitivity: 20,
    maxcc: 55,
  },
  SEA: {
    name_sputnik: SATELLITES.SENTINEL_1,
    contour_line_width: 2,
    sensitivity: 70,
    maxcc: 20,
  },
  RIVER: {
    name_sputnik: SATELLITES.SENTINEL_1,
    contour_line_width: 2,
    sensitivity: 20,
    maxcc: 55,
  }
}