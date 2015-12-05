(define (last-pair-def items)
  (if (null? (cdr items))
      items
      (last-pair (cdr items))))

; testing
(define list1 (list 1 2 3 4 5))
(last-pair-def list1)

(define list2 (list 1))
(last-pair-def list2)