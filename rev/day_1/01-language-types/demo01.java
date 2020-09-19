// Some Example Java code
import java.util.*;

public class demo01 {
    public static int bar(int n) {
        return n + 20;
    }

    public static int foo(int n) {
        return bar(n) * 2;
    }

    public static void main(String args[]) {
        System.out.println(foo(10));

    }
}
