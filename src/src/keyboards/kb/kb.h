#ifndef KB_H
#define KB_H

#include "quantum.h"

#define KEYMAP( \
	      K001, K002, K003, K004, K005, K006,                                                       K016, K017, K018, K019, K020, K021,       \
	      K101, K102, K103, K104, K105, K106, K107,                                           K115, K116, K117, K118, K119, K120, K121,       \
	K200, K201, K202, K203, K204, K205, K206,                         K211,                   K215, K216, K217, K218, K219, K220, K221, K222, \
	K300, K301, K302, K303, K304, K305, K306,                   K310,       K312,             K315, K316, K317, K318, K319, K320, K321,       \
	      K401, K402, K403, K404, K405, K406, K407,                   K411,             K414, K415, K416, K417, K418, K419, K420,             \
	                        K504, K505, K506, K507,                                     K514, K515, K516, K517,                               \
	                                                K608, K609, K610, K611, K612, K613, K614  \
) { \
	{ KC_NO, K001,  K002,  K003,  K004,  K005,  K006,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K016,  K017,  K018,  K019,  K020,  K021,  KC_NO }, \
	{ KC_NO, K101,  K102,  K103,  K104,  K105,  K106,  K107,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K115,  K116,  K117,  K118,  K119,  K120,  K121,  KC_NO }, \
	{ K200,  K201,  K202,  K203,  K204,  K205,  K206,  KC_NO, KC_NO, KC_NO, KC_NO, K211,  KC_NO, KC_NO, KC_NO, K215,  K216,  K217,  K218,  K219,  K220,  K221,  K222 }, \
	{ K300,  K301,  K302,  K303,  K304,  K305,  K306,  KC_NO, KC_NO, KC_NO, K310,  KC_NO, K312,  KC_NO, KC_NO, K315,  K316,  K317,  K318,  K319,  K320,  K321,  KC_NO }, \
	{ KC_NO, K401,  K402,  K403,  K404,  K405,  K406,  K407,  KC_NO, KC_NO, KC_NO, K411,  KC_NO, KC_NO, K414,  K415,  K416,  K417,  K418,  K419,  K420,  KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, K504,  K505,  K506,  K507,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K514,  K515,  K516,  K517,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K608,  K609,  K610,  K611,  K612,  K613,  K614,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }  \
}

#endif