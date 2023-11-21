package org.group9.Sorter;

public class Sorter {
    public void BubbleSort(int[] arr) {
        for(int i = 0; i < arr.length; i++){
            for(int j=0; j < arr.length - 1; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public void SelectionSort(int[] arr) {
        for(int i=0;i<arr.length; i++) {
            int minIndex = i;
            for(int j=i+1;j<arr.length; j++) {
                if(arr[j]<arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    public void InsertionSort(int[] arr) {
        for(int i = 1;i < arr.length; i++) {
            int j = i;
            while(j > 0 && arr[j] < arr[j-1]) {
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
                j--;
            }
        }
    }
}
