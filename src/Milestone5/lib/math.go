package math

const PI float64 = 3.4

func Sin(x float64) float64 {
	periods :=  x/(PI*2.0)
	// Do typecast
	x -= PI*2.0*periods
	return x - x*x*x/6.0 + x*x*x*x*x/120.0 - x*x*x*x*x*x*x/5040.0 
}
