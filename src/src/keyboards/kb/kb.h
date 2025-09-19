#ifndef KB_H
#define KB_H

#include "quantum.h"

#define KEYMAP( \
	      K001, K002, K003, K004, K005, K006, K007,                         K012, K013, K014, K015, K016, K017, K018, K019, \
	K100, K101, K102, K103, K104, K105, K106, K107,                   K111, K112, K113, K114, K115, K116, K117, K118, K119, \
	K200, K201, K202, K203, K204, K205, K206, K207,                   K211, K212, K213, K214, K215, K216, K217, K218,       \
	      K301, K302, K303, K304, K305, K306, K307,                         K312, K313, K314, K315, K316, K317, K318,       \
	                                          K407, K408,             K411, K412,                                           \
	                                    K506, K507, K508,       K510, K511, K512  \
) { \
	{ KC_NO, K001,  K002,  K003,  K004,  K005,  K006,  K007,  KC_NO, KC_NO, KC_NO, KC_NO, K012,  K013,  K014,  K015,  K016,  K017,  K018,  K019 }, \
	{ K100,  K101,  K102,  K103,  K104,  K105,  K106,  K107,  KC_NO, KC_NO, KC_NO, K111,  K112,  K113,  K114,  K115,  K116,  K117,  K118,  K119 }, \
	{ K200,  K201,  K202,  K203,  K204,  K205,  K206,  K207,  KC_NO, KC_NO, KC_NO, K211,  K212,  K213,  K214,  K215,  K216,  K217,  K218,  KC_NO }, \
	{ KC_NO, K301,  K302,  K303,  K304,  K305,  K306,  K307,  KC_NO, KC_NO, KC_NO, KC_NO, K312,  K313,  K314,  K315,  K316,  K317,  K318,  KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K407,  K408,  KC_NO, KC_NO, K411,  K412,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K506,  K507,  K508,  KC_NO, K510,  K511,  K512,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }  \
}

#endif