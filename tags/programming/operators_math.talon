tag: user.code_operators_math
-

# math operators
op (minus | subtract): user.code_operator_subtraction()
op (plus | add): user.code_operator_addition()
op (times | multiply): user.code_operator_multiplication()

op divide: user.code_operator_division()
op (integral | integer) divide: user.code_operator_division_integral()
op (fractional | real) divide: user.code_operator_division_fractional()
op (floating | float) divide: user.code_operator_division_floating()

op mod: user.code_operator_modulo()
op (integral | integer) mod: user.code_operator_modulo_integral()
op (fractional | real) mod: user.code_operator_modulo_fractional()
op (floating | float) mod: user.code_operator_modulo_floating()

op (power | exponent): user.code_operator_exponent()
op (integral | integer) (power | exponent): user.code_operator_exponent_integral()
op (fractional | real) (power | exponent): user.code_operator_exponent_fractional()
op (floating | float) (power | exponent): user.code_operator_exponent_floating()


# comparison operators
(op | is) equal: user.code_operator_equal()
(op | is) not equal: user.code_operator_not_equal()
(op | is) (greater | more): user.code_operator_greater_than()
(op | is) (less | below) [than]: user.code_operator_less_than()
(op | is) greater [than] or equal: user.code_operator_greater_than_or_equal_to()
(op | is) less [than] or equal: user.code_operator_less_than_or_equal_to()

# logical operators
(op | logical) and: user.code_operator_and()
(op | logical) or: user.code_operator_or()
