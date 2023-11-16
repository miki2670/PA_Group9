package org.group9.Implement;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class OverrideInterfaceTest {
    OverrideInterface override;

    @BeforeEach
    void setUp() {
        override = new OverrideInterface();
    }

    @Test
    void DefaultNoOverride() {
        assertEquals("Default" ,override.DefaultNoOverride());
    }

    @Test
    void defaultOverride() {
        assertEquals("Overridden" ,override.DefaultOverride());
    }

    @Test
    void defaultOverrideAndExtend() {
        assertEquals("Override and extended", override.DefaultOverrideAndExtend());
    }

    @Test
    void multipleCallsInOneTest() {
        assertEquals("Overridden" ,override.DefaultOverride());
        assertEquals("Override and extended", override.DefaultOverrideAndExtend());
    }
}