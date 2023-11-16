package org.group9.Enums;

import java.util.Arrays;
import java.util.List;

public class UseEnum {

    public int enumToInt(TestEnum test) {
        return test.ordinal();
    }

    public TestEnum intToEnum(int index) {
        return TestEnum.values()[index];
    }

    public List<String> listEnums() {
        return Arrays.stream(TestEnum.values()).map(Enum::toString).toList();
    }
}
