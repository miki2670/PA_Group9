import static org.junit.jupiter.api.Assertions.*;

// These tests should only be rerun if the tests change, as they do not depend on anything in this project
public class NoDependencyTest {
    @org.junit.jupiter.api.Test
    void test1() {
        assertEquals(5, 2+3);
    }

    @org.junit.jupiter.api.Test
    void test2() {
        assertEquals(6, 2*3);
    }


    @org.junit.jupiter.api.Test
    void test3() {
        var s = "Te";
        s += "st";
        assertEquals("Test", s);
    }

    @org.junit.jupiter.api.Test
    void test4() {
        assertThrows(ArithmeticException.class, () -> { @SuppressWarnings({"divzero", "NumericOverflow"}) var a = 5/0; });
    }
}
