import java.util.Scanner;
class A{
int sum(int[] numbers){
int S=0;
for(int el : numbers)
S+=el;
return S;
}
}
class B extends A{
B(int[] arr){
System.out.println("Sum = " +sum(arr));
}
}
class C extends A{
C(int[] arr){
System.out.println("Average= "+sum(arr)/10.0);
}
}
class D extends C{
D(int[] arr){
super(arr);
}
}
public class DiShap{
 public static void main(String[]args){
System.out.println("Type 10 intgers for getting their sum and average : ");
Scanner sc=new Scanner(System.in);
int[] x=new int[10];
for(int i=0;i<10;i++){
x[i]=sc.nextInt();
}
sc.close();
B  b= new B(x);
D d=new D(x);
}
}
