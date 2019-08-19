import java.io.*;
import java.util.*;
public class AddContinuosNumber
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int a[];
a=new int[100000]
int i,c=0;
for(i=0;i<n;i++)
{
a[i]=sc.nextInt();
}
for(i=0;i<n;i++)
{
c=c+a[i];
System.out.print(c);
System.out.print(" ");
}
}
}
