#ifndef KB_H
#define KB_H

#include "quantum.h"

#define KEYMAP( \
	      K001, K002, K003, K004, K005, K006, K007,                                     K014, K015, K016, K017, K018, K019, K020,       \
	K100, K101, K102, K103, K104, K105, K106,             K109,             K112,       K114, K115, K116, K117, K118, K119, K120, K121, \
	K200, K201, K202, K203, K204, K205, K206,             K209,             K212,       K214, K215, K216, K217, K218, K219, K220,       \
	      K301, K302, K303, K304, K305, K306, K307,       K309,             K312,       K314, K315, K316, K317, K318, K319, K320,       \
	      K401, K402,             K405, K406, K407,                               K413, K414, K415,             K418, K419,             \
	                                    K506, K507, K508, K509,                   K513, K514, K515  \
) { \
	{ KC_NO, K001,  K002,  K003,  K004,  K005,  K006,  K007,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K014,  K015,  K016,  K017,  K018,  K019,  K020,  KC_NO }, \
	{ K100,  K101,  K102,  K103,  K104,  K105,  K106,  KC_NO, KC_NO, K109,  KC_NO, KC_NO, K112,  KC_NO, K114,  K115,  K116,  K117,  K118,  K119,  K120,  K121 }, \
	{ K200,  K201,  K202,  K203,  K204,  K205,  K206,  KC_NO, KC_NO, K209,  KC_NO, KC_NO, K212,  KC_NO, K214,  K215,  K216,  K217,  K218,  K219,  K220,  KC_NO }, \
	{ KC_NO, K301,  K302,  K303,  K304,  K305,  K306,  K307,  KC_NO, K309,  KC_NO, KC_NO, K312,  KC_NO, K314,  K315,  K316,  K317,  K318,  K319,  K320,  KC_NO }, \
	{ KC_NO, K401,  K402,  KC_NO, KC_NO, K405,  K406,  K407,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K413,  K414,  K415,  KC_NO, KC_NO, K418,  K419,  KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K506,  K507,  K508,  K509,  KC_NO, KC_NO, KC_NO, K513,  K514,  K515,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }  \
}

#endif