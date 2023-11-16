package org.group9.Implement;

public interface ITest {
    default String DefaultNoOverride() {
        return "Default";
    }

    default String DefaultOverride() {
        return "DefaultToOverride";
    }

    default String DefaultOverrideAndExtend() {
        return "Override";
    }
}
