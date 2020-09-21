void single_call(int arg) {
	printf("SINGLE CALL %d\n", arg);
}

int single_call_return(int arg) {
	printf("SINGLE CALL RETURN %d\n", arg);
	arg += 100;
	return arg;
}

void multi_call(int arg, int arg2, int arg3) {
	printf("MUTI CALL %d %d %d\n", arg, arg2, arg3);
}

int multi_call_return(int arg, int arg2, int arg3) {
	printf("MUTI CALL %d %d %d\n", arg, arg2, arg3);
	return arg + arg2 + arg3;
}


int var_arg(int count, ...) {
	int var;
	va_list ap;
	va_start(ap, count);
	for (int i = 0; i < count; i++) {
		var = va_arg(ap, int);
		printf("VAR ARG %d\n", var);
	}
	va_end(ap);
	return 0;
}

int many_args(int arg, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8, int arg9, int arg10) {
	printf("%d %d %d %d %d %d %d %d %d %d\n", arg, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
	return arg + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10;
}

int main(int argc, char ** argv) {
	int a = 16;
	int b = 100;
	int c = 45;
	single_call(a);
	single_call_return(a);
	multi_call(a, b, c);
	multi_call_return(a, b, c);
	var_arg(10, 6, 3, 5, 3, 1, 6, 3, 5, 3, 1);
	a = many_args(10, 6, 3, 5, 3, 1, 7, 3, 5, 2);
	printf("%d\n", a);
}
