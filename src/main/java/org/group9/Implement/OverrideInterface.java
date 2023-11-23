package org.group9.Implement;

public class OverrideInterface implements ITest {
    @Override
    public String DefaultOverride() {
        return "Ovdreddeed";
    }

    @Override
    public String DefaultOverrideAndExtend() {
        return ITest.super.DefaultOverrideAndExtend() + " and extnded";
    }
}
