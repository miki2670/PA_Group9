package org.group9.NoInheritance;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FinalClassTest {

    @Test
    void baz() {
        assertEquals(10, new FinalClass().baz());
    }

    @Test
    void foo() {
        assertEquals("foo", new FinalClass().foo());
    }

    @Test
    void foobaz() {
        assertEquals("foo10", new FinalClass().foobaz());
    }

    @Test
    void multipleCallsInOneTest() {
        assertEquals(10, new FinalClass().baz());
        assertEquals("foo", new FinalClass().foo());
    }
}