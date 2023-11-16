package org.group9.Extend;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SquareTest {
    private final double width = 4.4;

    private Square sq;
    @BeforeEach
    void setUp() {
        sq = new Square(width);
    }

    // Should be rerun if Rectangle width changes
    @Test
    void width() {
        assertEquals(width, sq.width());
    }

    @Test
    void height() {
        assertEquals(width, sq.height());
    }

    @Test
    void area() {
        assertEquals(width*width, sq.area());
    }

    @Test
    void circumference() {
        assertEquals(4*width, sq.circumference());
    }

    @Test
    void multipleCallsInOneTest() {
        assertEquals(width, sq.width());
        assertEquals(width, sq.height());
        assertEquals(width*width, sq.area());
    }
}