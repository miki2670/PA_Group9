package org.group9.Extend;

import static org.junit.jupiter.api.Assertions.*;

class RectangleTest {
    private final double width = 10.2;
    private final double height = 5.5;

    private Rectangle rect;
    @org.junit.jupiter.api.BeforeEach
    void setUp() {
        rect = new Rectangle(width, height);
    }

    @org.junit.jupiter.api.Test
    void width() {
        assertEquals(width, rect.width());
    }

    @org.junit.jupiter.api.Test
    void height() {
        assertEquals(height, rect.height());
    }

    @org.junit.jupiter.api.Test
    void area() {
        assertEquals(width*height, rect.area());
    }

    @org.junit.jupiter.api.Test
    void circumference() {
        assertEquals(2*width+2*height, rect.circumference());
    }
}