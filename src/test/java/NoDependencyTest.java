
// These tests should only be rerun if the tests change, as they do not depend on anything in this project
public class NoDependencyTest {
    @org.junit.jupiter.api.Test
    void test1() {
        var val = 2 + 3;
        System.out.println(val == 5);
    }

    @org.junit.jupiter.api.Test
    void test2() {
        var val = 2 * 3;
        System.out.println(val == 6);
    }

    @org.junit.jupiter.api.Test
    void test3() {
        var s = "Te";
        s += "st";
        System.out.println("Test" == s);
    }
}
