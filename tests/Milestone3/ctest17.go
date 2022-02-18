package main
type Co_ordinates struct{
    x int
    y int 
}
type Point struct{
    name string
    pt Co_ordinates
}
func main(){
   var P Point 
   scan(P.pt.x,P.pt.y)
   P.name="test"

   print(P.name,"\n")
   print(P.pt.x," ",P.pt.y,"\n")

}
