package org.group9.Sorter;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

class SorterTest {
    Sorter sorter;
    int[] arr;
    int[] expected;
    @BeforeEach
    void setUp() {
        sorter = new Sorter();
        arr = new int[100000];
        var random = new Random();
        for (int i = 0; i < 100000; i++) {
            arr[i] = random.nextInt();
        }

        expected = arr.clone();
        Arrays.sort(expected);
    }

    @Test
    void arraySort() {
        Arrays.sort(arr);
        assertArrayEquals(expected, arr);
    }
    @Test
    void bubbleSort() {
        sorter.BubbleSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    void selectionSort() {
        sorter.SelectionSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    void insertionSort() {
        sorter.InsertionSort(arr);
        assertArrayEquals(expected, arr);
    }
}