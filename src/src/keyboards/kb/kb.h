#ifndef KB_H
#define KB_H

#include "quantum.h"

#define KEYMAP( \
	      K001, K002, K003, K004, K005, K006, K007, K008, K009,                   K013, K014, K015, K016, K017, K018, K019, K020, K021,       \
	K100, K101, K102, K103, K104, K105, K106, K107, K108, K109,                   K113, K114, K115, K116, K117, K118, K119, K120, K121, K122, \
	                  K203, K204, K205, K206, K207, K208, K209, K210,       K212, K213, K214, K215, K216, K217, K218, K219,                   \
	                  K303, K304, K305, K306, K307, K308, K309,                   K313, K314, K315, K316, K317, K318, K319,                   \
	                                                                                                                                          \
	                                                K508, K509, K510,       K512, K513, K514,                                                 \
	                                                K608, K609, K610,       K612, K613, K614  \
) { \
	{ KC_NO, K001,  K002,  K003,  K004,  K005,  K006,  K007,  K008,  K009,  KC_NO, KC_NO, KC_NO, K013,  K014,  K015,  K016,  K017,  K018,  K019,  K020,  K021,  KC_NO }, \
	{ K100,  K101,  K102,  K103,  K104,  K105,  K106,  K107,  K108,  K109,  KC_NO, KC_NO, KC_NO, K113,  K114,  K115,  K116,  K117,  K118,  K119,  K120,  K121,  K122 }, \
	{ KC_NO, KC_NO, KC_NO, K203,  K204,  K205,  K206,  K207,  K208,  K209,  K210,  KC_NO, K212,  K213,  K214,  K215,  K216,  K217,  K218,  K219,  KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, K303,  K304,  K305,  K306,  K307,  K308,  K309,  KC_NO, KC_NO, KC_NO, K313,  K314,  K315,  K316,  K317,  K318,  K319,  KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K508,  K509,  K510,  KC_NO, K512,  K513,  K514,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, K608,  K609,  K610,  KC_NO, K612,  K613,  K614,  KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }  \
}

#endif