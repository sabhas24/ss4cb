# Algorithm name
Selection sort

## Author
Juan Pablo Raimundi (2026-03-25)

## Algorithm description
Selection Sort is a simple comparison-based sorting algorithm.

* It divides the array into a sorted and an unsorted part.
The algorithm repeatedly selects the smallest element from the unsorted part. That element is then swapped with the first unsorted element.
After each iteration, the sorted portion grows by one element and the process continues until the entire array is sorted.
* It does not use additional data structures.
* Time complexity: O(n²) in all cases. Space complexity: O(1) (in-place)
* Inefficient for large datasets compared to algorithms like Heap Sort or Quick Sort

## Model used to create the base code
GPT-5.3

### Prompt
```
Écrivez un algorithme de selection-sort en python. 

Exigences: 
* Fournit de la documentation en français conforme à la réglementation PEP-8 
* Ne pas utiliser librairies 
* Ajoutez des commentaires informatifs en françai
```

## Obfuscated version
manually obfuscated