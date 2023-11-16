package org.group9.Enums;

import org.group9.Constant.Constant;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class UseEnumTest {

    @Test
    void enumToInt() {
        assertEquals(0, new UseEnum().enumToInt(TestEnum.Option1));
    }

    @Test
    void intToEnum() {
        assertEquals(TestEnum.Option2, new UseEnum().intToEnum(1));
    }

    @Test
    void listEnums() {
        assertIterableEquals(Arrays.stream(new String[]{"Option1", "Option2", "Option3"}).toList(), new UseEnum().listEnums());
    }

    @Test
    void multipleCallsInOneTest() {
        assertEquals(0, new UseEnum().enumToInt(TestEnum.Option1));
        assertIterableEquals(Arrays.stream(new String[]{"Option1", "Option2", "Option3"}).toList(), new UseEnum().listEnums());
    }
}