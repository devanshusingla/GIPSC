package math

const PI float64 = 3.14159265358979323846
const INF float64 = 1.7976931348623157e+308
const LN2 float64 = 0.6931471805599453

func Sin(x float64) float64 {
	var periods int =  int(x/(PI*float64(2)))
	x -= PI*2.0*periods
	return x - x*x*x/6.0 + x*x*x*x*x/120.0 - x*x*x*x*x*x*x/5040.0 
}
func Cos(x float64) float64 {
	return sin(PI/2.0 - x);
}

func Tan(x float64) float64 {

	if Cos(x) == 0.0 {
		return INF
	}
	return Sin(x)/Cos(x);
}

func Cot(x float64) float64 {
	if Tan(x) == 0.0 {
		return INF
	}
	return 1/Tan(x);
}

func Sec(x float64) float64 {
	if Cos(x) == 0.0 {
		return INF
	}
	return 1/Cos(x);
}

func Cosec(x float64) float64 {
	if Sin(x) == 0.0 {
		return INF
	}
	return 1/Sin(x);
}

func Exp(x float64) float64 {
	oper := 1.0
	fact := 1.0
	sum := 1.0
	N := 100
	for (i := 1; i <=N; i++) {
		oper *= x
		fact *= float64(i);
		sum += oper/fact;
	}
	return sum;
}

func Ln(x float64) float64 {
	if (x <= 0) {
		return -INF;
	}
	exponent := 0.0
	pw = 0
	for(i:=1; i<1000; i++){
		if(x < 1.0){
			break;
		}
		x /= 2.0
		pw += 1
	}
	oper := 1.0
	N := 100
	val = LN2*float64(pw);
	div = 1.0
	x -= 1.0
	for(i:=1; i<=N; i++){
		oper *= x;
		val += oper/div;
		div += 1.0
	}
	return val
}

func Sqrt(x float64) float64 {
	if(x < 0) {
		return -1
	}
	guess := 1.0
	N := 100
	for (i := 1; i<=N; i++){
		guess = (x/guess  + guess)/2.0
	}
	return guess
}

func Cbrt(x float64) float64 {
	if(x < 0) {
		return -1
	}
	return Exp(Ln(x)/3.0)
}

func PowMod(x int, n int, mod int) {
	if( n < 0){
		return -1;
	}
	res := 1;
    x = x % mod;
    if (x == 0){
		return 0;
	}
    for (; n > 0; ){
        if ((n & 1) > 0)
            res = (res*x) % mod;
 
        n >>= 1;
        x = (x*x) % mod;
    }
    return res;
}

func PowFloat(x float64, n int) {
	if(n < 0 ){
		return -1
	}
	res := 1.0;
    if (x == 0.0){
		return 0.0;
	}
    for (; n > 0; ){
        if ((n & 1) > 0)
            res = (res*x);
 
        n >>= 1;
        x = (x*x);
    }
    return res;
}

func Ceil(x float64) int {
	if(x - float64(int(x)) == 0.0){
		return int(x);
	}
	else{
		return int(x) + 1
	}
}

func Floor(x float64) int {
	return int(x);
}