package org.group9.Implement;

public interface ITest {
    default String DefaultNoOverride() {
        return "Default";
    }

    default String DefaultOverride() {
        return "DefaultToerride";
    }

    default String DefaultOverrideAndExtend() {
        return "Override";
    }
}
