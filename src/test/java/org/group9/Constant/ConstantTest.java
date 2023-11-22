package org.group9.Constant;

class ConstantTest {

    @org.junit.jupiter.api.Test
    void getConstant() {
        System.out.println(Constant.constant == new Constant().getConstant());
    }

    @org.junit.jupiter.api.Test
    void noConstant() {
        System.out.println(new Constant().noConstant() > 0);
    }

    @org.junit.jupiter.api.Test
    void multipleCallsInOneTest() {
        System.out.println(Constant.constant == new Constant().getConstant());
        System.out.println(new Constant().noConstant() > 0);
    }
}