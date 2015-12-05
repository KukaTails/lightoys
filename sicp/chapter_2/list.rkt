(define (list-ref-def items n)
  (if (= n 0)
      (car items)
      (list-ref-def (cdr items) (- n 1))))

(define (length-list items)
  (if (null? items)
      0
      (+ 1 (length-list (cdr items)))))

(define (length-list-i items)
  (define (iter a count)
    (if (null? a)
        count
        (iter (cdr a) (+ 1 count))))
  (iter items 0))

(define (append-list list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (append-list (cdr list1) list2))))

; testing
(define array1 (list 1 2 3 4 5))
(define array2 (list 6 7 8))

(list-ref-def array1 0)
(list-ref-def array1 4)
(length-list array1)

(list-ref-def array2 0)
(list-ref-def array2 2)
(length-list array2)

(define array3 (append-list array1 array2))
(length-list array3)
(list-ref-def array3 6)