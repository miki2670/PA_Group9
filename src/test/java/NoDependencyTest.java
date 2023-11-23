// These tests should only be rerun if the tests change, as they do not depend on anything in this project
public class NoDependencyTest {

    @org.junit.jupiter.api.Test
    void test1() {
        var a = 2 + 3;
        System.out.println(a == 5);
    }

    int calculate(int a, int b) {
        return a + b;
    }
}
